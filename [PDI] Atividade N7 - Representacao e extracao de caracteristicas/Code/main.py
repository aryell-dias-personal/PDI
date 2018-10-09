import matplotlib.pyplot as plt
import numpy as np

import utils
import extracao

def esqueletizacao(imagem):
    ImgOriginal = utils.LerImagem("../imagens/{}.bmp".format(imagem))

    ImgOriginal = utils.Binarizar(ImgOriginal)

    esqueleto = extracao.Esqueleto(ImgOriginal)

    fig,[ax1, ax2] = plt.subplots(1,2)
    ax1.imshow(ImgOriginal,cmap='gray')

    ax2.imshow(esqueleto,cmap='gray')
    plt.show()


def Chain(imagem):
    ImgOriginal = utils.LerImagem("../imagens/{}.bmp".format(imagem))

    ImgOriginal = utils.Binarizar(ImgOriginal)

    borda = utils.bordas(ImgOriginal)

    # fig,[ax1, ax2] = plt.subplots(1,2)
    # ax1.imshow(ImgOriginal,cmap='gray')

    # ax2.imshow(borda,cmap='gray')
    # plt.show()

    teste = extracao.ChainCode(borda,8, 30, 30)    
    print(teste)

if __name__ == '__main__':
    # Chain('Image_(1)')
    esqueletizacao('Image_(3)')
    
