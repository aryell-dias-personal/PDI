import matplotlib.pyplot as plt
import utils
import Operacoes
import numpy as np

def mainOpera(imagem1,imagem2,operacao):
    # formato das imagens 1a e 1b são diferentes do esperado 
    ImgOriginal1 = utils.LerImagem('../imagens/{}.png'.format(imagem1))
    ImgOriginal2 = utils.LerImagem('../imagens/{}.png'.format(imagem2))   

    ImgResultado = utils.operation(ImgOriginal1,ImgOriginal2,operacao)

    fig, [ax1,ax2,ax3] = plt.subplots(1,3,figsize=(10,5))
    ax1.imshow(ImgOriginal1,cmap='gray')
    ax2.imshow(ImgOriginal2,cmap='gray')
    ax3.imshow(ImgResultado,cmap='gray')
    plt.show()

def filtro_de_ruido(imagem,SE,centrox,centroy):
    ImgOriginal = utils.LerImagem("../imagens/{}.jpg".format(imagem))
    ImgOriginal = utils.Binarizar(ImgOriginal)
    
    fig, [ax1,ax2] = plt.subplots(1,2)
    ax1.imshow(ImgOriginal,cmap='gray')

    imagem = Operacoes.Opening(ImgOriginal,kernel,centrox,centroy)
    imagem = Operacoes.Closing(imagem,kernel,centrox,centroy)
    
    ax2.imshow(imagem,cmap='gray')
    plt.show()

def Preenche_furos(imagem,SE,centrox,centroy):
    ImgOriginal = utils.LerImagem("../imagens/{}.jpg".format(imagem))
    fig, [ax1,ax2] = plt.subplots(1,2)
    ax1.imshow(ImgOriginal,cmap='gray')
    ImgOriginal = utils.Binarizar(ImgOriginal)

    imagem = Operacoes.Dilation(ImgOriginal,kernel,centrox,centroy)
    imagem = Operacoes.Dilation(imagem,kernel,centrox,centroy)

    imagem = Operacoes.Preencher_furos(imagem,kernel,centrox,centroy)
    
    imagem = Operacoes.Erosion(imagem,kernel,centrox,centroy)
    # imagem = Operacoes.Erosion(imagem,kernel,centrox,centroy)
    
    ax2.imshow(imagem,cmap='gray')
    plt.show()
    
def Quarta_Questao(imagem,SE,centrox,centroy):
    ImgOriginal = utils.LerImagem("../imagens/{}.jpg".format(imagem))
    ImgOriginal = utils.Binarizar(ImgOriginal)
    fig, [ax1,ax2] = plt.subplots(1,2)
    ax1.imshow(ImgOriginal,cmap='gray')

    imagemD = Operacoes.Dilation(ImgOriginal,SE,1,1)
    imagemD = Operacoes.Dilation(imagemD,SE,1,1)
    imagemD = Operacoes.Dilation(imagemD,SE,1,1)   

    imagem = Operacoes.Preencher_furos(imagemD,SE,1,1)

    imagem = Operacoes.Erosion(imagem,SE,1,1)
    imagem = Operacoes.Erosion(imagem,SE,1,1)
    imagem = Operacoes.Erosion(imagem,SE,1,1)

    ax2.imshow(imagem,cmap='gray')
    plt.show()


if __name__ == '__main__':
    # kernel = [[0,1,0],[1,1,1],[0,1,0]]
    # kernel2 = [[1,1,1],[1,1,1],[1,1,1]]

    mainOpera('Image_(1a)','Image_(1b)','nand')

    # filtro_de_ruido('Image_(2a)',kernel,cx,cy)

    # Preenche_furos('Image_(3a)',kernel,1,1)

    # Quarta_Questao('Image_(4a)',kernel,1,1)
    
    # mainPreenche('Image_(3a)')

    # plt.savefig('../resultados/teste_{}_{}_{}_{}x{}.png'.format(tipo,imagem,filtro,m,n),dpi=150,bbox_inches='tight')
