import matplotlib.pyplot as plt 
import utils
import compressao
import numpy as np

def mainQuant(imagem,bit):
    ImgOriginal = utils.LerImage(imagem)

    fig,[ax1, ax2] = plt.subplots(1,2)
    ax1.imshow(ImgOriginal, cmap='gray')

    q = compressao.Quant(imagem,bit)

    ax2.imshow(q,cmap='gray')

    plt.show()

if __name__ == '__main__':
    # mainQuant('Image_(3)',8)
    ImgOriginal = utils.LerImage('Image_(1)')

    q = compressao.Huffman('Image_(1)')

    fig,[ax1, ax2] = plt.subplots(1,2)
    ax1.imshow(ImgOriginal, cmap='gray')
    # ax2.imshow(q,cmap='gray')
    plt.show()

    
