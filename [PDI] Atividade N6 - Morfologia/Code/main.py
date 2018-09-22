import matplotlib.pyplot as plt
import utils


def mainOpera(imagem1,imagem2,Operacao):
    ImgOriginal1 = utils.LerImagem('../imagens/originais/{}.jpg'.format(imagem1))
    ImgOriginal2 = utils.LerImagem('../imagens/originais/{}.jpg'.format(imagem2))   

    # TODO something

    fig, [ax1,ax2,ax3] = plt.subplots(1,3,figsize=(20,30))
    ax1.imshow(ImgOriginal1,cmap='gray')
    ax2.imshow(ImgOriginal1,cmap='Greys')
    ax2.imshow("",cmap='Greys')
    plt.show()
    
if __name__ == '__main__':
    mainOpera('Image_(1a)','Image_(1b)','And')
