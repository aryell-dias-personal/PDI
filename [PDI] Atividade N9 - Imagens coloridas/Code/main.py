import matplotlib.pyplot as plt 
import numpy as np
import iluminacao
import utils
import ruido

def filterRGB(imagem,m=3,n=3):
    ImgOriginal = utils.LerImage(imagem)

    imagem = np.uint8(ruido.Median(ImgOriginal,m,n))
    imagem = np.uint8(ruido.Median(imagem,m,n))

    fig,[ax1,ax2] = plt.subplots(1,2)
    ax1.imshow(ImgOriginal)
    ax2.imshow(imagem)

    plt.show()

def filterHSI(imagem,m=3,n=3):
    ImgOriginal = utils.LerImage(imagem)
    
    img = utils.rgb2hsi(ImgOriginal)
    img = ruido.Median(img,m,n)
    img = ruido.Median(img,m,n)
    img = ruido.Median(img,m,n)
    img = utils.hsi2rgb(img)

    fig,[ax1,ax2] = plt.subplots(1,2)
    ax1.imshow(ImgOriginal)
    ax2.imshow(img)

    plt.show()

if __name__ == '__main__':
    ImgOriginal = utils.LerImage('Image_(1b)')
    fig,[ax1,ax2] = plt.subplots(1,2)
    ax1.imshow(ImgOriginal)
    ax2.imshow(iluminacao.escurecer(ImgOriginal,0.02))
    plt.show()

    # filterRGB('Image_(2b)')
    # filterHSI('Image_(2a)',5,5)
    # ax2.imshow(imagem[:,:,0],cmap='gray')
    # ax3.imshow(imagem[:,:,1],cmap='gray')
    # ax4.imshow(imagem[:,:,2],cmap='gray')
