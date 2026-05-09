# Objective
Create two Python scripts to manage an iPhone photo backup folder. The scripts will track files and identify deleted photos, saving the list and file size stats to a JSON file for later deletion from the iPhone via MTP.

# Key Files & Context
- `index_photos.py`: Script to generate the initial baseline.
- `find_deleted.py`: Script to compare the folder against the baseline.
- `index.json`: Data file storing the baseline (relative paths and sizes).
- `deleted.json`: Data file storing missing files and their sizes.

# Implementation Steps
1. **Draft `index_photos.py`:**
   - Use `os.walk` or `pathlib` to recursively scan the target directory.
   - For each file, record the relative path and file size in bytes.
   - Save this dictionary to `index.json`.
2. **Draft `find_deleted.py`:**
   - Load `index.json`.
   - Scan the target directory again to build the current state.
   - Compare the current state against `index.json` to identify missing keys (deleted files).
   - Calculate the total size of the deleted files.
   - Save the list of missing files (with paths and sizes) to `deleted.json`.
   - Print a summary message: "X GB will be freed" (converting bytes to GB).
3. **MTP Deletion Script (Out of Scope for initial draft):**
   - Acknowledge that `deleted.json` is formatted specifically for a future script to read and execute MTP delete commands.

# Verification & Testing
- Create a dummy directory structure with test files.
- Run `index_photos.py` to create `index.json`.
- Delete a file manually.
- Run `find_deleted.py` to verify `deleted.json` is created with correct paths and size calculations.