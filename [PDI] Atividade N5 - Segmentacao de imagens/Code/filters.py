import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

def Average(imagem,m,n):
    aux = np.shape(imagem)

    if np.size(aux) > 2:
        imagem = imagem[:][:][0]
        aux = np.shape(imagem)
        
    filterImg = np.zeros(aux)
    kernel = np.zeros(m*n)

    media = 0

    for x in range(aux[0]):
        for y in range(aux[1]):
            for u in range(m*n):
                if (x+u%m-1 >= 0) and (x+u%m-1 < aux[0]) and (y+u%n-1 >= 0) and (y+u%n-1 < aux[1]):
                    media += imagem[x+u%m-1][y+u%n-1]
            filterImg[x][y] = media/(m*n)
            media = 0

    filterImg = imagem - filterImg

    return filterImg

def Median(imagem,m,n):
    aux = np.shape(imagem)

    if np.size(aux) > 2:
        imagem = imagem[:][:][0]
        aux = np.shape(imagem)
    
    filterImg = np.zeros(aux)
    kernel = np.zeros(m*n)

    for x in range(aux[0]):
        for y in range(aux[1]):
            for u in range(m*n):
                if (x+u%m-1 >= 0) and (x+u%m-1 < aux[0]) and (y+u%n-1 >= 0) and (y+u%n-1 < aux[1]):
                    kernel[u] = imagem[x+u%m-1][y+u%n-1]
            for v in range(m*n):
                for t in range(v,m*n):
                    if kernel[v] > kernel[t]:
                        auxi = kernel[t]
                        kernel[t] = kernel[v]
                        kernel[v] = auxi
            if (m*n)%2 > 0:
                filterImg[x][y] = kernel[int((m*n-1)/2)]
            else:
                filterImg[x][y] = (kernel[int(np.floor(m*n/2))]+kernel[int(np.ceil(m*n/2))])/2

    # filterImg = imagem - filterImg

    return filterImg

def Adaptative(imagem, M_max):
    aux = np.shape(imagem)

    if np.size(aux) > 2:
        imagem = imagem[:][:][1]
        aux = np.shape(aux)
    
    m = 3
    filterImg = np.zeros(aux)
    kernel = np.zeros(m*m)

    for x in range(aux[0]):
        for y in range(aux[1]):
            for u in range(m*m):
                if (x+u%m-1 >= 0) and (x+u%m-1 < aux[0]) and (y+u%m-1 >= 0) and (y+u%m-1 < aux[1]):
                    kernel[u] = imagem[x+u%m-1][y+u%m-1]
            for v in range(m*m):
                for t in range(v,m*m):
                    if kernel[v] > kernel[t]:
                        auxi = kernel[t]
                        kernel[t] = kernel[v]
                        kernel[v] = auxi
            mini = np.min(kernel)
            maxi = np.max(kernel)
            a = 1
            while a == 1: 
                if (m*m)%2 > 0:
                    med = kernel[int((m*m-1)/2)]
                else:
                    med = (kernel[int(np.floor(m*m/2))]+kernel[int(np.ceil(m*m/2))])/2
                A1 = med - mini
                A2 = med - maxi
                if A1 > 0 and A2 < 0:
                    B1 = imagem[x][y] - mini
                    B2 = imagem[x][y] - maxi
                    if B1 > 0 and B2 < 0:
                        filterImg[x][y] = imagem[x][y]
                        a = 0
                    else:
                        filterImg[x][y] = med
                        a = 0
                else:
                    m = m + 1
                    kernel = np.zeros(m*m)
                    if m <= M_max:
                        continue
                    else:
                        filterImg[x][y] = imagem[x][y]
                        m = 3
                        a = 0
                        kernel = np.zeros(m*m)

    return filterImg
                    
def Adapted(imagem,m,n):
    aux = np.shape(imagem)

    if np.size(aux) > 2:
        imagem = imagem[:][:][1]
        aux = np.shape(aux)

    filterImg = np.zeros(aux)
    kernel = np.zeros(m*n)
    media = np.mean(imagem)

    for x in range(aux[0]):
        for y in range(aux[1]):
            if (imagem[x][y] > 1.15*media) or (imagem[x][y] < 0.15*media):
                for u in range(m*n):
                    if (x+u%m-1 >= 0) and (x+u%m-1 < aux[0]) and (y+u%n-1 >= 0) and (y+u%n-1 < aux[1]):
                        kernel[u] = imagem[x+u%m-1][y+u%n-1]
                for v in range(m*n):
                    for t in range(v,m*n):
                        if kernel[v] > kernel[t]:
                            auxi = kernel[t]
                            kernel[t] = kernel[v]
                            kernel[v] = auxi
                if (m*n)%2 > 0:
                    filterImg[x][y] = kernel[int((m*n-1)/2)]
                else:
                    filterImg[x][y] = (kernel[int(np.floor(m*n/2))]+kernel[int(np.ceil(m*n/2))])/2
            else:
                filterImg[x][y] = imagem[x][y]

    return filterImg