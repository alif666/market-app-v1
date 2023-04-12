# Python program to read
# json file
  

import os, json

path_to_json_files = 'posts/'
#get all JSON file names as a list
json_file_names = [filename for filename in os.listdir(path_to_json_files) if filename.endswith('.json')]

for json_file_name in json_file_names:
    with open(os.path.join(path_to_json_files, json_file_name)) as json_file:
        json_text = json.load(json_file)
        print(json_text["user_id"])
        print(json_text["user_url"])
        



