from settings import IMAGES_STORE as folder_path, base_dir as base_dir
import os
print(folder_path)
file_path = folder_path+'/'+base_dir.split('/')[-2]
print(file_path)
