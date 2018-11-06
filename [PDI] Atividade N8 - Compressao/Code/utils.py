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


def Pad(imagem,g,l):
    size = np.shape(imagem)
    aux = size
    padImg = np.zeros(size)

    while size[0]%g != 0:
        padImg = np.zeros([size[0]+1,size[1]])
        size = np.shape(padImg)
    while size[1]%l != 0:
        padImg = np.zeros([size[0],size[1]+1])
        size = np.shape(padImg)

    if (aux[0]-size[0])%2 > 0:
        complemento = 1 
    else:
        complemento = 0

    if (aux[1]-size[1])%2 > 0:
        comp = 1 
    else:
        comp = 0
    
    for i in range(int(np.floor((size[0]-aux[0])/2)),int(size[0]-np.floor((size[0]-aux[0])/2)-complemento)):
        for j in range(int(np.floor((size[1]-aux[1])/2)),int(size[1]-np.floor((size[1]-aux[1])/2)-comp)):
            padImg[i][j] = imagem[i-int(np.floor((size[0]-aux[0])/2))][j-int(np.floor((size[1]-aux[1])/2))]

    return padImg