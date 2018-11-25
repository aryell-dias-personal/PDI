import numpy as np
import matplotlib.image as mpimg
import cv2

def extraiRetas(imagem, threshold):
    print(imagem)
    lines = cv2.HoughLines(np.array(imagem[0], dtype=np.uint8),1,np.pi/360,threshold)
    retorno = np.zeros(np.shape(imagem))
    if(not lines is None):
        for things in lines:
            for rho,theta in things:
                a = np.cos(theta)
                b = np.sin(theta)
                x0 = a*rho
                y0 = b*rho
                x1 = int(x0 + 1000*(-b))
                y1 = int(y0 + 1000*(a))
                x2 = int(x0 - 1000*(-b))
                y2 = int(y0 - 1000*(a))
                retorno = cv2.line(retorno,(x1,y1),(x2,y2),(255,0,0),2)
    return retorno

def LerImage(imagem):
    try:
        img = mpimg.imread('../imagens/{}.jpg'.format(imagem))
    except:
        img = mpimg.imread('../imagens/{}.png'.format(imagem))
    return img

def rgb2gray(imagem):
    img = 0.3*imagem[:,:,0] + 0.59*imagem[:,:,1] + 0.11*imagem[:,:,2]

    return img

def Normalizar(imagem):
    mini = np.min(imagem)
    maxi = np.max(imagem)
    imagem = imagem - mini
    imagem = imagem*255/(maxi-mini)
    return imagem

def Binarizar(imagem):
    aux = np.shape(imagem)
    if np.size(aux) > 2:
        imagem = imagem[:,:,0]
        aux = np.shape(imagem)
    ImgBin = np.zeros(aux)
    for x in range(aux[0]):
        for y in range(aux[1]):
            # 0.1*np.max(imagem)
            if imagem[x][y] >= ((np.max(imagem)+np.min(imagem))/2):                
            # if imagem[x][y] >= 127:
                ImgBin[x][y] = 0
                # ImgBin[x][y] = 1
            else:
                ImgBin[x][y] = 1
                # ImgBin[x][y] = 0
    return ImgBin
