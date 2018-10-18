import numpy as np
import utils
import Operacoes

def segmentar(imagem):
    kernel = [[0,1,0],[1,1,1],[0,1,0]]

    img = utils.Binarizar(imagem)
    img = 1 - img

    img = Operacoes.Preencher_furos(img,kernel,1,1)

    return img


def color(imagem):
    aux = np.shape(imagem)

    r = np.zeros(aux)
    g = np.zeros(aux)
    b = np.zeros(aux)

    for x in range(aux[0]):
        for y in range(aux[1]):
            if imagem[x][y] >= 245: 
                r[x][y] = 255 # amarelo
                g[x][y] = 217
                b[x][y] = 15
            elif imagem[x][y] >= 210 and imagem[x][y] < 245: #210 a 245
                r[x][y] = 241 # vermelho
                g[x][y] = 78
                b[x][y] = 40
            elif imagem[x][y] >= 100 and imagem[x][y] < 210: #100 a 210
                r[x][y] = 0  # azul
                g[x][y] = 157
                b[x][y] = 220
            elif imagem[x][y] < 100:
                r[x][y] = 0
                g[x][y] = 0
                b[x][y] = 0

    img = segmentar(imagem)

    r = np.uint8(r*img)
    g = np.uint8(g*img)
    b = np.uint8(b*img)
    
    colorida = []

    colorida.append(r)
    colorida.append(g)
    colorida.append(b)

    colorida = np.einsum('abc->bca',colorida)

    return colorida
            

