"""
This script renames files in a filder 
"""

# import os to interact with the operating system 
import os 

#set a folder path and a variable to read the files
folder_path = ""
files = os.listdir(folder_path)

#set a base name to use in renaming the files 
base_name = "Test"

# set a counter for the loop
counter = 1

# loop through the folder an rename the files 
for file in files: 
    fullpath = os.path.join(folder_path, file)                  # get the fullpath ~ directory + file

    if not os.path.isfile(fullpath):                    # check if it's a file, if not, skip it 
        continue 

    name, extension = os.path.splitext(file)        # extract the name and extension 
    extension = extension.lower()                   # make extension lower case for consistency 

    if name.startswith('.'):                         # skip hidden files 
        continue 

    new_name = f"{base_name}_{counter:03d}{extension}"         # set the new name format

    new_path = os.path.join(folder_path, new_name)          # set the new destination path 

    # set a try/exception block for unexpected actions 
    try:
        counter +=1                             # set counter increment 
        os.rename(fullpath, new_path)           # rename the file to the new name || pass the source and destination to function to rename the file.
    except Exception as e:
        (f"Unable to rename {file}: {e}")

    print(f"Renamed {file} -> {new_name}")



    


