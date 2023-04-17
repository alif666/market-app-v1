# Python program to read
# json file
#Issue Make dynamic  
#Issue Add time
#Issue check if parsed before

import os, json
import connect as c


#Getting posts
def json_to_db(loc):
    loc= loc+'/'
    path_to_json_files = loc
    #get all JSON file names as a list
    json_file_names = [filename for filename in os.listdir(path_to_json_files) if filename.endswith('.json')]

    for json_file_name in json_file_names:
        with open(os.path.join(path_to_json_files, json_file_name)) as json_file:
            print("##################################")
            json_text = json.load(json_file)
            print("User ID :")
            customerId = json_text["user_id"]
            print(customerId)
            
            

            print("User Name:")
            print(json_text["username"])
            userName = json_text["username"]
            
            
            print("post type: POST")
            postType = "POST"
            print("Image URL: ")
            print(json_text["image_lowquality"])
            imageUrl = json_text["image_lowquality"]

            
            print("Post ID :")
            print(json_text["post_id"])
            postId = json_text["post_id"]

            print("Page ID: ")
            print(json_text["page_id"])
            pageId = json_text["page_id"]


            sql = "insert into customer(customer_id, customer_name, post_image_url, customer_post_type, post_or_comment_id, page_id) values (%s, %s, %s, %s, %s, %s)"  
            val = (customerId, userName, imageUrl, postType, postId, pageId)
                        
            conn = c.open_db_connection()
            cur = conn.cursor()
            try:

                cur.execute(sql,val)
                print(cur.execute(sql,val))
                #commit the transaction
                conn.commit()
                print("insertion successful")
            except Exception as e:
                print(e)
                print("insertion failed")
                conn.rollback()
                conn.close()

            print(cur.rowcount,"record inserted!")
            conn.close()
                
            


    #Getting comments

    path_to_json_files = loc+'comments/'
    #get all JSON file names as a list
    json_file_names = [filename for filename in os.listdir(path_to_json_files) if filename.endswith('.json')]

    for json_file_name in json_file_names:
        with open(os.path.join(path_to_json_files, json_file_name)) as json_file:
            print("##################################")
            json_text = json.load(json_file)
            print("User ID :")
            customerId = json_text["commenter_id"]
            print(customerId)
            
            

            print("User Name:")
            print(json_text["commenter_name"])
            userName = json_text["commenter_name"]
            
            
            print("post type: POST")
            postType = "COMMENT"
        

            
            print("Comment ID :")
            print(json_text["comment_id"])
            postId = json_text["comment_id"]



            sql = "insert into customer(customer_id, customer_name,  customer_post_type, post_or_comment_id) values (%s, %s, %s, %s)"  
            val = (customerId, userName,  postType, postId)
                        
            conn = c.open_db_connection()
            cur = conn.cursor()
            try:

                cur.execute(sql,val)
                print(cur.execute(sql,val))
                #commit the transaction
                conn.commit()
                print("insertion successful")
            except Exception as e:
                print(e)
                print("insertion failed")
                conn.rollback()
                conn.close()

            print(cur.rowcount,"record inserted!")
            conn.close()
                
            


    #Getting replies

    path_to_json_files = loc+'replies/'
    #get all JSON file names as a list
    json_file_names = [filename for filename in os.listdir(path_to_json_files) if filename.endswith('.json')]

    for json_file_name in json_file_names:
        with open(os.path.join(path_to_json_files, json_file_name)) as json_file:
            print("##################################")
            json_text = json.load(json_file)
            print("User ID :")
            customerId = json_text["commenter_id"]
            print(customerId)
            
            

            print("User Name:")
            print(json_text["commenter_name"])
            userName = json_text["commenter_name"]
            
            
            print("post type: POST")
            postType = "REPLY"
        

            
            print("Comment ID :")
            print(json_text["comment_id"])
            postId = json_text["comment_id"]



            sql = "insert into customer(customer_id, customer_name,  customer_post_type, post_or_comment_id) values (%s, %s, %s, %s)"  
            val = (customerId, userName,  postType, postId)
                        
            conn = c.open_db_connection()
            cur = conn.cursor()
            try:

                cur.execute(sql,val)
                print(cur.execute(sql,val))
                #commit the transaction
                conn.commit()
                print("insertion successful")
            except Exception as e:
                print(e)
                print("insertion failed")
                conn.rollback()
                conn.close()

            print(cur.rowcount,"record inserted!")
            conn.close()
            
            


json_to_db("653547362293676_posts/")
