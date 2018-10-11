import numpy as np 
import os
import matplotlib.pyplot as plt 

def LZWdescompress(dictionary, comp, originalShape):
    x, y = originalShape
    imagemDesformatada = []
    for x in comp:
        if(isinstance(dictionary[x],int)):
            imagemDesformatada += [dictionary[x]]
        else:
            imagemDesformatada += dictionary[x]
    print(imagemDesformatada)    
    imagemRetorno = []
    counter = 0
    for i in range(x):
        for j in range(y):
            counter += j
            imagemRetorno[i][j] = imagemDesformatada[counter]
    return imagemRetorno