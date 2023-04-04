import os
import json

'''
# Set the directory path and filename
dir_path = "my_folder"
filename = "my_file.txt"
file_path = os.path.join(dir_path, file_name)
'''


def write_file(dir_path,file_name,content):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    filename = dir_path+"/"+file_name+".json"
    with open(filename, 'w') as f:
        print(filename)
        print(content)
        print("############")
        print(f)
        json.dump(content, f,indent=4, sort_keys=True, default=str)
        print('write_file File Write Done!!!')


        
    
    

