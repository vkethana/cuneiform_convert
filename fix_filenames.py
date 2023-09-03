from PIL import Image
import imagehash
import json
import os
import requests
import shutil
import urllib.parse

def are_images_same(image_path1, image_path2):
    # Load the images
    try:
      img1 = Image.open(image_path1)
      img2 = Image.open(image_path2)
      '''
      # Compute hash values for the images
      hash1 = imagehash.average_hash(img1)
      hash2 = imagehash.average_hash(img2)
      '''
      # Compare the hash values to determine if the images are the same
      #return hash1 == hash2
      return img1 == img2
    except:
      print("ERROR:", image_path1, " or ", image_path2, " may be a broken file")
      return 0

def get_q_code(url):
  q_index = url.find('Q')
  if q_index != -1:
    # Extract everything after 'Q'
    result = url[q_index + 1:]  # Add 2 to skip 'Q='
    return result
'''
# Specify the paths of the two image files you want to compare
image_path1 = "png/1.png"
image_path2 = "png/1.png"

# Check if the images are the same
if are_images_same(image_path1, image_path2):
    print("The two images are the same.")
else:
    print("The two images are different.")
'''


#
'''
f = open("query.json")
data = json.load(f)

for item in data:
  url = item["image"]
  print(url)
  img_data = requests.get(url).content
  with open("png_with_qcode/" + get_q_code(item['form']) + ".png", 'wb') as handler:
    handler.write(img_data)
'''

matching_img_dict = {}

dir1 = "png"
dir2 = "png_with_qcode"

for file1 in os.listdir(dir1):
  for file2 in os.listdir(dir2):
    path1 = os.path.join(dir1, file1)
    path2 = os.path.join(dir2, file2)
    #print(path1,path2)
    if are_images_same(path1, path2):
      matching_img_dict[file1] = file2
      shutil.copy2(("svg/"+ os.path.splitext(file1)[0] + ".svg"), ("svg_with_qcode/"+ os.path.splitext(file2)[0] + "_" + (os.path.splitext(file1)[0]) + ".svg") )

print(matching_img_dict)
