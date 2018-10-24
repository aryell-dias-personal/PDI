import matplotlib.pyplot as plt 
import numpy as np
import iluminacao
import utils
import ruido
import colori

def filterRGB(imagem,m=3,n=3):
    ImgOriginal = utils.LerImage(imagem)

    # imagem = np.uint8(ruido.average(ImgOriginal,m,n))
    # imagem = np.uint8(ruido.Median(imagem,m,n))
    imagem = np.uint8(ruido.Median(ImgOriginal,m,n))

    # imagem = np.uint8(ruido.min_max(imagem,m,n))

    imagem = np.uint8(ruido.midpoint(imagem,m,n))

    fig,[ax1,ax2] = plt.subplots(1,2)
    ax1.imshow(ImgOriginal)
    ax2.imshow(imagem)

    plt.show()

def filterHSI(imagem,m=3,n=3):
    ImgOriginal = utils.LerImage(imagem)
    
    img = utils.rgb2hsi(ImgOriginal)
    
    # img = ruido.average(img,m,n)
    # img = ruido.Median(img,m,n)
    # img = ruido.Median(img,m,n)
    img = ruido.midpoint(img,m,n)
    
    img = utils.hsi2rgb(img)

    fig,[ax1,ax2] = plt.subplots(1,2)
    ax1.imshow(ImgOriginal)
    ax2.imshow(img)

    plt.show()

def cor(imagem):
    ImgOriginal = utils.LerImage('Image_(3a)')

    img = colori.color(ImgOriginal)

    fig,[ax1,ax2] = plt.subplots(1,2)
    ax1.imshow(ImgOriginal,cmap='gray')
    ax2.imshow(img)

    plt.show()
    

def escurecer(imagem,m):
    ImgOriginal = utils.LerImage('Image_(1b)')
    fig,[ax1,ax2] = plt.subplots(1,2)
    ax1.imshow(ImgOriginal)
    ax2.imshow(iluminacao.escurecer(ImgOriginal,m))
    plt.show()

def clarear(imagem,m):
    ImgOriginal = utils.LerImage(imagem)
    fig,[ax1,ax2] = plt.subplots(1,2)
    ax1.imshow(ImgOriginal)
    ax2.imshow(iluminacao.clarear(ImgOriginal,m))
    plt.show()

if __name__ == '__main__':
    # filterRGB('Image_(2b)',5,5)

    filterHSI('Image_(2a)')

    # cor('Image_(3a)')   

    # escurecer('Image_(1b)', 0.008)

    # clarear('Image_(1a)', 0.2)