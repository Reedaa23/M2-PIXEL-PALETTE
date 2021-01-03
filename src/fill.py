# -*- coding: utf-8 -*-
import numpy as np
import random
from image import getPixel
from image import getMiddlePointPosition
random.seed(123)

def pixelEuclideanDistanceToPixels(pixel, pixels):
    
    pixel_list=[pixel]
    pixel_array=np.array(pixel_list)
    pixels_array=np.array(pixels)
    difference=pixel_array-pixels_array
    
    return np.linalg.norm(difference,axis=1)
        
def minimalPixelsEuclideanDistancePosition(pixel, pixels_dict):
    
    pixels_dict_values_list=list(pixels_dict.values())
    pixels_dict_keys_list=list(pixels_dict.keys())
    euclideanDistance=pixelEuclideanDistanceToPixels(pixel, pixels_dict_values_list)
    distance_dict= dict(zip(pixels_dict_keys_list, euclideanDistance))
    
    return min(distance_dict, key=distance_dict.get)

def addLeftFreeAdjacentPixel(adjacentPixels_dict, position_X, position_Y, width, height, image):
    
    if(position_X-1<width and position_X>=1 and position_Y<height and position_Y>=0 and getPixel(image,position_X-1, position_Y)==[0,0,0]):
        adjacentPixels_dict[(position_X-1,position_Y)]=[0,0,0]

def addRightFreeAdjacentPixel(adjacentPixels_dict, position_X, position_Y, width, height, image):
    
    if(position_X+1<width and position_X>=0 and position_Y<height and position_Y>=0 and getPixel(image,position_X+1, position_Y)==[0,0,0]):
        adjacentPixels_dict[(position_X+1,position_Y)]=[0,0,0]

def addBottomFreeAdjacentPixel(adjacentPixels_dict, position_X, position_Y, width, height, image):
    
    if(position_X<width and position_X>=0 and position_Y-1<height and position_Y>=1 and getPixel(image,position_X, position_Y-1)==[0,0,0]):
        adjacentPixels_dict[(position_X,position_Y-1)]=[0,0,0]

def addTopFreeAdjacentPixel(adjacentPixels_dict, position_X, position_Y, width, height, image):
    
    if(position_X<width and position_X>=0 and position_Y+1<height and position_Y>=0 and getPixel(image,position_X, position_Y+1)==[0,0,0]):
        adjacentPixels_dict[(position_X,position_Y+1)]=[0,0,0]

def freeToFillAdjacentPixels(image, position_X, position_Y, width, height):
    
    adjacentPixels_dict={}
    
    addLeftFreeAdjacentPixel(adjacentPixels_dict, position_X, position_Y, width, height, image)
    addRightFreeAdjacentPixel(adjacentPixels_dict, position_X, position_Y, width, height, image)
    addBottomFreeAdjacentPixel(adjacentPixels_dict, position_X, position_Y, width, height, image)
    addTopFreeAdjacentPixel(adjacentPixels_dict, position_X, position_Y, width, height, image)
    
    return adjacentPixels_dict

def fillByPosition(image, position_X, position_Y, pixel):
    
    image[position_Y][position_X]=pixel
    
def fillImageFirstIteration(dominantColor, width, height, randomColorShades_list, image, boundaryPixels_dict):
    
    randomColor=random.choice(randomColorShades_list)
    middlePointPosition=getMiddlePointPosition(width, height)
    pixelPositionsToFill=freeToFillAdjacentPixels(image, middlePointPosition[0], middlePointPosition[1], width, height).keys()
    pixelPositionToFill=random.choice(list(pixelPositionsToFill))
    fillByPosition(image, pixelPositionToFill[0], pixelPositionToFill[1], randomColor)
    boundaryPixels_dict[pixelPositionToFill]=randomColor
    randomColorShades_list.remove(randomColor)

def addToBoundaryPixels(pixelPositionToFill,randomColor, width, height, image, boundaryPixels_dict):
    
    freeToFillAdjacentPixels_dict=freeToFillAdjacentPixels(image, pixelPositionToFill[0], pixelPositionToFill[1], width, height)
    if(list(freeToFillAdjacentPixels_dict.keys())!=[]):
        boundaryPixels_dict[pixelPositionToFill]=randomColor
    
def fillImageMiddleIterations(dominantColor, width, height, randomColorShades_list, image, boundaryPixels_dict):
    
    randomColor=random.choice(randomColorShades_list)
    minimalDistanceFilledPixelPosition=minimalPixelsEuclideanDistancePosition(randomColor, boundaryPixels_dict)
    pixelPositionsToFill=freeToFillAdjacentPixels(image, minimalDistanceFilledPixelPosition[0], minimalDistanceFilledPixelPosition[1], width, height).keys()
    pixelPositionToFill=random.choice(list(pixelPositionsToFill))
    fillByPosition(image, pixelPositionToFill[0], pixelPositionToFill[1], randomColor)
    
    addToBoundaryPixels(pixelPositionToFill,randomColor, width, height, image, boundaryPixels_dict)
    
    return [pixelPositionToFill, randomColor]
    
def deleteLeftBoundaryPixels(pixelPositionToFill, width, height, image, boundaryPixels_dict):
    
    freeToFillAdjacentPixels_dict=freeToFillAdjacentPixels(image, pixelPositionToFill[0]-1, pixelPositionToFill[1], width, height)
    if(list(freeToFillAdjacentPixels_dict.keys())==[] and (pixelPositionToFill[0]-1, pixelPositionToFill[1]) in boundaryPixels_dict.keys()):
        del boundaryPixels_dict[(pixelPositionToFill[0]-1, pixelPositionToFill[1])]

def deleteRightBoundaryPixels(pixelPositionToFill, width, height, image, boundaryPixels_dict):
    
    freeToFillAdjacentPixels_dict=freeToFillAdjacentPixels(image, pixelPositionToFill[0]+1, pixelPositionToFill[1], width, height)
    if(list(freeToFillAdjacentPixels_dict.keys())==[] and (pixelPositionToFill[0]+1, pixelPositionToFill[1]) in boundaryPixels_dict.keys()):
        del boundaryPixels_dict[(pixelPositionToFill[0]+1, pixelPositionToFill[1])]
    
def deleteBottomBoundaryPixels(pixelPositionToFill, width, height, image, boundaryPixels_dict):
    
    freeToFillAdjacentPixels_dict=freeToFillAdjacentPixels(image, pixelPositionToFill[0], pixelPositionToFill[1]-1, width, height)
    if(list(freeToFillAdjacentPixels_dict.keys())==[] and (pixelPositionToFill[0], pixelPositionToFill[1]-1) in boundaryPixels_dict.keys()):
        del boundaryPixels_dict[(pixelPositionToFill[0], pixelPositionToFill[1]-1)]
            
def deleteTopBoundaryPixels(pixelPositionToFill, width, height, image, boundaryPixels_dict):
    
    freeToFillAdjacentPixels_dict=freeToFillAdjacentPixels(image, pixelPositionToFill[0], pixelPositionToFill[1]+1, width, height)
    if(list(freeToFillAdjacentPixels_dict.keys())==[] and (pixelPositionToFill[0], pixelPositionToFill[1]+1) in boundaryPixels_dict.keys()):
        del boundaryPixels_dict[(pixelPositionToFill[0], pixelPositionToFill[1]+1)]
        
def deleteFromBoundary(pixelPositionToFill, width, height, image, boundaryPixels_dict):
    
    deleteLeftBoundaryPixels(pixelPositionToFill, width, height, image, boundaryPixels_dict)
    deleteRightBoundaryPixels(pixelPositionToFill, width, height, image, boundaryPixels_dict)
    deleteBottomBoundaryPixels(pixelPositionToFill, width, height, image, boundaryPixels_dict)
    deleteTopBoundaryPixels(pixelPositionToFill, width, height, image, boundaryPixels_dict)
            
def fillImage(dominantColor, width, height, randomColorShades_list, imageSize, image, initialColorShadesLength, boundaryPixels_dict):

    fillImageFirstIteration(dominantColor, width, height, randomColorShades_list, image, boundaryPixels_dict)
    
    while(len(randomColorShades_list)>initialColorShadesLength-imageSize):
        
        newPixel=fillImageMiddleIterations(dominantColor, width, height, randomColorShades_list, image, boundaryPixels_dict)
        pixelPositionToFill=newPixel[0]
        randomColor=newPixel[1]
        deleteFromBoundary(pixelPositionToFill, width, height, image, boundaryPixels_dict)
        randomColorShades_list.remove(randomColor)
    
    return image