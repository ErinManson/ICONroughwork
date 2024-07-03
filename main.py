import json
import sql
import pdfConvertercopy
import shutil
import os

def separate_urls(input_list):
    postings = []
    for item in input_list:
        # Decode the JSON string to get the list of URLs
        urls = json.loads(item)
        postings.append(urls)
    return postings


# Input
input_data = sql.sql_main()
# Separate URLs
postings = separate_urls(input_data)


#test with valid pdf by adding a valid url to one post
if isinstance(postings[1], list):
    new_post = postings[1]
else:
    new_post = []
new_post.append("https://canadabuys.canada.ca/sites/default/files/webform/tender_notice/7467/rfp---english.pdf")
postings[1] = new_post



#loop through posts
j=0
for post in postings:
    j+=1
    i=0
    #loop through urls scanning each until we get a hit for a chair builder page in a text format for now
    found_builder = "No"
    #while we havent found builder pages or we have reached a stopping point
    while found_builder == "No" and found_builder != "Stop":
        for url in post:
            i+=1
            pdfConvertercopy.main(url)
            #after converting we read the final text file and see if it contains more than 20 lines of useful info
            with open("temp.txt", 'r') as fp:
                lines = len(fp.readlines())
                if lines >= 20:
                    found_builder = "Yes"
                    postname = "post" +str(j) + "url" + str(i) + "builder.txt"
                    shutil.copyfile("temp.txt", postname)
                #os.remove("temp.txt")



#if we loop through all urls set to stop
        if found_builder == "No":
            found_builder = "Stop"
        if found_builder == "Stop":
            print("No chair builder page found for this post!")
        else:
            print("Chair builder page found see .txt file")
        i+=1




