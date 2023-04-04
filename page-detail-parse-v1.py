"""
Download comments for a public Facebook post.
"""
import json_file_v1 as jf
import facebook_scraper as fs
import write_file_v1 as wf

def get_posts_details_from_list_of_post_id(filenames, loc):
    for filename_str in filenames:
        # get POST_ID from the URL of the post which can have the following structure:
        # https://www.facebook.com/USER/posts/POST_ID
        # https://www.facebook.com/groups/GROUP_ID/posts/POST_ID
        POST_ID = filename_str
        # number of comments to download -- set this to True to download all comments
        MAX_COMMENTS = 500

        # get the post (this gives a generator)
        gen = fs.get_posts(
            post_urls=[POST_ID],
            options={"comments": MAX_COMMENTS, "progress": True}
        )

        # take 1st element of the generator which is the post we requested
        post = next(gen)

        # extract the comments part
        comments = post['comments_full']

        # process comments as you want...
        for comment in comments:

            # e.g. ...print them
            print(comment)
            print(type(comment))
            
            #write comments in file.
            #Issue dynamic variable name with mapper
            wf.write_file(loc+'comments',comment['comment_id']+'.json',comment)
            
            # e.g. ...get the replies for them
            for reply in comment['replies']:
                print(' ', reply)
                print(type(reply))
                #write replies in file
                #Issue dynamic variable name with mapper
                wf.write_file(loc+'comments/replies',comment['comment_id']+'.json',comment)

                
#First method to call
def get_list_of_post_id(loc):
    filenames=[]

    #get filenames list from json_file_v1
    filenames = jf.get_all_filenames_from_location(loc)
    print("page-detail-parse-v1 received the filenames :")

    #filenames is list so cannot concatenate with previous string
    print(filenames)
    get_posts_details_from_list_of_post_id(filenames, loc)

    
#This is the first method to call
#get_list_of_post_id('data/')
