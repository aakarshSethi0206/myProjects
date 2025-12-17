import os

folderPath = "/Users/aakarshsethi/Desktop/SomeDocuments" # Path of the folder
files = os.listdir(folderPath)
prefix = input("What should file prefix be? ")
dry_run = True

old_paths = []
new_paths = []

for filename in files:
    old_path = os.path.join(folderPath, filename)
    old_paths.append(old_path)

    if os.path.isfile(old_path):
        if not filename.startswith(prefix):
            name, ext = os.path.splitext(filename)

            new_name = f"{prefix}{name}{ext}"
            new_path = os.path.join(folderPath, new_name)
            new_paths.append(new_path)

            if dry_run:
                print(f"{filename} → {new_name}")

response = input("Are you sure to rename the files? Enter y to continue ")
if response == 'y':
    i = len(old_paths)
    while i > 0:
        os.rename(old_paths[i-1], new_paths[i-1]) # The renaming function
        print(new_paths[i-1])   
        i = i-1;           
else:
    print("Not renaming the files.")
    