import os
import shutil

# user input location of directory
path = str(input("enter path -> "))

# Check if path exists, if it does, store all file names in files variable
if os.path.exists(path):
    files = os.listdir(path)
else:
    print(f"{path} path doesn't exist")
    exit()  # Exit the script if the path doesn't exist

# Separate the filename and file extension
for file in files:
    fileName, fileExtension = os.path.splitext(file)
    fileExtension = fileExtension[1:].strip()

    # Assign a folder to a file without extension
    if fileExtension == "":
        fileExtension = "NoExtension"

    # Define source and destination paths
    source_path = os.path.join(path, file)
    destination_path = os.path.join(path, fileExtension, file)

    # Check if file exists at the destination
    if os.path.exists(destination_path):
        print(f"File {file} already exists in {fileExtension} folder.")
        continue

    # Create the directory if it doesn't exist
    if not os.path.exists(os.path.join(path, fileExtension)):
        os.mkdir(os.path.join(path, fileExtension))
        print(f"Directory {fileExtension} created.")

    # Move the file if the source and destination paths are different
    if source_path != destination_path:
        shutil.move(source_path, destination_path)
        print(f"Moved {file} to {fileExtension} folder")


# future development
# add delete all files
# develop in twkinter for better ui
