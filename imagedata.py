from PIL import Image
from PIL.ExifTags import TAGS
 
def get_exif(fn):
    ret = {}
    pic = Image.open(fn)
    info = pic._getexif()
    for tag, value in info.items():
        decoded = TAGS.get(tag)
        ret[decoded] = value
    return ret

<<<<<<< Updated upstream
# change the parameter to get_exif to refer to a file on your own machine
# it is simplest to put the image in the same folder as your code
tags = get_exif("/Users/lindam/Pictures/ethanwallace.JPG")

#print (type(tags))
#print (tags)
print ("gps: ", type(tags["GPSInfo"]))

#for key,value in tags.items():
#   print (key,value)
=======
tags = get_exif("IMG_0083.jpg")
>>>>>>> Stashed changes

for tag in tags:
    print (tag)

print (tags["GPSInfo"])

