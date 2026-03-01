import os
import shutil

# Folder to organize
source_folder = os.path.expanduser("~/Downloads")

# File type folders
folders = {
    "Images": [".png", ".jpg", ".jpeg", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mov"],
    "Music": [".mp3"],
    "Archives": [".zip", ".rar"]
}

for file in os.listdir(source_folder):
    file_path = os.path.join(source_folder, file)

    if os.path.isfile(file_path):
        for folder, extensions in folders.items():
            if file.lower().endswith(tuple(extensions)):
                target_folder = os.path.join(source_folder, folder)

                if not os.path.exists(target_folder):
                    os.makedirs(target_folder)

                shutil.move(file_path, os.path.join(target_folder, file))
                print(f"Moved {file} → {folder}")
