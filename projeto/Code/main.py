import numpy as np
import matplotlib.pyplot as plt 
import utils
import project


if __name__ == '__main__': 
    # for i in range(1,68):
    img = utils.LerImage(str(19))

    img = utils.rgb2gray(img)

    # imagem = utils.Median(imagem,9,9)

    # imagem = utils.Binarizar(imagem)  

    # borda, imagem = project.projeto_sobel(img)

    # borda = project.projeto_canny(img)

    imagem = project.projeto_aryell(img)

    fig, [ax1, ax2] = plt.subplots(1,2,figsize=(20,10))

    ax1.imshow(img, cmap='gray')
    # ax2.imshow(borda and labeled,cmap='gray')
    # ax2.imshow(labeled,cmap='gray')
    ax2.imshow(imagem,cmap='gray')
    plt.show()