# Neo-Geo IPS Patcher ԅ(¬‿¬ԅ)


## 🔧 What is this?

A standalone **IPS patcher** for the Neo Geo ROM modifications you can find on this account.  
It provides a simple way for users to apply `.ips` patches with a clickable `.exe`, no command line required.

- Written in Python (`nips.py`)  
- Built into a standalone Windows binary (`nips.exe`)  

Alternatively, you can use the `.ips` patches with these well-established IPS Patchers:  
- Lunar IPS - https://www.romhacking.net/utilities/240  
- Floating IPS - https://github.com/Alcaro/Flips


## 🕹️ For End Users

### Usage:

1. **Download `nips.exe`**  
   - Go to the [Releases page](../../releases) and download the latest `nips.exe`.  
     (As it's an exe file, it may trigger your browser's protection logic. In any case, always virus-scan any downloaded exe file before running.)  

2. **Download a patch package**  
   - Each patch repository, e.g. [Universe BIOS 4.0 PICKnMIX Patch](https://github.com/clearpaper/uni-bios_4_0_PnM), has `.ips` and `.json` files inside a ZIP release.  
   - Extract the ZIP so you have access to the patch files.

3. **Run `nips.exe`**  
   - Double-click `nips.exe`.  
   - When prompted, select the `.json` patch file you want to apply.

4. **Select the input ROM**  
   - When prompted, select the original file that the patch expects, typically with `.rom` or `.bin` extensions, e.g. `uni-bios_4_0.rom`.  
   - `nips.exe` will check the input ROM's CRC32 checksum against the required one and will display an error if it does not match.

5. **Patched ROM generated**  
   - If the CRC32 matches, the `nips.exe` will apply the changes and create a new ROM file with the name as defined in the `.json` file, e.g. `uni-bios_4_0_PnM.rom`.
   - `nips.exe` will check the output ROM's CRC32 checksum against the expected one and will display an error if it does not match.  


## 🚀 Example: Universe BIOS 4.0 PICKnMIX Patch

### Patch files:
- `uni-bios_4_0_PnM_patch.ips`  
- `uni-bios_4_0_PnM_patch.json`  

### Input ROM:
- Filename: `uni-bios_4_0.rom`  
- Expected CRC32: `A7AAB458`  

### Output ROM:
- Filename: `uni-bios_4_0_PnM.rom`  
- Expected CRC32: `B204F293`  

### Steps:
1. Run `nips.exe`.  
2. Select `uni-bios_4_0_PnM_patch.json`.  
3. Select your `uni-bios_4_0.rom`  
4. `nips.exe` creates `uni-bios_4_0_PnM.rom`.  


## ❓ Troubleshooting
- **Input CRC mismatch error:** Your ROM isn’t the correct version. Check that it matches the expected input CRC32.  
- **No patched file appears:** Ensure you have permission to write in the folder that contains the `json` and `ips` files.   
- **Output CRC32 mismatch error:** The patch may not have been applied correctly. Redownload the patch package and try again.  


## 🛠 For Developers

You can run `nips.py` directly or build the `nips.exe` yourself:

### Build Requirements
- Python 3.10+  
- [PyInstaller](https://pyinstaller.org)  

### Build Instructions

Run these commands in a terminal:

```
pip install pyinstaller
pyinstaller --onefile src/nips.py
```

Result: `dist/nips.exe`

---


## 📜 License
MIT License — see [LICENSE](LICENSE).  

---

## ⚖️ Legal
This tool applies patches only.  **No ROMs are included.**  
It does not contain, distribute, or endorse sharing of copyrighted ROMs or BIOS images.  
