import matplotlib.pyplot as plt
import utils
import filters
import bordas

def main(imagem,tipo,filtro,m,n):
    fig, [ax1,ax2, ax3] = plt.subplots(1,3,figsize=(20,30))
    # imagens
    ImgFiltrada = bordas.Derivative(ImgOriginal, tipo, filtro, m, n)
    ImgOriginal = utils.LerImagem('../imagens/{}.jpg'.format(imagem))
    BinaryImg = utils.Threshold(ImgFiltrada)
    imgTest = filters.Average(ImgOriginal,7)
    # subplots
    ax1.imshow(ImgOriginal,cmap='gray')
    ax2.imshow(BinaryImg,cmap='gray')
    ax3.imshow(imgTest,cmap='gray')
    plt.savefig('../resultados/{}_{}_{}_{}x{}.png'.format(tipo,imagem,filtro,m,n),dpi=150,bbox_inches='tight')
    plt.show()
    
if __name__ == '__main__':
    main('Image_(1a)','Prewitt','Median',9,9)