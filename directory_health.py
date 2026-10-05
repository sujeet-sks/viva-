import os

target_directory = input("Enter the directory path: ")

if not os.path.exists(target_directory):
    print("Error: Directory does not exist.")
else:
    file_count = 0
    total_bytes = 0

    for root, dirs, files in os.walk(target_directory):
        for filename in files:
            file_count += 1
            full_path = os.path.join(root, filename)
            total_bytes += os.path.getsize(full_path)

    size_in_mb = total_bytes / (1024 * 1024)

    #Classification
    if size_in_mb < 100:
        category = "Small (<100MB)"
    elif size_in_mb <= 1000:
        category = "Medium (100MB - 1GB)"
    else:
        category = "Large (>1GB)"

    # Print
    print(f"Total Files: {file_count}")
    print(f"Disk Usage: {size_in_mb:.2f} MB")
    print(f"Directory Size: {category}")
