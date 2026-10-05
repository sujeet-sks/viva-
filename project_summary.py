import os
import datetime

dir_name = "D:/IITB_sem1/cs744_DECS/cs744-autumn2026-lab1"

if not os.path.exists(dir_name):
    print(f"Error: The directory '{dir_name}' does not exist.")
elif not os.path.isdir(dir_name):
    print(f"Error: '{dir_name}' is a file, not a directory.")
else:
    #directory found
    total_files = 0
    total_size = 0
    file_list = []

    for root, dirs, files in os.walk(dir_name):
        total_files += len(files)

        for filename in files:
            file_path = os.path.join(root, filename)
            if os.path.exists(file_path):
                total_size += os.path.getsize(file_path)
                mod_time = os.path.getmtime(file_path)
                file_list.append((file_path, mod_time))

    print(f"Total number of files: {total_files}")
    print(f"Total disk usage: {total_size} bytes)")
                
    file_list.sort(key=lambda x: x[1], reverse=True)
    #display the sorted files
    print("\n--- Files Sorted by Modified Time (Newest First) ---")
    for path, timestamp in file_list:
        readable_time = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
        print(f"[{readable_time}] {path}")

    print(f"Analysis Completed!")



