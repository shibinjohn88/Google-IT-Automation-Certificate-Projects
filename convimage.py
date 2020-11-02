

"""Convert TIFF Images to JPEG, resize and rorate image
   Written by Shibin John for Google IT Automation Certificate Program
"""

#!/usr/bin/env python3
from PIL import Image
import os
in_directory = r"/home/student-02-e6ae0def6e97/images"
out_directory = r"/opt/icons"
filelist = []
#iterate through source folder and append file names to a list
for filename in os.listdir(in_directory):
    filelist.append(filename)

#Iterate through file names in the list to scale and convert image to JPEG
for file in filelist:
    if file != ".DS_Store":
     with Image.open(in_directory+"/"+file) as im:
        im = im.resize((128, 128))
        im = im.rotate(90)
        if im.mode != 'RGB':
         im = im.convert('RGB')
        im.save(out_directory+"/"+os.path.splitext(file)[0]+".jpeg")
