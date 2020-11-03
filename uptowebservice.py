
#! /usr/bin/env python3
import os
import requests
source_folder = r"/data/feedback"
filelist = []
textdictionary = {}

#Append all files in the source folder to a list
for file in os.listdir(source_folder):
    filelist.append(file)

#Iterate through each file in the list create a dictionary and upload to the webservice using post
for filename in filelist:
    if filename != ".DS_Store":
        with open(source_folder+"/"+filename, "r") as tx:
            count = 0
            for line in tx.readlines():
                if count == 0:
                    textdictionary["title"] = line.strip("\n")
                elif count == 1:
                    textdictionary["name"] = line.strip("\n")
                elif count == 2:
                    textdictionary["date"] = line.strip("\n")
                else:
                    textdictionary["feedback"] = line.strip("\n")
                count += 1
            print(textdictionary)
            response = requests.post("http://34.121.116.234/feedback/", data=textdictionary)
            print(response.status_code)
            print(response.text)
            if response.status_code == 201:
             print("success")
