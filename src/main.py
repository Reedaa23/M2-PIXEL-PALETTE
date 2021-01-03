# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from image import createImage
from colors import randomColorShades
from fill import fillImage
from fill import fillImageFirstIteration
from fill import fillImageMiddleIterations
from fill import deleteFromBoundary

width=100
height=100
imageSize=width*height
image=createImage(width,height)
dominantColor=None
#dominantColor='red'
#dominantColor='green'
#dominantColor='blue'
randomColorShades_list=randomColorShades(imageSize, dominantColor)
initialColorShadesLength=len(randomColorShades_list)
boundaryPixels_dict={}

fillImage=fillImage(dominantColor, width, height, randomColorShades_list, imageSize, image, initialColorShadesLength, boundaryPixels_dict)
imagePlot=plt.imshow(fillImage, origin='lower')
plt.show()


'''
width=40
height=40
imageSize=width*height
image=createImage(width,height)
dominantColor=None
#dominantColor='red'
#dominantColor='green'
#dominantColor='blue'
randomColorShades_list=randomColorShades(imageSize, dominantColor)
initialColorShadesLength=len(randomColorShades_list)
boundaryPixels_dict={}
fillImageFirstIteration(dominantColor, width, height, randomColorShades_list, image, boundaryPixels_dict)

def fillAnimatedImage(*args):
    
    if(len(randomColorShades_list)>initialColorShadesLength-imageSize):
        
        newPixel=fillImageMiddleIterations(dominantColor, width, height, randomColorShades_list, image, boundaryPixels_dict)
        pixelPositionToFill=newPixel[0]
        randomColor=newPixel[1]
        
        deleteFromBoundary(pixelPositionToFill, width, height, image, boundaryPixels_dict)
        randomColorShades_list.remove(randomColor)
        
        imagePlot.set_array(image)
        
        return imagePlot,

fig = plt.figure()
imagePlot=plt.imshow(image, origin='lower', animated=True)
animation = animation.FuncAnimation(fig, fillAnimatedImage, interval=0, blit=True)
plt.show()'''