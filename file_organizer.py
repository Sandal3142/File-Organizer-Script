import os
import shutil


target_folder = os.getcwd()


file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Documents': ['.pdf', '.docx', '.doc', '.txt', '.xlsx', '.pptx'],
    'Videos': ['.mp4', '.mkv', '.avi', '.mov'],
    'Music': ['.mp3', '.wav', '.aac'],
    'Archives': ['.zip', '.rar', '.tar', '.gz'],
    'Scripts': ['.py', '.js', '.sh', '.bat','cs', '.java', '.cpp', '.c','jsx'],
    'Others': []
}

def create_folder(name):
    folder_path = os.path.join(target_folder, name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    return folder_path

def get_category(extension):
    for category, extensions in file_types.items():
        if extension.lower() in extensions:
            return category
    return 'Others'

def organize_files():
    for filename in os.listdir(target_folder):
        file_path = os.path.join(target_folder, filename)
        
        
        if os.path.isdir(file_path) or filename == os.path.basename(__file__):
            continue

        _, ext = os.path.splitext(filename)
        category = get_category(ext)

        dest_folder = create_folder(category)
        dest_path = os.path.join(dest_folder, filename)

       
        shutil.move(file_path, dest_path)
        print(f"Moved: {filename} ➜ {category}/")

if __name__ == "__main__":
    organize_files()
    print("\n🎉 Files organized successfully!")
