import time
import csv
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
            "posts_per_page": 10000
        }):
            results.append(post)
            print(type(post))

            
            print(post['post_id'])
        print("All done")
        #print(results)
        # open the file in the write mode
        f = open('foodbankbd.txt', 'w')

        # create the csv writer
        writer = csv.writer(f)

        # write a row to the csv file
        writer.writerow(results)




        break
    except exceptions.TemporarilyBanned:
        print("Temporarily banned, sleeping for 10m")
        time.sleep(600)
