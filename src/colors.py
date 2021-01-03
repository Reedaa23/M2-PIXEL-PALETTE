# -*- coding: utf-8 -*-
import numpy as np

def noDominantColor(randomColors_list, cubeRoot):
    
    uniformlyDistributedRGB=np.linspace(0.1,255,cubeRoot)
    
    for red in uniformlyDistributedRGB:
        for green in uniformlyDistributedRGB:
            for blue in uniformlyDistributedRGB:
                randomColors_list.append([red, green, blue])
        
    return randomColors_list

def redDominantColor(randomColors_list,squareRoot):
    
    uniformlyDistributedRGB=np.linspace(0.1,255,squareRoot)
    
    for green in uniformlyDistributedRGB:
        for blue in uniformlyDistributedRGB:
            randomColors_list.append([255, green, blue])
            
    return randomColors_list

def greenDominantColor(randomColors_list, squareRoot):
    
    uniformlyDistributedRGB=np.linspace(0.1,255,squareRoot)
    
    for red in uniformlyDistributedRGB:
        for blue in uniformlyDistributedRGB:
            randomColors_list.append([red, 255, blue])
            
    return randomColors_list

def blueDominantColor(randomColors_list, squareRoot):
    
    uniformlyDistributedRGB=np.linspace(0.1,255,squareRoot)
    
    for red in uniformlyDistributedRGB:
        for green in uniformlyDistributedRGB:
            randomColors_list.append([red, green, 255])
            
    return randomColors_list

def randomColorShades(imageSize, dominantColor):
    
    squareRoot=int(imageSize**(1/2)+1)
    cubeRoot=int(imageSize**(1/3)+1)
    randomColors_list=[]
    
    if(dominantColor=='red'):
        return redDominantColor(randomColors_list, squareRoot)
    elif(dominantColor=='green'):
        return greenDominantColor(randomColors_list, squareRoot)
    elif(dominantColor=='blue'):
        return blueDominantColor(randomColors_list, squareRoot)
    
    return noDominantColor(randomColors_list, cubeRoot)