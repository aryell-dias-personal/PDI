import numpy as np
import matplotlib.pyplot as plt 
import utils

if __name__ == '__main__':
    img = utils.LerImage('63')

    imagem = utils.rgb2gray(img)

    imagem = utils.Median(imagem)

    imagem = utils.Binarizar(imagem)

    plt.imshow(imagem,cmap='gray')
    plt.show()