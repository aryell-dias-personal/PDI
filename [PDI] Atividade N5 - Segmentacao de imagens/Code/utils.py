import matplotlib.image as mpimg
import numpy as np

# leitura da imagem
def LerImagem(nome):
    imagem = mpimg.imread(nome)
    return imagem

# normalização da imagem
def Normalizar(imagem):
    mini = np.min(imagem)
    maxi = np.max(imagem)
    imagem = imagem - mini
    # diferença entre a imagem e o mínimo vezes 
    # 255 dividido pela diferença entre o máximo
    # e o minimo
    imagem = imagem*255/(maxi-mini)
    return imagem

def Threshold(imagem):
    aux = np.shape(imagem)

    # caso a imagem possua mais de dois shapes (duas dimensões)
    # ignoramos algumas coordenadas
    if np.size(aux) > 2:
        imagem = imagem[:][:][1]
        aux = np.shape(imagem)

    # imagem preenchida apenas com zeros
    BinImg = np.zeros(aux)

    for x in range(aux[0]):
        for y in range(aux[1]):
            if imagem[x][y] > 0.33*np.max(imagem):
                # se maior o máximo da imagem é 1
                BinImg[x][y] = 1
            else:
                # se não é 0
                BinImg[x][y] = 0

    return BinImg