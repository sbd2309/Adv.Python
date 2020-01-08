from PIL import Image, ImageFilter


img=Image.open('./Img/pika.jpg')
#print different aspects of the image
print (img.format,img.size,img.mode)

#adding filter and adding it new file
filtered_image=img.filter(ImageFilter.BLUR)#SMOOTH or SHARPEN

#saving the filtered file
filtered_image.save("pika_filter.png",'png')

#coverting image to greyscale like filters
filtered_image=img.convert('L')#greyscale is L
filtered_image.save("greyscale.png",'png')

#for displaying the image
filtered_image.show()

#rotating images by 90
rotated_image=filtered_image.rotate(90)
rotated_image.save('rotate.png','png')
rotated_image.show() 

#resize any image
#resize accepts tuple here
resize_image=filtered_image.resize((300,300))
resize_image.show()

#crop a picture
box=(100,100,400,400)
crop_image=filtered_image.crop(box)
crop_image.save('crop_image.png','png')
crop_image.show()
