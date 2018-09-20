import matplotlib.pyplot as plt
import numpy as np
import utils
import filters
import bordas
import segmentacao

def main(imagem,tipo,filtro,m,n):
    ImgOriginal = np.array(segmentacao.limirizacaoLocal(utils.LerImagem('../images/{}.jpg'.format(imagem)), 'sobel',),dtype='uint8')    
        
    BinaryImg = segmentacao.otsu(ImgOriginal)    

    fig, [ax1,ax2] = plt.subplots(1,2,figsize=(20,30))
    ax1.imshow(ImgOriginal,cmap='gray')
    ax2.imshow(BinaryImg,cmap='gray')
    
    # plt.savefig('../resultados/teste_{}_{}_{}_{}x{}.png'.format(tipo,imagem,filtro,m,n),dpi=150,bbox_inches='tight')
    
    plt.show()
    
if __name__ == '__main__':
    main('Image_(3b)','Sobel','Average',5,5)