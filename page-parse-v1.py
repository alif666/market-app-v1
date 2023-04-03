import time
import csv
import json
from facebook_scraper import *

results = []
start_url = None
def handle_pagination_url(url):
    global start_url
    start_url = url
    if results:
        print(f"{len(results)}: {results[-1]['time']}: {start_url}")
set_cookies("cookies.txt")
while True:
    try:
        for post in get_posts("537554109685212", page_limit=None, start_url=start_url, request_url_callback=handle_pagination_url, options={
            "allow_extra_requests": False,
            "posts_per_page": 10
        }):
            #results.append(post)
            print(type(post))
            print(post)

            #dict to json parse
            json_post = json.dumps(post, indent=4, sort_keys=True, default=str)
            print(type(json_post))

            #create individual file for each json and write
            filename = "data/"+post['post_id']+".json"
            with open(filename, 'w') as f:
                json.dump(post, f,indent=4, sort_keys=True, default=str)
            
            print(post['post_id'])
        print("All done")
        #print(type(result))
        #print(results)
        # open the file in the write mode
        break
    except exceptions.TemporarilyBanned:
        print("Temporarily banned, sleeping for 10m")
        time.sleep(600)
