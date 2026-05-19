"""
file_organizer.py

This script organizes files in a folder by file type.
It moves images, documents, and spreadsheets into separate folders.
"""

#import necessary modules 
import os
import shutil 

#path to the folder to organize 
directory_path = ""

#list of files in the directory 
files = os.listdir(directory_path)

#set an extension map to categorize files based on their extensions. 
extension_map = {
    ".docx": "documents",
    ".pdf": "documents",
    ".txt": "documents",
    ".xlsx": "spreadsheets",
    ".jpg": "images",
    ".png": "images",
    ".jpeg": "images",
    ".py": "scripts",
    ".js": "scripts",
    ".json": "scripts",
    ".java": "scripts",
    ".html": "scripts",
    ".css": "scripts",
    ".drawio": "diagrams",
    ".mp4": "videos",
    ".avi": "videos",
    ".mkv": "videos",
    ".mov": "videos"
}

# to find the number of files in the folder 
print(f"Found {len(files)} files in the directory.")

# loop through the files and organize them based on their extensions 
for file in files: 
    fullpath = os.path.join(directory_path, file) # get the full path of the file
    if not os.path.isfile(fullpath): # check if its a file, if not, skip it 
        continue

    name, extension = os.path.splitext(file) # split the file naname and extension
    extension = extension.lower() # make the extensions lower case for consistency 
    category = extension_map.get(extension, "other") # get the category of the file based on the extension, if not found, add to other

    destination_path = os.path.join(directory_path, category) # create the destination folder path
    os.makedirs(destination_path, exist_ok=True) # create the destination folder if it doesnt exist

    try:
        shutil.move(fullpath, destination_path) # move the file to the destination folder
    except Exception as e:
        print(f"Error moving file {file}: {e}")
        
    print(f" {file} --> {destination_path}") # print the file and its new location
