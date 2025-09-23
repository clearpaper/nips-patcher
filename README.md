# Neo Geo IPS Patcher

## 🔧 What is this?

This is a custom **IPS patcher** for the ROM modifications you can find on this account.  
It provides a simple way for users to apply `.ips` patches with a clickable `.exe`, no command line required.

- Written in Python (`apply_patch.py`)  
- Built into a standalone Windows binary (`apply_patch.exe`)  
- Each patch repo contains an `.ips` patch and a companion `.json` file that defines:
  - Expected input ROM CRC32
  - Expected output ROM CRC32
  - Output file name
  - Notes / description

⚠️ **No ROMs are included**. You must supply your own, legally obtained ROMs.

---

## 🕹️ For End Users

### Usage:

1. **Download `apply_patch.exe`**  
   - Go to the [Releases page](../../releases) and download the latest `apply_patch.exe`.  

2. **Download a patch package**  
   - Each patch repo (for example, `unibios-4.0-pnm`) provides its own `.ips` and `.json` files inside a ZIP release.  
   - Extract the ZIP so you have access to the patch files.

3. **Run the patcher**  
   - Double-click `apply_patch.exe`.  
   - When prompted, select the `.json` patch file you want to apply.

4. **Select the input ROM**  
   - Choose the original `.rom` or `.bin` file that the patch expects.  
   - The patcher will check the input ROM's CRC32 checksum against the required patch CRC32 checksum.  
   - If it doesn’t match, you’ll see an error.

5. **Get the patched ROM**  
   - If the CRC32 matches, the patcher will apply the changes and create a new ROM file.  
   - The name of the output file is defined in the patch’s `.json` (for example, `uni-bios_4_0_PnM.rom`).

6. **Verify the patched ROM**  
   - The patcher will check the output ROM's CRC32 checksum against the expected patch CRC32 checksum.  
   - If it doesn’t match, you’ll see an error.

7. **Done!**  
   - Use the patched ROM in your emulator or hardware setup.

---

## 🚀 Example: Universe BIOS 4.0 PICKnMIX Patch

### Features:

A. *On cold boot*
   1. runs PICKnMIX mode by default, OR
   2. runs original 161-in-1 Game Select Menu (GSM) by holding Player 1 START button  

B. *Warm reset. While cursor on "SOFT REBOOT SYSTEM" of "IN GAME MENU"*  
   1. press A button resets current game, allowing game re-selection through PICKnMIX mode, OR
   2. press A button while holding START resets to 161-in-1 GSM.

### Patch files:
- `uni-bios_4_0_PnM_patch.ips`  
- `uni-bios_4_0_PnM_patch.json`  

### Input ROM:
- Filename: `uni-bios_4_0.rom`  
- Expected CRC32: `A7AAB458`  

### Output ROM:
- Filename: `uni-bios_4_0_PnM.rom`  
- Expected CRC32: `078E2043`  

### Steps:
1. Run `apply_patch.exe`.  
2. Select `uni-bios_4_0_PnM_patch.json`.  
3. Select your `uni-bios_4_0.rom`  
4. The patcher creates `uni-bios_4_0_PnM.rom`.  

---

## ❓ Troubleshooting
- **CRC mismatch error:** Your ROM isn’t the correct version. Check that it matches the expected input CRC32.  
- **No patched file appears:** Ensure you have permission to write in the folder where you ran `apply_patch.exe`.  
- **Output CRC32 doesn’t match:** The patch may not have been applied correctly. Redownload the patch package and try again.  

---

## 🛠 For Developers

You can run `apply_patch.py` directly or build the `apply_patch.exe` yourself:

### Requirements
- Python 3.10+  
- [PyInstaller](https://pyinstaller.org)  

### Build Instructions

Run these commands in a terminal:

```
pip install pyinstaller
pyinstaller --onefile src/apply_patch.py
```

Result: `dist/apply_patch.exe`

---


## 📜 License
MIT License — see [LICENSE](LICENSE).  

---

## ⚖️ Legal
This tool applies patches only.  
It does not contain, distribute, or endorse sharing of copyrighted ROMs or BIOS images.  
