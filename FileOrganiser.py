import os
import shutil

# Set the directory you want to organize
source_folder = r"C:\Users\YourUsername\Downloads"  # <-- Change this to your path

# Define the target folders and file types
file_types = {
    "Images": [".png", ".jpg", ".jpeg", ".gif"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Documents": [".docx", ".doc", ".txt", ".pptx", ".xlsx"],
    "PDFs": [".pdf"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar", ".7z"],
    "Code": [".py", ".js", ".html", ".css", ".java", ".cpp"],
    "Others": []
}

def organize_files():
    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        file_ext = os.path.splitext(filename)[1].lower()
        moved = False

        for folder_name, extensions in file_types.items():
            if file_ext in extensions:
                target_folder = os.path.join(source_folder, folder_name)
                os.makedirs(target_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(target_folder, filename))
                print(f"📁 Moved: {filename} → {folder_name}")
                moved = True
                break

        # Move to 'Others' if no match
        if not moved:
            other_folder = os.path.join(source_folder, "Others")
            os.makedirs(other_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(other_folder, filename))
            print(f"📦 Moved: {filename} → Others")

if __name__ == "__main__":
    organize_files()
    print("\n✅ Done organizing!")
