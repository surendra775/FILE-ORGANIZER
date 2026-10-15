import os
import shutil
folder_path = 'file-organizer'
files = os.listdir(folder_path)
print(files)
os.makedirs(os.path.join(folder_path, "Images"), exist_ok=True)
os.makedirs(os.path.join(folder_path, "Documents"), exist_ok=True)
for file in files:
    if file.endswith('.jpg') or file.endswith('.png'):
        source_path = os.path.join(folder_path, file)
        destination_path = os.path.join(folder_path, 'Images')
        shutil.move(source_path, destination_path)
    elif file.endswith('.txt') or file.endswith('.pdf'):
        source_path1 = os.path.join(folder_path, file)
        destination_path1 = os.path.join(folder_path, 'Documents')
        shutil.move(source_path1, destination_path1)
