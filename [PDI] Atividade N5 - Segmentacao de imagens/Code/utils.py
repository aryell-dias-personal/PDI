import matplotlib.image as mpimg
import numpy as np

def LerImagem(nome):
    imagem = mpimg.imread(nome)
    return imagem

def Normalizar(imagem):
    mini = np.min(imagem)
    maxi = np.max(imagem)

    imagem = imagem - mini

    imagem = imagem*255/(maxi-mini)

    return imagem

def Threshold(imagem):
    aux = np.shape(imagem)

    if np.size(aux) > 2:
        imagem = imagem[:][:][1]
        aux = np.shape(imagem)

    BinImg = np.zeros(aux)

    for x in range(aux[0]):
        for y in range(aux[1]):
            if imagem[x][y] > 0.33*np.max(imagem):
                BinImg[x][y] = 1
            else:
                BinImg[x][y] = 0

    return BinImg