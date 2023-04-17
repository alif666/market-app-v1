import time
import csv
import json
from facebook_scraper import *
from facebook_scraper import get_group_info
import os


import write_file_v1 as wf
import page_detail_parse as pdp
import json_to_db as jtd
#remote import        

#Method to parse facebook Group Posts
def get_post_id(post_id, loc, limit):
    loc = post_id+"_"+loc
    results = []
    start_url = None
    def handle_pagination_url(url):
        global start_url
        start_url = url
        if results:
            print(f"{len(results)}: {results[-1]['time']}: {start_url}")
    set_cookies("cookies.txt")
    #Issue : Dynamic page info add
    while True:
        try:
            for post in get_posts(post_id, page_limit=None, start_url=start_url, request_url_callback=handle_pagination_url, options={
                "allow_extra_requests": False,
                "posts_per_page": limit
            }):
                #results.append(post)
                print(type(post))
                #Issue : Try catch exception handling
                #Issue : Make this dynamic to call from other file
                #profile detail page import
                #create individual file for each json and write
                wf.write_file(loc,post['post_id'],post)
                print(post['post_id'])
            print("All done")
            #print(type(result))
            #print(results)
            # open the file in the write mode
            break
        except exceptions.TemporarilyBanned:
            print("Temporarily banned, sleeping for 10m")
            time.sleep(600)
#537554109685212
#2152489894978055

#Give the page ID
#groupDict = get_group_info("foodbankbd") 
#pageId = groupDict['id']
pageId = "653547362293676"
get_post_id("653547362293676", "posts", 10000)
pdp.get_list_of_post_id_details("653547362293676"+"_posts")
#jtd.json_to_db(pageId+"_posts")


