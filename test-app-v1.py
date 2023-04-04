import os

#Make this a module
def get_all_filenames_from_location(folder_path):
    #initialize returning list
    filenames = []
    
    #Get a list of all  files in the folder
    files = os.listdir(folder_path)
    
    #Print the file names
    for file in files:
        filename, extension = os.path.splitext(file)
        filenames.append(filename)

    return filenames


# Define the folder path
folder_path = 'data/'    
print(get_all_filenames_from_location(folder_path))
    
