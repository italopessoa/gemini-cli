import os
import json
import argparse
from pathlib import Path

def index_folder(target_dir):
    photo_index = {}
    target_path = Path(target_dir).resolve()
    
    if not target_path.exists():
        print(f"Error: Directory {target_dir} does not exist.")
        return None

    for root, _, files in os.walk(target_path):
        for file in files:
            file_path = Path(root) / file
            # Use relative path as key
            rel_path = str(file_path.relative_to(target_path))
            try:
                size = file_path.stat().st_size
                photo_index[rel_path] = size
            except FileNotFoundError:
                continue
                
    return photo_index

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Index photos in a folder.")
    parser.add_argument("directory", help="Target directory to index")
    parser.add_argument("--output", default="index.json", help="Output JSON file")
    args = parser.parse_args()
    
    data = index_folder(args.directory)
    if data is not None:
        with open(args.output, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        
        print(f"Indexed {len(data)} files. Saved to {args.output}")
