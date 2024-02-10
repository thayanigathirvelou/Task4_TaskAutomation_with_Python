import os
import shutil

def organize_files(directory):
    # Define file types and corresponding folders
    file_types = {
        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "Documents": [".pdf", ".doc", ".docx", ".txt"],
        "Videos": [".mp4", ".avi", ".mkv"],
        "Others": []
    }

    # Create folders if they don't exist
    for folder in file_types.keys():
        folder_path = os.path.join(directory, folder)
        os.makedirs(folder_path, exist_ok=True)

    # Organize files into respective folders
    for filename in os.listdir(directory):
        if filename != "organize_files.py":  # Exclude the script file itself
            file_path = os.path.join(directory, filename)
            if os.path.isfile(file_path):
                file_type = None
                for category, extensions in file_types.items():
                    if any(filename.lower().endswith(ext) for ext in extensions):
                        file_type = category
                        break

                # Move the file to the corresponding folder
                if file_type:
                    destination_folder = os.path.join(directory, file_type)
                    shutil.move(file_path, os.path.join(destination_folder, filename))
                else:
                    # Move to the "Others" folder if the file type is not recognized
                    shutil.move(file_path, os.path.join(directory, "Others", filename))

if __name__ == "__main__":
    directory_to_organize = "."  # Change this to the path of the directory you want to organize
    organize_files(directory_to_organize)
    print("Files organized successfully.")
