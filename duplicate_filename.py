import os

target_directory = r"D:/IITB_sem1/cs744_DECS/cs744-autumn2026-lab1"  

file_tracker = {}

for root, dirs, files in os.walk(target_directory):
    for filename in files:
        full_path = os.path.join(root, filename)
        if filename not in file_tracker:
            file_tracker[filename] = []
        file_tracker[filename].append(full_path)

duplicate_count = 0

for filename, paths in file_tracker.items():
    if len(paths) > 1:
        duplicate_count += 1
        print(f"Duplicate File: {filename}") 
        for path in paths:
            print(f"  Location: {path}")
        print("-" * 50)

if duplicate_count == 0:
    print("No duplicate filenames found. All files have unique names!")
