import matplotlib.image as mpimg
import numpy as np

# leitura da imagem
def LerImagem(nome):
    imagem = mpimg.imread(nome)
    return imagem

# as operações foram interpretadas como sendo as classicas
# utilizando dos pixels nas correspondentes de uma imagem 
# para outra

def operation(img1,img2, operation):
    # img1 = np.array(img1[:,:,0], dtype=bool)
    # img2 = np.array(img2[:,:,0], dtype=bool)
    x,y = np.shape(img1)
    if(operation == 'and'):
        return [[img1[i][j] and img2[i][j] for j in range(y)]for i in range(x)]
    elif(operation == 'or'):
        return [[img1[i][j] or img2[i][j] for j in range(y)]for i in range(x)]
    elif(operation == 'xor'):
        return [[((not img1[i][j]) and (img2[i][j])) or ((img1[i][j]) and (not img2[i][j])) for j in range(y)]for i in range(x)]
    # seria um xnor?
    elif(operation == 'nand'):
        return [[not((img1[i][j]) and (img2[i][j])) for j in range(y)]for i in range(x)]


# quando for utilizado deve definir quanto deverá ser transladado
# por padrão os espaços desconhecidos (fora do escopo da imagem o-
# riginal) são preenchidos com 0
def translacao(conjunto, shape, Zx = 0, Zy = 0):
    x,y = np.shape(conjunto) 
    return [
        [
            conjunto[Zx+i][Zy+j]
            if Zx+i>0 and Zy+j>0 and Zx+i<x and Zy+j<y
            else 0 
            for j in range(y)
        ]
        for i in range(x)
    ]

def reflexao(conjunto):
    x,y = np.shape(conjunto) 
    return [
        [
            conjunto[aux[0] - i-1][aux[1] - j-1]
            for j in range(y)
        ]
        for i in range(x)
    ]

def intersecao(B,A):
    # depende de como é interpretado, a questão é que pode ser
    # que a posição x e y componha juntamente com o valor do pixel o valor
    # do ponto, permitindo fazer uma comparação ponto a ponto
    # neste caso supomos que a interseção apenas retorne 1 quando 
    # a mesma posicao em ambos os conjuntos for 1, caso esta interpretação
    # esteja correta, a interseção será equivalente a um and
    return operation(B,A,'and')
    # não faz sentido a posição x e y não interferir no processo, pois é obvio que a imagem
    # binária tem 0s e 1s.

def Binarizar(imagem):
    aux = np.shape(imagem)
    if np.size(aux) > 2:
        imagem = imagem[:,:,0]
        aux = np.shape(imagem)

    ImgBin = np.zeros(aux)
    
    for x in range(aux[0]):
        for y in range(aux[1]):
            if imagem[x][y] >= 128:
                ImgBin[x][y] = 1
            else:
                ImgBin[x][y] = 0

    return ImgBin
 
