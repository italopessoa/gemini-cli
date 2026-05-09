import os
import json
import argparse
from pathlib import Path

def find_deleted(target_dir, index_file):
    if not os.path.exists(index_file):
        print(f"Error: Index file {index_file} not found.")
        return {}, 0

    with open(index_file, "r", encoding="utf-8") as f:
        old_index = json.load(f)
    
    target_path = Path(target_dir).resolve()
    if not target_path.exists():
        print(f"Error: Directory {target_dir} does not exist.")
        return {}, 0

    current_files = set()
    for root, _, files in os.walk(target_path):
        for file in files:
            file_path = Path(root) / file
            try:
                rel_path = str(file_path.relative_to(target_path))
                current_files.add(rel_path)
            except ValueError:
                continue
            
    deleted_files = {}
    total_bytes = 0
    
    for rel_path, size in old_index.items():
        if rel_path not in current_files:
            deleted_files[rel_path] = size
            total_bytes += size
            
    return deleted_files, total_bytes

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find deleted photos compared to index.")
    parser.add_argument("directory", help="Current target directory")
    parser.add_argument("--index", default="index.json", help="Baseline JSON index")
    parser.add_argument("--output", default="deleted.json", help="Output JSON for deleted files")
    args = parser.parse_args()
    
    deleted, bytes_saved = find_deleted(args.directory, args.index)
    
    if deleted:
        with open(args.output, "w", encoding="utf-8") as f:
            json.dump(deleted, f, indent=4)
            
        gb = bytes_saved / (1024**3)
        print(f"Found {len(deleted)} deleted files.")
        print(f"Saved to {args.output}")
        print(f"Deleting these from iPhone will save {gb:.2f} GB.")
    else:
        print("No deleted files found.")
