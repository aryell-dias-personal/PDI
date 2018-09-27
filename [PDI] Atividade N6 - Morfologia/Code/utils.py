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
    if np.size(np.shape(img1)) > 2:
        img1 = img1[:,:,0]
    if np.size(np.shape(img2)) > 2:
        img2 = img2[:,:,0]
        
    x,y = np.shape(img1)
    if(operation == 'and'):
        return [[img1[i][j] and img2[i][j] for j in range(y)]for i in range(x)]
    elif(operation == 'or'):
        return [[img1[i][j] or img2[i][j] for j in range(y)]for i in range(x)]
    elif(operation == 'xor'):
        return [[((not img1[i][j]) and (img2[i][j])) or ((img1[i][j]) and (not img2[i][j])) for j in range(y)]for i in range(x)]
    elif(operation == 'nand'):
        return [[((not img1[i][j]) or (not img2[i][j])) for j in range(y)]for i in range(x)]

def Binarizar(imagem):
    aux = np.shape(imagem)

    if np.size(aux) > 2: # seleciona apenas uma matriz de cor caso a leitura seja rgb
        imagem = imagem[:,:,0]
        aux = np.shape(imagem)

    # imagem binária, 0 se for menor do que 128 e 1 maior do que 128

    ImgBin = np.zeros(aux)
    
    for x in range(aux[0]):
        for y in range(aux[1]):
            if imagem[x][y] >= 128:
                ImgBin[x][y] = 1
            else:
                ImgBin[x][y] = 0

    return ImgBin
 
