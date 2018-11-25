import numpy as np
import matplotlib.pyplot as plt 
import utils
import project

def rodrigo(imagem):
    borda,imagem,aaaa = project.projeto_rodrigo(img)

    fig, [[ax1, ax2],[ax3,ax4]] = plt.subplots(2,2,figsize=(20,10))

    ax1.imshow(img, cmap='gray')
    ax2.imshow(borda,cmap='gray')
    ax3.imshow(imagem,cmap='gray')
    ax4.imshow(aaaa,cmap='gray')
    plt.show()

def sobel(imagem):
    borda, imagem = project.projeto_sobel(img)

    fig, [ax1, ax2,ax3] = plt.subplots(1,3,figsize=(20,10))

    ax1.imshow(img, cmap='gray')
    ax2.imshow(imagem,cmap='gray')
    ax3.imshow(borda,cmap='gray')
    plt.show()

def aryell(imagem):
    x,y = np.shape(imagem)
    retorno, borda, rejunte, imagem = project.projeto_aryell_2(imagem)
    fig, [(ax1, ax2), (ax3, ax4)] = plt.subplots(2,2,figsize=(20,10))
    ax1.imshow(imagem,cmap='gray')
    ax2.imshow(borda, cmap='gray')
    ax3.imshow(rejunte,cmap='gray')
    ax4.imshow(retorno,cmap='gray')
    plt.show()

def canny(imagem):
    borda, img = project.projeto_canny(imagem)

    fig, [ax1, ax2, ax3] = plt.subplots(1,3,figsize=(20,10))

    ax1.imshow(imagem, cmap='gray')
    ax2.imshow(img,cmap='gray')
    ax3.imshow(borda,cmap='gray')
    plt.show()

if __name__ == '__main__': 
    for i in range(1,68):
        img = utils.LerImage(str(i))
        img = utils.rgb2gray(img)
        aryell(img)

        # canny(img)

        # rodrigo(img)

    # imagem = project.projeto_aryell(img)

    # fig, [ax1, ax2] = plt.subplots(1,2,figsize=(20,10))

    # ax1.imshow(img, cmap='gray')
    # # ax2.imshow(borda and labeled,cmap='gray')
    # # ax2.imshow(labeled,cmap='gray')
    # ax2.imshow(imagem,cmap='gray')
    # plt.show()
