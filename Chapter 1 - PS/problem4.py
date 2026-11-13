import os

# Select the directory whose contain you want to list
path = input("Enter directory path (leave blank for current directory): ").strip()
if path == "":
    path = "."

try:
    # Use the os module to list the directory content
    contents = os.listdir(path)
    print(f"\nContents of '{os.path.abspath(path)}':\n")
    for item in contents:
        print(item)
except FileNotFoundError:
    print("Error: that directory does not exist.")
except NotADirectoryError:
    print("Error: that path is not a directory.")
except PermissionError:
    print("Error: you don't have permission to read that directory.")