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

def Median(imagem,m=5,n=5):
    aux = np.shape(imagem)

    if np.size(aux) > 2:
        imagem = imagem[:][:][0]
        aux = np.shape(imagem)
    
    filterImg = np.zeros(aux)
    kernel = np.zeros(m*n)

    for x in range(aux[0]):
        for y in range(aux[1]):
            for u in range(m*n):
                if (x+u%m-1 >= 0) and (x+u%m-1 < aux[0]) and (y+u%n-1 >= 0) and (y+u%n-1 < aux[1]):
                    kernel[u] = imagem[x+u%m-1][y+u%n-1]
            for v in range(m*n):
                for t in range(v,m*n):
                    if kernel[v] > kernel[t]:
                        auxi = kernel[t]
                        kernel[t] = kernel[v]
                        kernel[v] = auxi
            if (m*n)%2 > 0:
                filterImg[x][y] = kernel[int((m*n-1)/2)]
            else:
                filterImg[x][y] = (kernel[int(np.floor(m*n/2))]+kernel[int(np.ceil(m*n/2))])/2

    # filterImg = imagem - filterImg

    # plt.imshow(filterImg,cmap='gray')
    # plt.show()

    return filterImg

def Binarizar(imagem):
    aux = np.shape(imagem)

    if np.size(aux) > 2: # seleciona apenas uma matriz de cor caso a leitura seja rgb
        imagem = imagem[:,:,0]
        aux = np.shape(imagem)

    # imagem binária, 0 se for menor do que 128 e 1 maior do que 128

    ImgBin = np.zeros(aux)
    
    for x in range(aux[0]):
        for y in range(aux[1]):
            if imagem[x][y] >= 0.4*np.max(imagem):
                ImgBin[x][y] = 1
            else:
                ImgBin[x][y] = 0

    return ImgBin
