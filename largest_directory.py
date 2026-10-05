import os

home_dir = os.path.expanduser("~")
dir_sizes = {}

for root, dirs, files in os.walk(home_dir):
    current_dir_size = 0
    
    for file in files:
        file_path = os.path.join(root, file)
        try:
            if os.path.exists(file_path) and not os.path.islink(file_path):
                current_dir_size += os.path.getsize(file_path)
        except (PermissionError, FileNotFoundError):
            continue
            
    path_parts = root.split(os.sep)
    for i in range(len(path_parts)):
        parent_path = os.sep.join(path_parts[:i+1])
        if parent_path.startswith(home_dir):
            dir_sizes[parent_path] = dir_sizes.get(parent_path, 0) + current_dir_size

#Sort
sorted_dirs = sorted(dir_sizes.items(), key=lambda x: x[1], reverse=True)

def format_size(bytes_size):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes_size < 1024.0:
            return f"{bytes_size:.2f} {unit}"
        bytes_size /= 1024.0
    return f"{bytes_size:.2f} PB"

print(f"{'Directory Path':<60} | {'Size':<12}")
print("-" * 75)

for path, size in sorted_dirs[:10]:
    print(f"{path:<60} | {format_size(size):<12}")
