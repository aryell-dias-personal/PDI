import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np


def initImage(X, Y):
    imagem = [[]]
    for j in range(0, int(X)):
        for i in range(0, int(Y)):
            imagem[j] = imagem[j] + [0]
        if(j < X-1):
            imagem += [[]]
    return imagem


def Zoom(nome, imagemOriginal, X, Y, Xdestiny, Ydestiny):
    cx = Xdestiny/X
    cy = Ydestiny/Y
    imagem = initImage(Xdestiny, Ydestiny)
    for j in range(0, int(X)):
        for i in range(0, int(Y)):
            imagem[int(j*cx)][int(i*cy)] = imagemOriginal[j][i]
    imagem = np.array(imagem, dtype=np.uint8)
    # imgplot = plt.imshow(imagem, cmap='gray')
    plt.hist(np.reshape(imagem,[-1]),bins=256, range=[0,255])
    plt.show()
    # plt.imsave('./Resultados/'+nome, imagem, cmap='gray')


def clarear(nome, imagemOriginal, c):
    plt.hist(np.reshape(imagemOriginal,[-1]),bins=256, range=[0,255])
    plt.show()
    imagemOriginal = np.log(c*imagemOriginal+1)
    imagemOriginal = imagemOriginal - np.min(imagemOriginal)
    imagemOriginal = imagemOriginal / np.max(imagemOriginal)
    imagemOriginal = imagemOriginal*255
    imagemOriginal = np.array(imagemOriginal, dtype=np.uint8)
    # imgplot = plt.imshow(imagemOriginal, cmap='gray')
    # plt.imsave('./Resultados/'+nome, imagemOriginal, cmap='gray')


def escurecer(nome, imagemOriginal, c):
    plt.hist(np.reshape(imagemOriginal,[-1]),bins=256, range=[0,255])
    plt.show()
    imagemOriginal = np.exp(c*imagemOriginal)
    imagemOriginal = imagemOriginal - np.min(imagemOriginal)
    imagemOriginal = imagemOriginal / np.max(imagemOriginal)
    imagemOriginal = imagemOriginal*255
    imagemOriginal = np.array(imagemOriginal, dtype=np.uint8)
    # imgplot = plt.imshow(imagemOriginal, cmap='gray')
    # plt.imsave('./Resultados/'+nome, imagemOriginal, cmap='gray')


# imagemOriginal = mpimg.imread('./Zoom/imagens/Zoom_in_(1).jpg')
# imagemOriginal = mpimg.imread('./Zoom/imagens/Zoom_in_(2).jpg')
# imagemOriginal = mpimg.imread('./Zoom/imagens/Zoom_in_(3).jpg')
# imagemOriginal = mpimg.imread('./Zoom/imagens/Zoom_out_(1).jpg')
# imagemOriginal = mpimg.imread('./Zoom/imagens/Zoom_out_(2).jpg')
# imagemOriginal = mpimg.imread('./Zoom/imagens/Zoom_out_(3).jpg')
imagemOriginal = mpimg.imread('./Realce/imagens/Clarear_(1).jpg')
# imagemOriginal = mpimg.imread('./Realce/imagens/Clarear_(2).jpg')
# imagemOriginal = mpimg.imread('./Realce/imagens/Clarear_(3).jpg')
# imagemOriginal = mpimg.imread('./Realce/imagens/Escurecer_(1).jpg')
# imagemOriginal = mpimg.imread('./Realce/imagens/Escurecer_(2).jpg')
# imagemOriginal = mpimg.imread('./Realce/imagens/Escurecer_(3).jpg')

# Zoom('Zoom_in_(1).jpg', imagemOriginal, 150.0, 100.0, 360.0, 480.0)
# Zoom('Zoom_in_(2).jpg', imagemOriginal, 500.0, 890.0, 1456, 2592)
# Zoom('Zoom_in_(3).jpg', imagemOriginal, 330, 250, 990.0, 720.0)
# Zoom('Zoom_out_(1).jpg', imagemOriginal, 500.0, 750.0, 120.0, 271.0)
# Zoom('Zoom_out_(2).jpg', imagemOriginal, 1600.0, 990.0, 500.0, 317.0)
# Zoom('Zoom_out_(3).jpg', imagemOriginal, 750.0, 330.0, 500.0, 174.0)
clarear('Clarear_(1).jpg', imagemOriginal,0.01)
# clarear('Clarear_(2).jpg', imagemOriginal,0.055)
# clarear('Clarear_(3).jpg', imagemOriginal,0.01)
# escurecer('Escurecer_(1).jpg', imagemOriginal, 0.012)
# escurecer('Escurecer_(2).jpg', imagemOriginal, 0.03)
# escurecer('Escurecer_(3).jpg', imagemOriginal, 0.03)
