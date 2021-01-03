# -*- coding: utf-8 -*-
import numpy as np

WIDTH_MIN=500
HEIGHT_MIN=400

def createImage(width=WIDTH_MIN, height=HEIGHT_MIN):
    
    image = np.zeros((height,width,3),dtype=np.uint8)
    
    return image

def getPixel(image, position_X, position_Y):
    
    return list(image[position_Y][position_X])

def getMiddlePointPosition(width, height):
            
    return (int(width/2),int(height/2))