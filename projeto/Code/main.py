import numpy as np
import matplotlib.pyplot as plt 
import utils
import project


if __name__ == '__main__': 
    for i in range(1,68):
        img = utils.LerImage(str(i))

        img = utils.rgb2gray(img)

        # imagem = utils.Median(imagem,9,9)

        # imagem = utils.Binarizar(imagem)  

        borda, imagem = project.projeto(img)

        fig, [ax1, ax2, ax3] = plt.subplots(1,3,figsize=(20,10))

        ax1.imshow(img, cmap='gray')
        ax2.imshow(imagem,cmap='gray')
        ax3.imshow(borda,cmap='gray')
        plt.show()