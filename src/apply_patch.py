import os
import sys
import json
import zlib
import tkinter as tk
from tkinter import filedialog, messagebox

def crc32_of_file(path):
    prev = 0
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            prev = zlib.crc32(chunk, prev)
    return f"{prev & 0xFFFFFFFF:08X}".upper()

def apply_ips_patch(rom_path, ips_path, output_path):
    with open(rom_path, "rb") as f:
        rom_data = bytearray(f.read())

    with open(ips_path, "rb") as f:
        ips_data = f.read()

    if not ips_data.startswith(b"PATCH") or not ips_data.endswith(b"EOF"):
        raise ValueError("Invalid IPS file format")

    offset = 5
    while ips_data[offset:offset+3] != b"EOF":
        addr = int.from_bytes(ips_data[offset:offset+3], "big")
        offset += 3
        size = int.from_bytes(ips_data[offset:offset+2], "big")
        offset += 2
        if size == 0:  # RLE encoded
            rle_size = int.from_bytes(ips_data[offset:offset+2], "big")
            offset += 2
            value = ips_data[offset]
            offset += 1
            for i in range(rle_size):
                if addr+i < len(rom_data):
                    rom_data[addr+i] = value
                else:
                    rom_data.extend([0] * (addr+i - len(rom_data) + 1))
                    rom_data[addr+i] = value
        else:  # Direct patch
            for i in range(size):
                if addr+i < len(rom_data):
                    rom_data[addr+i] = ips_data[offset+i]
                else:
                    rom_data.extend([0] * (addr+i - len(rom_data) + 1))
                    rom_data[addr+i] = ips_data[offset+i]
            offset += size

    with open(output_path, "wb") as f:
        f.write(rom_data)

def main():
    root = tk.Tk()
    root.withdraw()

    # Select JSON metadata
    json_path = filedialog.askopenfilename(
        title="Select patch JSON file",
        filetypes=[("Patch metadata", "*.json")]
    )
    if not json_path:
        return

    with open(json_path, "r", encoding="utf-8") as f:
        metadata = json.load(f)

    ips_path = os.path.join(os.path.dirname(json_path), metadata["patch_file"])
    output_path = os.path.join(os.path.dirname(json_path), metadata["output_file"])

    # Select ROM file
    rom_path = filedialog.askopenfilename(
        title="Select input ROM file",
        filetypes=[("ROM files", "*.rom *.bin"), ("All files", "*.*")]
    )
    if not rom_path:
        return

    # Validate input CRC
    actual_crc = crc32_of_file(rom_path)
    if actual_crc != metadata["input_crc32"]:
        messagebox.showerror("Error", f"Input CRC32 mismatch!\nExpected: {metadata['input_crc32']}\nGot: {actual_crc}")
        return

    # Apply patch
    apply_ips_patch(rom_path, ips_path, output_path)

    # Validate output CRC
    actual_out_crc = crc32_of_file(output_path)
    if actual_out_crc != metadata["output_crc32"]:
        messagebox.showerror("Error", f"Patched CRC32 mismatch!\nExpected: {metadata['output_crc32']}\nGot: {actual_out_crc}")
        return

    messagebox.showinfo("Success", f"Patched ROM saved as:\n{output_path}")

if __name__ == "__main__":
    main()
