import PIL   # sudo apt install python3-pil


from PIL import Image
im = Image.open("bride.jpg")
im.rotate(45).show()

# help(PIL)

#For example, if we wanted to resize an image and save the new image with a new name, we could do it with:
from PIL import Image
im = Image.open("example.jpg")
new_im = im.resize((640,480))
new_im.save("example_resized.jpg")

#to rotate 

from PIL import Image
im = Image.open("example.jpg")
new_im = im.rotate(90)
new_im.save("example_rotated.jpg")


#to rotate resize

from PIL import Image
im = Image.open("example.jpg")
im.rotate(180).resize((640,480)).save("flipped_and_resized.jpg")
