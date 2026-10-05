import os

csv_filename = input("Enter the CSV filename: ").strip()

if not os.path.exists(csv_filename):
    print(f"Error: The file '{csv_filename}' does not exist.")
elif not os.path.isfile(csv_filename):
    print(f"Error: '{csv_filename}' is a directory, not a file.")
else:
    #csv file found
    total_lines = 0
    cse_count = 0
    ee_count = 0

    with open(csv_filename, mode='r') as file:
        for line in file:
            total_lines += 1            
            line_upper = line.upper()
            
            if "CSE" in line_upper:
                cse_count += 1
            elif "EE" in line_upper:
                ee_count += 1
    print(f"Total number of lines: {total_lines}")
    print(f"Total students in CSE department: {cse_count}")
    print(f"Total students in EE department: {ee_count}")
    print(f"Analysis Completed!")
