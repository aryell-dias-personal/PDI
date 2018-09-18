import numpy as np

import filters
from utils import Normalizar

def Prewitt(imagem):
    # kernelx = [[-1,-1,-1],[0,0,0],[1,1,1]]
    # kernely = [[-1,0,1],[-1,0,1],[-1,0,1]]    
    kernelx = [[0,1,1],[-1,0,1],[-1,-1,0]]
    kernely = [[-1,-1,0],[-1,0,1],[0,1,1]]

    imagemfil = filters.Average(imagem,7,7)
    
    # imagemfil = Median(imagem,7,7)
    # imagemfil = Median(imagemfil,5,5)
    # imagemfil = Median(imagemfil,5,5)

    # imagemfil = Adaptative(imagem,7)

    # imagemfil = filters.Adapted(imagem,5,5)
    # imagemfil = filters.Median(imagemfil,7,7)

    imagemfil = imagem - imagemfil

    aux = np.shape(imagem)

    if np.size(aux) > 2:
        imagem = imagem[:][:][0]
        aux = np.shape(imagem)

    edgeImg = np.zeros(aux)

    for x in range(aux[0]):
        for y in range(aux[1]):
            for u in range(-1,1):
                for v in range(-1,1):
                    if (x+u >= 0) and (x+u < aux[0]) and (y+v >= 0) and (y+v < aux[1]):
                        edgeImg[x][y] += np.abs(imagemfil[x+u][y+v]*kernelx[u+2][v+2]) + np.abs(imagemfil[x+u][y+v]*kernely[u+2][v+2])
    
    edgeImg = Normalizar(edgeImg)

    edgeImg = imagemfil - edgeImg

    return edgeImg