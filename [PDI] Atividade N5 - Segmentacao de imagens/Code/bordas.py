import numpy as np
import scipy as spy

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
    elif filtro == 'Gaussian':
        imagemfil = filters.Gaussian(imagem)

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
    
    edgeImg = imagemfil - edgeImg

    # edgeImg = np.abs(edgeImg - np.max(edgeImg)) 

    edgeImg = Normalizar(edgeImg)

    return edgeImg

def Canny(imagem, T_min, T_max):
    aux = np.shape(imagem)

    if np.size(aux) > 2:
        imagem = imagem[:][:][1]
        aux = np.shape(imagem)
    
    kernelx = [[-1,-2,-1],[0,0,0],[1,2,1]]
    kernely = [[-1,0,1],[-2,0,2],[-1,0,1]]

    magImg = np.zeros(aux)
    phaseImg = np.zeros(aux)
    ImgFiltrada = np.zeros(aux)

    for x in range(aux[0]):
        for y in range(aux[1]):
            for u in range(-1,1):
                for v in range(-1,1):
                    if (x+u >= 0) and (x+u < aux[0]) and (y+v >= 0) and (y+v < aux[1]):
                        magImg[x][y] += np.abs(imagem[x+u][y+v]*kernelx[u+2][v+2]) + np.abs(imagem[x+u][y+v]*kernely[u+2][v+2])
                        phaseImg[x][y] += np.arctan(imagem[x+u][y+v]*kernely[u+2][v+2]/imagem[x+u][y+v]*kernelx[u+2][v+2])
    
    for x in range(aux[0]):
        for y in range(aux[1]):
            if phaseImg[x][y] >= -23 and phaseImg[x][y] < 23: 
                if magImg[x][y] < magImg[x][y-1] or magImg[x][y] < magImg[x][y+1]:
                    ImgFiltrada[x][y] = 0
                else:
                    ImgFiltrada[x][y] = magImg[x][y]
            elif phaseImg[x][y] >= 23 and phaseImg[x][y] < 67:
                if magImg[x][y] < magImg[x-1][y+1] or magImg[x][y] < magImg[x+1][y-1]:
                    ImgFiltrada[x][y] = 0
                else:
                    ImgFiltrada[x][y] = magImg[x][y] 
            elif (phaseImg[x][y] >= 67 and phaseImg[x][y] <= 90) or (phaseImg[x][y] >= -89 and phaseImg[x][y] < -67):
                if magImg[x][y] < magImg[x-1][y] or magImg[x][y] < magImg[x+1][y]:
                    ImgFiltrada[x][y] = 0
                else:
                    ImgFiltrada[x][y] = magImg[x][y]
            elif phaseImg[x][y] >= -67 and phaseImg[x][y] < -23:
                if magImg[x][y] < magImg[x-1][y-1] or magImg[x][y] < magImg[x+1][y+1]:
                    ImgFiltrada[x][y] = 0
                else:
                    ImgFiltrada[x][y] = magImg[x][y]

    ImgThrHigh = np.zeros(aux)
    ImgThrLow = np.zeros(aux)
    
    for x in range(aux[0]):
        for y in range(aux[1]):
            if imagem[x][y] >= T_max:
                ImgThrHigh[x][y] = 1
                ImgThrLow[x][y] = 1
            elif imagem[x][y] >= T_min and imagem[x][y] < T_max:
                ImgThrLow[x][y] = 1
                ImgThrHigh[x][y] = 0
            else:
                ImgThrLow[x][y] = 0
                ImgThrHigh[x][y] = 0

    ImgFiltrada = ImgThrHigh

    for x in range(aux[0]):
        for y in range(aux[1]):
            if ImgThrHigh[x][y] > 0:
                for u in range(9):
                    if ImgThrLow[x+u%9-1][y+u%9-1] > 0 and ImgThrHigh[x+u%9-1][y+u%9-1] == 0:
                        ImgFiltrada[x+u%9-1][y+u%9-1] = ImgThrLow[x+u%9-1][y+u%9-1]

    return ImgFiltrada