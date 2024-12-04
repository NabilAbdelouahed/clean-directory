import shutil, os


dir_path = "C:/Users/nabil/Downloads"

mapping = {"Photos" : {"jpeg", "png", "webp", "jpg" }, 
           "Docs" : {"pdf", "docx", "xlsx", "csv", "pptx", "txt"},
           "Music" : {"mp3", "wav"},
           "Video" : {"mp4", "mov"}
           }


# Invert the mapping to extension: folder
ext_to_folder = {}
for folder, extensions in mapping.items():
    for ext in extensions:
        ext_to_folder[ext] = folder

# Prepare directories beforehand
for folder in mapping.keys():
    os.makedirs(os.path.join(dir_path, folder), exist_ok=True)

# List all files
files = [f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path , f))]

for file in files : 
    # Get the file extension
    _, extension = os.path.splitext(file)
    extension = extension[1:].lower() 

    #If the extension is taken into account in mapping
    if extension in ext_to_folder : 

        # Get the right folder
        folder = ext_to_folder[extension]

        # Move the file
        shutil.move(f"{dir_path}/{file}", f"{dir_path}/{folder}/{file}")

print("Files have been organized.")