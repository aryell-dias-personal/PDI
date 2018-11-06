import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

def LerImagem(nome):
    imagem = mpimg.imread(nome)
    return imagem

def Histograma(imagem):
    aux = np.shape(imagem)
    count = np.zeros(256)
    mem = 0

    for pixel in range(256):
        for x in range(aux[0]):
            for y in range(aux[1]):
                mem = imagem[x][y]
                if  mem == pixel:
                    count[pixel] = count[pixel] + 1

    return count

# def saveImg():
#     plt.imsave('../resultados/.jpg', gaussianNoise(imagemOrignal), cmap='gray')

