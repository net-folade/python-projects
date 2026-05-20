"""
This script sorts photos based on their dates in a folder. 
"""

#import necessary modules 
import os 
import shutil 
from datetime import datetime 

# set a folder path and a variable to read the files
directory_path = ""
files = os.listdir(directory_path)

# build the loop to sort the files 
for file in files:
    fullpath = os.path.join(directory_path, file) # get the full path of the file

    if not os.path.isfile(fullpath): # check if its a file, if not, skip it
        continue

    name, extension = os.path.splitext(file) # split the file name and extension

    if name.startswith('.'): # skip hidden files
        continue 

    if extension.lower() not in ['.jpg', '.jpeg', '.png', '.gif', '.bmp']: # check if the file is an image, if not, skip it
        continue 


    timestamp = os.path.getmtime(fullpath) # get the last modified time of the file

    date = datetime.fromtimestamp(timestamp) # convert the timestamp to a date object  

    # extract the year, month, and day from the date object and format them as strings with leading zeros for month
    year = date.year
    month = f"{date.month:02d}"
    day = f"{date.day}"

    # make new directory name based on the date of the file
    destination_folder = os.path.join(directory_path, f"{year}", f"{month}") # set the destination folder path

    # create the new directory if it doesnt exist
    os.makedirs(destination_folder, exist_ok=True)


    try:
        shutil.move(fullpath, destination_folder) # move the file to the new directory
        print(f"Moved {file} to {destination_folder}") # print the file and its new location
    except Exception as e:
        print(f"Error moving file {file}: {e}")