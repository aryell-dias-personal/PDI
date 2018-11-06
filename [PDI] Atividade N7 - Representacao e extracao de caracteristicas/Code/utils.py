import matplotlib.image as mpimg
import numpy as np
import matplotlib.pyplot as plt

def LerImagem(nome):
    imagem = mpimg.imread(nome)
    
    if np.size(np.shape(imagem)) > 2:
        imagem = imagem[:,:,0]
    
    # imagem = Binarizar(imagem)

    return imagem

def Binarizar(imagem):
    aux = np.shape(imagem)

    # imagem binária, 0 se for menor do que 128 e 1 maior do que 128

    ImgBin = np.zeros(aux)
    
    for x in range(aux[0]):
        for y in range(aux[1]):
            if imagem[x][y] >= 128:
                ImgBin[x][y] = np.uint8(1)
            else:
                ImgBin[x][y] = np.uint8(0)

    # for i in range(np.shape(ImgBin)[0]):
    #     for j in range(np.shape(ImgBin)[1]):
    #         print(ImgBin[i][j])

    return ImgBin

def Erosion(imagem, SE, centrox, centroy):
    aux = np.shape(imagem)

    ImgErod = [] # array vazio que será responsável pelas colunas da imagem
    ImgLinha = [] # array vazio que será responsável pelas linhas da imagem
    tam = np.shape(SE) # tamanho do elemento estruturante (SE)
    check = 0 # flag para indicar se o SE está completamente contido no objeto
    total = 0 # flag para indicar a quantidade de pixels 1 dentro do elemento estruturante

    for u in range(tam[0]):
        for v in range(tam[1]):
            if SE[u][v] != 0:
                total += 1 # contagem da quantidade de pixels maior que zero

    for x in range(aux[0]):
        for y in range(aux[1]):
            if imagem[x][y] == 1: # verifica se o pixel sobre analise é branco
                for u in range(0-centrox,tam[0]-centrox):
                    for v in range(0-centroy,tam[1]-centroy):
                        if x+u >= 0 and x+u <aux[0] and y+v >= 0 and y+v < aux[1]: 
                            # incrementa o flag se o SE está td contido no objeto
                            check += SE[u+centrox][v+centroy]*imagem[x+u][y+v] 
                if check == total: # se o SE está td contido no objeto da imagem
                    ImgLinha.append(1) # adiciona-se um pixel igual a 1
                else: # caso contrário, adiciona-se um pixel igual a 0
                    ImgLinha.append(0)
                check = 0
            else:
                ImgLinha.append(0)
        ImgErod.append(ImgLinha) # se adiciona-se uma nova coluna no array
        ImgLinha = []

    # corrige os valores das bordas

    copia = np.copy(ImgErod)

    ImgErod[0][:] = copia[1][:]
    ImgErod[-1][:] = copia[-2][:]
    
    for x in range(aux[0]):
        ImgErod[x][0] = copia[x][1]     
        ImgErod[x][-1] = copia[x][-2] 

    ImgErod[0][0] = 0
    ImgErod[-1][-1] = 0
    ImgErod[-1][0] = 0
    ImgErod[0][-1] = 0

    return ImgErod

def Dilation(imagem, SE, centrox, centroy):
    aux = np.shape(imagem)
    
    for x in range(aux[0]): # cria-se o complemento da imagem
        for y in range(aux[1]):
            imagem[x][y] = 1 - imagem[x][y]

    ImgDilat = Erosion(imagem, SE, centrox, centroy) # erode o complemento da imagem

    for x in range(aux[0]): # tira-se o complemento da imagem erodida
        for y in range(aux[1]):
            ImgDilat[x][y] = 1 - ImgDilat[x][y]

    return ImgDilat

def bordas(imagem):
    kernel = [[0,1,0],[1,1,1],[0,1,0]]
    
    # imagem = Binarizar(imagem)

    ImgDil = Dilation(imagem,kernel,1,1)
    ImgDil = Dilation(ImgDil,kernel,1,1)
    ImgDil = Dilation(ImgDil,kernel,1,1)

    ImgEro = Erosion(imagem,kernel,1,1)

    ImgBorda = np.abs(np.array(ImgDil) - np.array(ImgEro))
    ImgBorda = 1 - ImgBorda

    return ImgBorda
