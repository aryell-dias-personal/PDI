import numpy as np
import matplotlib.pyplot as plt 
import utils
from skimage import filters
import project

def sobel(imagem):
    borda, imagem = project.projeto_sobel(img)
    fig, [ax1, ax2,ax3] = plt.subplots(1,3,figsize=(20,10))
    ax1.imshow(img, cmap='gray')
    ax2.imshow(imagem,cmap='gray')
    ax3.imshow(borda,cmap='gray')
    plt.show()

def aryell(imagem):
    retorno, esqueleto, retas, binarizado = project.projeto_aryell_3(imagem)
    # esqueleto = project.projeto_aryell_3(imagem)    
    # fig, ax = plt.subplots(1,1)
    fig, [(ax1, ax2), (ax3, ax4)] = plt.subplots(2,2,figsize=(20,10))
    ax1.imshow(binarizado,cmap='gray')
    ax2.imshow(esqueleto,cmap='gray')
    ax3.imshow(retas,cmap='gray')
    ax4.imshow(retorno, cmap='gray')
    # ax.imshow(esqueleto,cmap='gray')
    plt.show()

def aryell2(imagem):
    result, lines, borda = project.teste(img)
    fig, [(ax1, ax2),(ax3, ax4)] = plt.subplots(2,2,figsize=(20,10))

    ax1.imshow(utils.rgb2gray(img), cmap='gray')
    ax2.imshow(result,cmap='gray')
    ax3.imshow(result,cmap='gray')
    for line in lines:
        ax3.plot(*zip(*line), c='r')
    ax4.imshow(borda, cmap='gray')
    plt.show()

def canny(imagem):
    borda, img = project.projeto_canny(imagem)
    fig, [ax1, ax2, ax3] = plt.subplots(1,3,figsize=(20,10))
    ax1.imshow(imagem, cmap='gray')
    ax2.imshow(img,cmap='gray')
    ax3.imshow(borda,cmap='gray')
    plt.show()

def canny_banda(imagem):
    # R,G,B = project.canny_por_canal(imagem)
    result = project.canny_por_canal(imagem)

    fig, [[ax1,ax2],[ax3,ax4]] = plt.subplots(2,2,figsize=(20,10))

    ax1.imshow(imagem)
    ax2.imshow(res,cmap='gray')
    ax4.imshow(R,cmap='gray')
    ax5.imshow(G,cmap='gray')
    ax6.imshow(B,cmap='gray')
    plt.show()    

def r(imagem):
    img,a = project.rodrigo(imagem)

    fig, [ax1, ax2, ax3] = plt.subplots(1,3,figsize=(20,10), sharex=True, sharey=True)

    ax1.imshow(imagem, cmap='gray')
    ax2.imshow(img, cmap='gray')
    ax3.imshow(a,cmap='gray')
    plt.show()

if __name__ == '__main__': 
    for i in range(1,68):
        img = utils.LerImage(str(i))
        img = utils.rgb2gray(img)

        # print(img)
        # sobel(img)

        # canny_banda(img)

        r(img)

        # aryell(img)
        # aryell2(img)

        # plt.imshow(result,cmap='gray')
        # histogram = {}

        # canny(img)
        
        # r(img)
