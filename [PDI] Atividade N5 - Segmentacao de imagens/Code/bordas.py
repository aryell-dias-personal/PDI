import numpy as np

import filters
from utils import Normalizar

def Derivative(imagem, tipo, filtro, m=5, n=5):
    if tipo == 'Prewitt':
        kernelx = [[-1,-1,-1],[0,0,0],[1,1,1]]
        kernely = [[-1,0,1],[-1,0,1],[-1,0,1]]    
        # kernelx = [[0,1,1],[-1,0,1],[-1,-1,0]]
        # kernely = [[-1,-1,0],[-1,0,1],[0,1,1]]
    elif tipo == 'Sobel':
        kernelx = [[-1,-2,-1],[0,0,0],[1,2,1]]
        kernely = [[-1,0,1],[-2,0,2],[-1,0,1]]    
        # kernelx = [[0,1,2],[-1,0,1],[-2,-1,0]]
        # kernely = [[-2,-1,0],[-1,0,1],[0,1,2]]

    if filtro == 'Average':
        imagemfil = filters.Average(imagem,m,n)
    elif filtro == 'Median':
        imagemfil = filters.Median(imagem,m,n)
        # imagemfil = Median(imagemfil,5,5)
        # imagemfil = Median(imagemfil,5,5)
    elif filtro == 'Adaptative':
        imagemfil = filters.Adaptative(imagem,m)
    elif filtro == 'Adapted':
        imagemfil = filters.Adapted(imagem,m,n)
        # imagemfil = filters.Median(imagemfil,m,n)

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
    
    # edgeImg = imagemfil - edgeImg

    edgeImg = Normalizar(edgeImg)

    return edgeImg