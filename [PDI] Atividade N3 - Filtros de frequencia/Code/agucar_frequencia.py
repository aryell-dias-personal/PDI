import matplotlib.pyplot as plt
import matplotlib.image as mpimg
# from skimage import color
import numpy as np
# import math
from scipy import fftpack

# path = 'C:\users\digo_\documents\[PDI] Atividade N3 - Filtros de frequencia'

def LerImagem(nome):
    imagem = mpimg.imread(nome)
    # imagem = 
    return imagem

def is_power2(num):

	'states if a number is a power of two'

	return num != 0 and ((num & (num - 1)) == 0)

def pad(ImagemOriginal):
    ImagemOriginal = np.mean(ImagemOriginal,-1)
    size = np.shape(ImagemOriginal)
    aux = np.shape(ImagemOriginal)
    padImg = np.zeros(size)
    while any((not is_power2(size[0]), (size[0] < 2*aux[0]-1))): 
        padImg = np.zeros((size[0]+1,size[1]))
        size = np.shape(padImg)

    while any((not is_power2(size[1]), (size[1] < 2*aux[1]-1))): 
        padImg = np.zeros((size[0],size[1]+1))
        size = np.shape(padImg)

    for x in range(0,aux[0],1):
        for y in range(0,aux[1],1):
            # print(ImagemOriginal[x][y])
            padImg[x][y] = ImagemOriginal[x][y]

    pesos_X,pesos_Y = np.meshgrid(range(size[0]),range(size[1]))
    pesos = (-1)**(pesos_X+pesos_Y)
    padImg = np.multiply(padImg,pesos)
    
    for x in range(size[0]):
        for y in range(size[1]):
            if padImg[x][y] < 0:
                padImg[x][y] = 0

    return padImg   


# def DFT(paddedImg):
#     aux = np.shape(paddedImg)
#     V = np.zeros(aux, dtype=complex)
    
#     for u in range(aux[0]):
#         for v in range(aux[1]):
#             for x in range(aux[0]):
#                 for y in range(aux[1]):
#                     V[u][v] += paddedImg[x][y]*np.exp(-2*1j*np.pi*(u*x/aux[0]+v*y/aux[1]))
#                     print(y)

#     real = V.real
#     imagi = V.imag
#     norma = np.sqrt(real**2 + imagi**2)
#     fase = np.arctan2(imagi,real)
#     F = norma*np.exp(1j*fase)
#     mini = np.min(F)
#     F = F - mini
#     F = F*255/(np.max(F)-mini)
#     F = np.log10(V+1)

#     return F

def LogarithmicTransformation(image, max_val=255):

    c = max_val / (math.log(1 + image.max()))

    P = image.shape[0]
    Q = image.shape[1]

    transformed_image = np.zeros(image.shape)

    for line in range(P):
        for col in range(Q):
            transformed_image[line, col] = c * math.log(1 + abs(image[line, col]))

    return transformed_image

def FFT(paddedImg):
    aux = np.shape(paddedImg)
    wx = np.exp(-1j*np.pi)
    V = np.zeros(aux, dtype=complex)
    v1 = 0
    v2 = 0
    tam = aux[0]
    num = 1

    # w = np.zeros((aux))

    # for x in range(aux[0]):
    #     for y in range(aux[1]):
    #         w[x][y] = wx**(2*x*y)
        
    # X = w*paddedImg
    # X = X*w.transpose()
            
    # X = np.uint8(np.fft.fft2(paddedImg))

    while True:
        tam = tam/2
        num = num*2
        if tam == 2:
            break
    
    for y in range(aux[1]):
        for t in range(num):
            for i in range(t*2,2*t+2,1):
                if i == 2*t:
                    v1 = v1 + paddedImg[i][y]*wx**(2*np.floor(i/(2*t+1))*np.floor(i/(2*t+1)))
                elif i == 2*t+1:
                    v2 = v2 + paddedImg[i][y]*wx**(2*np.floor(i/(2*t+1))*np.floor(i/(2*t+1)))
            V[2*t][y] = (v1 + v2)
            # print(2*t)
            V[2*t+1][y] = (v1 - v2*(wx))
            # print(V[2*t+1][y])
            v1 = 0
            v2 = 0

    aux = np.shape(V)
    tam = aux[1]
    num = 1
    while True:
        tam = tam/2
        num = num*2
        if tam == 2:
            break

    for x in range(aux[1]):
        for t in range(num):
            for i in range(t*2,2*t+2,1):
                if i == 2*t:
                    v1 = v1 + paddedImg[x][i]*wx**(2*np.floor(i/(2*t+1))*np.floor(i/(2*t+1)))
                elif i == 2*t+1:
                    v2 = v2 + paddedImg[x][i]*wx**(2*np.floor(i/(2*t+1))*np.floor(i/(2*t+1)))
            V[x][2*t] = (v1 + v2)
            # print(2*t)
            V[x][2*t+1] = (v1 - v2*(wx))
            # print(V[2*t+1][y])
            v1 = 0
            v2 = 0

    real = V.real
    imagi = V.imag
    norma = np.sqrt(real**2 + imagi**2)
    fase = np.arctan2(imagi,real)
    F = np.zeros(aux, dtype=complex)
    F = norma*np.exp(1j*fase)
    F = np.uint8(F)
    # F = np.uint8(real**2 + imagi**2)
    mini = np.min(F)
    F = F - mini
    maxi = np.max(F)
    # print(np.max(F))
    for x in range(aux[0]):
        for y in range(aux[1]):
            F[x][y] = np.rint((F[x][y]*255)/(maxi-mini))
    
    # F = np.uint8(np.log10(F+1))
    print(F)
    # print(X)

    return F #LogarithmicTransformation(X)

if __name__ == '__main__':
    imagem = LerImagem("./Images/Capturar.jpg")
    # imagem = [[50,30,0,200],[150,70,89,32],[46,215,120,27],[81,155,2,100]]
    fig, [ax1,ax2, ax3] = plt.subplots(1,3)
    ax1.imshow(imagem,cmap='gray')
    padImg = pad(imagem)
    ax2.imshow(padImg,cmap='gray')
    fft = FFT(padImg)
    ax3.imshow(fft,cmap='gray')
    # plt.imshow(imagem)
    plt.show()



