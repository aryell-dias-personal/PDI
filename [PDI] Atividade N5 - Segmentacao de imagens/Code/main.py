import matplotlib.pyplot as plt
import numpy as np
import utils
import filters
import bordas
import segmentacao


def main(imagem,tipo,filtro,m,n):
    ImgOriginal = utils.LerImagem('../imagens/{}.jpg'.format(imagem))    
    
    # ImgFiltrada = bordas.Derivative(ImgOriginal,tipo, filtro,m,n)
    
    # limiar = 0.1*np.mean(ImgFiltrada)
    # BinaryImg = utils.Threshold(ImgFiltrada,limiar)   

    BinaryImg = bordas.Canny(ImgOriginal,m,n) 

    fig, [ax1,ax2] = plt.subplots(1,2,figsize=(20,30))
    ax1.imshow(ImgOriginal,cmap='gray')
    ax2.imshow(BinaryImg,cmap='Greys')
    
    plt.savefig('../resultados/teste_{}_{}_{}_{}x{}.png'.format(tipo,imagem,filtro,m,n),dpi=150,bbox_inches='tight')
    
    plt.show()
    
if __name__ == '__main__':
    main('Image_(1a)','Canny','Gaussian',0.3,0.6)
