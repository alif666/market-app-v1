import os

# Set the directory path and filename
dir_path = "my_folder"
file_name = "my_file.txt"
file_path = os.path.join(dir_path, file_name)



def(dir_path,file_name,content):
    # Create the directory if it does not exist
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
        with open(filename, 'w') as f:
            json.dump(content, f, indent=4, sort_keys=True, default=str)

        print('make_dir File Write Done!!!')


        
    
    

