from PIL import Image
'''
image = Image.open('/assets/python.png')
data = list(image.getdata())
print(data)
'''

from urllib.request import urlopen
import io
response = urlopen("https://i.pinimg.com/originals/48/93/49/48934956251c1690b5e93ea710b7095a.jpg")
im_file = io.BytesIO(response.read())
im = Image.open(im_file)
im = im.rotate(90)
im = im.resize((800, 600))
im.save('downloaded_image.jpg', 'JPEG')