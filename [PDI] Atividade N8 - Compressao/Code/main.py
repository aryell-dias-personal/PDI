import matplotlib.pyplot as plt 
import numpy as np

import utils
import compressao
import descompressao

def mainQuant(imagem,bit):
    ImgOriginal = utils.LerImage(imagem)

    fig,[ax1, ax2] = plt.subplots(1,2)
    ax1.imshow(ImgOriginal, cmap='gray')

    q = compressao.Quant(imagem,bit)

    ax2.imshow(q,cmap='gray')

    plt.show()

if __name__ == '__main__':
    # mainQuant('Image_(3)',8)
    # ImgOriginal = utils.LerImage('Image_(2)')
    ImgOriginal = [[39,39,126,126],[39,39,126,126],[39,39,126,126],[39,39,126,126]]

    # q = np.shape(ImgOriginal)

    # q = compressao.Huffman('Image_(1)')
    # q = utils.Pad(ImgOriginal,8,8)
    dictionary = compressao.LZW(ImgOriginal)
    compress = compressao.LZWcompress(dictionary)
    decompress = descompressao.LZWdescompress(dictionary,compress,(4,4))
    decompress = np.uint8(decompress)
    # print(decompress, np.shape(decompress))

    # q = compressao.LZW(ImgOriginal,8192)    
    fig,[ax1, ax2] = plt.subplots(1,2)
    ax1.imshow(ImgOriginal, cmap='gray')
    ax2.imshow(decompress,cmap='gray')
    plt.show()

    
