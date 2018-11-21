import numpy as np
import matplotlib.image as mpimg

def LerImage(imagem):
    try:
        img = mpimg.imread('../imagens/{}.jpg'.format(imagem))
    except:
        img = mpimg.imread('../imagens/{}.png'.format(imagem))
    return img

def rgb2gray(imagem):
    img = 0.3*imagem[:,:,0] + 0.59*imagem[:,:,1] + 0.11*imagem[:,:,2]

    return img

def Normalizar(imagem):
    mini = np.min(imagem)
    maxi = np.max(imagem)
    imagem = imagem - mini
    imagem = imagem*255/(maxi-mini)
    return imagem

def Binarizar(imagem):
    aux = np.shape(imagem)
    if np.size(aux) > 2:
        imagem = imagem[:,:,0]
        aux = np.shape(imagem)
    ImgBin = np.zeros(aux)
    for x in range(aux[0]):
        for y in range(aux[1]):
            # 0.1*np.max(imagem)
            if imagem[x][y] >= 127:
                ImgBin[x][y] = 1
            else:
                ImgBin[x][y] = 0
    return ImgBin
