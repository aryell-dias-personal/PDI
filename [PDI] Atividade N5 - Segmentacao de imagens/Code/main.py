import matplotlib.pyplot as plt
import utils
import filters
import bordas
import segmentacao

def main(imagem,tipo = 'Prewitt', filtro = 'Median', m = 9 ,n = 9):
    fig, [ax1,ax2] = plt.subplots(1,2,figsize=(20,30))
    # imagens
    ImgOriginal = utils.LerImagem('../images/{}.jpg'.format(imagem))
    imagemSegmentada = segmentacao.limirizacaoLocal(ImgOriginal)
    # subplots
    ax1.imshow(ImgOriginal,cmap='gray')
    ax2.imshow(imagemSegmentada,cmap='gray')
    # plots
    # plt.savefig('../resultados/{}_{}_{}_{}x{}.png'.format(tipo,imagem,filtro,m,n),dpi=150,bbox_inches='tight')
    plt.show()
    
if __name__ == '__main__':
    main('Image_(4)')