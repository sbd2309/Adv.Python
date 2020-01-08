from PIL import Image , ImageFilter

img=Image.open('./Img/384132.jpg')
img2=img
#creation of thumbnail and keeping the aspect ratio same 
#thumbnail function returns nothing and hence the image v load the changes will be reflected there

img2.thumbnail((400,200))
img2.save('thumbnail.jpg')
img2.show()