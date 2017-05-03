import numpy, sys
from math import sqrt, pi, floor, log
from cmath import sin, cos, tan, cosh, sinh, phase, exp
from PIL import Image

# set constants
scale = 8
center = 0 + 0j
img_width = 500
img_height = 500
col = 40.6

# write julia array to pgm image
def save_img(data, fname):
        # generate an hsv image
        img = Image.new("HSV",(img_width,img_height))
        img.putdata(data)
        # convert to rgb and rotate
        img = img.convert("RGB")
        img = img.rotate(-90)
        # save image
        img.save(fname)

#define function to color
def func(z):
	return z

def color(z):
        z=func(z)
        h=int(40.6*(phase(z)+pi))
        s=int(50+50*log(1+2*abs(z)))
        v=200
        return (h,s,v)

# correct for image size
size_correct = sqrt((img_width/2)**2 + (img_height/2)**2)
# init pixel list
data = []

# iterate through matrix
for x in range(-img_width//2,img_height//2):
    for y in range(-img_width//2,img_width//2):
        z = (x+(y*1.0j))/size_correct
        z = scale*(z+center)
        # declare hue/coloring tuple
        px = color(z)
        # append to list        
        data.append(px)
    #print(x)
    
# send the array to file
save_img(data,"out/domain.png")
