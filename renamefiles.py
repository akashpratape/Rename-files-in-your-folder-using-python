import os
import re

folder_path = 'your folder path'

def rename_files(folder_path):

    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            match = re.match(r'(your file name) \((\d+)\)(\.[\w]+)$', filename)
            if match:
                base_name = match.group(1)
                number = match.group(2)
                extension = match.group(3)
                new_name = f'{base_name}{number}{extension}'
                old_path = os.path.join(folder_path, filename)
                new_path = os.path.join(folder_path, new_name)
                os.rename(old_path, new_path)
                print(f'Renamed: {filename} -> {new_name}')

rename_files(folder_path)
