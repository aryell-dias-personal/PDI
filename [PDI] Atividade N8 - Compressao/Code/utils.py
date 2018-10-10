import matplotlib.image as mpimg
import numpy as np

def LerImage(imagem):
    img = mpimg.imread("../imagens/{}.tif".format(imagem))

    if np.size(np.shape(img)) > 2:
        img = img[:,:,0]

    return img

def Histograma(imagem):
    aux = np.shape(imagem)
    count = np.zeros(256)
    mem = 0

    for x in range(aux[0]):
        for y in range(aux[1]):
            count[imagem[x][y]] += 1

    return count


def Probabilidade(hist):
    histo = Histograma(hist)

    aux = np.shape(hist)

    pixels = aux[0]*aux[1]
    prob = np.zeros(256)

    for i in range(256):
        prob[i] = histo[i]/pixels

    return prob

def Normalizar(imagem):
    mini = np.min(imagem)
    maxi = np.max(imagem)

    img = 255*(imagem - mini)/(maxi-mini)

    return img
