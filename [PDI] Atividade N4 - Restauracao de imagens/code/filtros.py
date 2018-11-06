import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

def Harmonic(imagem, m, n):
    imagem = imagem
    aux = np.shape(imagem)
    FiltImg = np.zeros(aux)
    soma = 0
    saltox = int(np.floor(m/2))
    saltoy = int(np.floor(n/2))
    # kernel = np.zeros([3,3])

    for x in range(aux[0]):
        for y in range(aux[1]):
            for u in range(-saltox,saltox):
                for v in range(-saltoy,saltoy):
                    if (x+u >= 0) and (x+u < aux[0]) and (y+v >= 0) and (y+v < aux[1]):
                        soma = soma + imagem[x+u][y+v]
            FiltImg[x][y] = m*n/(1/(soma+1))
            soma = 0
            # m = 0
            # n = 0

    mini = np.min(FiltImg)
    FiltImg = FiltImg - mini
    maxi = np.max(FiltImg)

    for x in range(aux[0]):
        for y in range(aux[1]):
            FiltImg[x][y] = np.rint(FiltImg[x][y]*255/(maxi-mini))

    return FiltImg

def ContraHarmonic(imagem, Q):
    # imagem = np.mean(imagem)
    aux = np.shape(imagem)
    FiltImg = np.zeros(aux)
    soma1 = float(0)
    soma2 = float(0)
    m = 3
    n = 3
    saltox = int(np.floor(m/2))
    saltoy = int(np.floor(n/2))

    for x in range(aux[0]):
        for y in range(aux[1]):
            for u in range(-saltox,saltox):
                for v in range(-saltoy,saltoy):
                    if (x+u >= 0) and (x+u < aux[0]) and (y+v >= 0) and (y+v < aux[1]):
                        if imagem[x+u][y+v] != 0:
                            soma1 = soma1 + np.float_power(imagem[x+u][y+v],Q+1)
                            soma2 = soma2 + np.float_power(imagem[x+u][y+v],Q)
                        else:
                            soma1 = soma1 + np.float_power(imagem[x+u][y+v]+1,Q+1)
                            soma2 = soma2 + np.float_power(imagem[x+u][y+v]+1,Q)
            FiltImg[x][y] = soma1/soma2
            soma1 = 0
            soma2 = 0

    mini = np.min(FiltImg)
    FiltImg = FiltImg - mini
    maxi = np.max(FiltImg)

    for x in range(aux[0]):
        for y in range(aux[1]):
            FiltImg[x][y] = np.rint(FiltImg[x][y]*255/(maxi-mini))

    return FiltImg

def AlphaTrim(imagem,d, m, n):
    # imagem = np.mean(imagem)
    aux = np.shape(imagem)
    FiltImg = np.zeros(aux)
    # m = 3
    # n = 3
    kernel = np.zeros(m*n)
    soma = 0
    xmax = aux[0]
    ymax = aux[1]

    for x in range(aux[0]):
        for y in range(aux[1]):
            for u in range(m*n): #(-saltox,saltox):
                if (x+u%m-1 >= 0) and (x+u%m-1 < xmax) and (y+u%n-1 >= 0) and (y+u%n-1 < ymax):
                    kernel[u] = imagem[x+u%m-1][y+u%n-1]

            for v in range(m*n):
                for t in range(v,(m*n)):
                    if kernel[v] > kernel[t]:
                        auxi = kernel[t]
                        kernel[t] = kernel[v]
                        kernel[v] = auxi

            for h in range(0+d//2,9-d//2):
                soma = soma + kernel[h]

            FiltImg[x][y] = soma/(m*n-d)
            kernel = np.zeros(m*n)
            soma = 0

    mini = np.min(FiltImg)
    FiltImg = FiltImg - mini
    maxi = np.max(FiltImg)

    for x in range(aux[0]):
        for y in range(aux[1]):
            FiltImg[x][y] = np.rint(FiltImg[x][y]*255/(maxi-mini))

    return FiltImg
