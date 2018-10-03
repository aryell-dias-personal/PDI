import matplotlib.pyplot as plt
import numpy as np

import utils
import extracao

def main(imagem):
    ImgOriginal = utils.LerImagem("../imagens/{}.bmp".format(imagem))

    ImgOriginal = utils.Binarizar(ImgOriginal)

    for i in range(np.shape(ImgOriginal)[0]):
        for j in range(np.shape(ImgOriginal)[1]):
            print(ImgOriginal[i][j])

    # borda = utils.bordas(ImgOriginal)

    fig,[ax1, ax2] = plt.subplots(1,2)
    ax1.imshow(ImgOriginal,cmap='gray')

    esqueleto = extracao.Esqueleto(ImgOriginal)

    ax2.imshow(extracao,cmap='gray')
    plt.show()

    # teste = extracao.ChainCode(borda,8)    
    # print(teste)

if __name__ == '__main__':
    main('Image_(3)')
