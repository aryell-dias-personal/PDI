import utils
import numpy as np
import matplotlib.pyplot as plt

def Dilation(imagem, SE, centrox, centroy):
    aux = np.shape(imagem)

    if np.size(aux) > 2:
        imagem = imagem[:][:][0]
        aux = np.shape(imagem)
    
    for x in range(aux[0]):
        for y in range(aux[1]):
            imagem[x][y] = np.abs(imagem[x][y] - 1)

    ImgDilat = Erosion(imagem, SE, centrox, centroy)

    for x in range(aux[0]):
        for y in range(aux[1]):
            ImgDilat[x][y] = np.abs(ImgDilat[x][y] - 1)

    return ImgDilat

def Erosion(imagem, SE, centrox, centroy):
    aux = np.shape(imagem)

    if np.size(aux) > 2:
        imagem = imagem[:][:][0]
        aux = np.shape(imagem)

    ImgErod = []
    ImgLinha = []
    tam = np.shape(SE)
    check = 0
    total = 0

    for u in range(tam[0]):
        for v in range(tam[1]):
            if SE[u][v] != 0:
                total += 1

    for x in range(aux[0]):
        for y in range(aux[1]):
            if imagem[x][y] == 1:
                for u in range(0-centrox,tam[0]-centrox):
                    for v in range(0-centroy,tam[1]-centroy):
                        if x+u >= 0 and x+u <aux[0] and y+v >= 0 and y+v < aux[1]: 
                            check += SE[u+centrox][v+centroy]*imagem[x+u][y+v]
                if check == total:
                    ImgLinha.append(1)
                else:
                    ImgLinha.append(0)
                check = 0
            else:
                ImgLinha.append(0)
        ImgErod.append(ImgLinha)
        ImgLinha = []
            
    a = np.shape(ImgErod)
        
    return ImgErod

def Opening(imagem,SE,centrox,centroy):
    ImgOpen = Dilation(Erosion(imagem,SE,centrox,centroy),SE,centrox,centroy)
    return ImgOpen

def Closing(imagem,SE,centrox,centroy):
    ImgClose = Erosion(Dilation(imagem,SE,centrox,centroy),SE,centrox,centroy)
    return ImgClose

def Preencher_furos(imagem):

    aux = np.shape(imagem)

    if np.size(aux) > 2:
        imagem = imagem[:][:][0]
        aux = np.shape(imagem)

    # ImgOriginal = utils.Binarizar(imagem)

    CompImg = np.zeros(aux)

    for x in range(aux[0]):
        for y in range(aux[1]):
            CompImg[x][y] = 1 - imagem[x][y]

    MarkerImg = np.zeros(aux)

    for y in range(aux[1]):
        MarkerImg[0][y] = 1 - imagem[0][y]
        MarkerImg[aux[0]-1][y] = 1 - imagem[aux[0]-1][y]

    for x in range(aux[0]):
        MarkerImg[x][0] = 1 - imagem[x][0]
        MarkerImg[x][aux[1]-1] = 1 - imagem[x][aux[1]-1]

    SE = [[1,1,1],[1,1,1],[1,1,1]]

    ImgSemFuros = Geo_Dil(MarkerImg,CompImg,SE,1,1)

    return ImgSemFuros
    

def Geo_Dil(markerimagem,maskimagem,SE,centrox,centroy):
    aux1 = np.shape(markerimagem)

    if np.size(aux1) > 2:
        markerimagem = markerimagem[:][:][0]
        aux1 = np.shape(markerimagem)

    if np.size(np.shape(maskimagem)) > 2:
        maskimagem = maskimagem[:][:][0]    

    stop = 0
    x = 0
    lastImg = np.zeros(aux1)
    ones = np.ones(aux1)

    while stop == 0:
        ImgDilat = Dilation(markerimagem,SE,centrox,centroy)
        ImgGeoDilat = utils.operation(ImgDilat,maskimagem,'and')
        # ImgGeoDilat = ones - ImgGeoDilat
        if x == 49:
            fig, [ax1,ax2] = plt.subplots(1,2,figsize=(20,30))
            ax1.imshow(lastImg,cmap='gray')
            ax2.imshow(ImgGeoDilat,cmap='gray')
            plt.show()
        if np.allclose(lastImg,ImgGeoDilat):
            stop = 1
            print('funfou')
        else:
            lastImg = ImgGeoDilat
            markerimagem = ImgGeoDilat
            x += 1
            if x == 50:
                print('andou')
                x = 0



    return ImgGeoDilat
    