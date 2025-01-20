#Program to list files in the user given folders
import os

folders = input("Enter the folder names by giving space in between: ").split()
for folder in folders:
    try:
        files_list = os.listdir(folder)
        print("Files in the folder: "+folder)
        for file in files_list:
            print(file)
    except(FileNotFoundError):
        print(f"Enter a valid Folder Name as folder {folder} does not exist")
    except(PermissionError):
        print(f"You dont have permission to access folder {folder}")
    