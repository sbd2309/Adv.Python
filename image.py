import sys
import os
from PIL import Image, ImageFilter

# grab input through command line
image_folder = sys.argv[1]
destination = sys.argv[2]
#command to change directory
os.chdir('/Users/soumyabratadutta/PycharmProjects/Udemy_Code/ImagePlayground')
# create folder if it don't exits
if not os.path.exists(destination):
    os.makedirs(destination)

# for accessing all files inside image_folder
for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    # excluding .jpg from the file name
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{destination}{clean_name}.png', 'png')
