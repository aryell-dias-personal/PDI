import numpy as np 
import os
import matplotlib.pyplot as plt 

def LZWdescompress(dictionary, comp, originalShape):
    x, y = originalShape
    imagemDesformatada = []
    for i in comp:
        if(isinstance(dictionary[i],int)):
            imagemDesformatada += [dictionary[i]]
        else:
            imagemDesformatada += dictionary[i]
    imagemDesformatada += [dictionary[i][-1]]
    imagemRetorno = [[i*j for i in range(x)]for j in range(y)]
    counter = 0
    for i in range(x):
        for j in range(y):
            # print(imagemDesformatada[counter])
            imagemRetorno[i][j] = imagemDesformatada[counter]
            counter += 1
    return imagemRetorno