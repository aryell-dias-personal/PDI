import matplotlib.pyplot as plt
import Utils
import Operacoes

def mainPreenche(imagem):
    ImgOriginal = Utils.LerImagem('../Imagens/Originais/{}.png'.format(imagem1))

    ImgResultado = Operacoes.dilata(ImgOriginal)

    fig, [ax1,ax2] = plt.subplots(1,2,figsize=(20,30))
    ax1.imshow(ImgOriginal1,cmap='gray')
    ax2.imshow(ImgResultado,cmap='gray')
    plt.show()
    

def mainOpera(imagem1,imagem2,operacao):
    # formato das imagens 1a e 1b são diferentes do esperado 
    ImgOriginal1 = Utils.LerImagem('../Imagens/Originais/{}.png'.format(imagem1))
    ImgOriginal2 = Utils.LerImagem('../Imagens/Originais/{}.png'.format(imagem2))   

    ImgResultado = Utils.operation(ImgOriginal1,ImgOriginal2,operacao)

    fig, [ax1,ax2,ax3] = plt.subplots(1,3,figsize=(20,30))
    ax1.imshow(ImgOriginal1,cmap='gray')
    ax2.imshow(ImgOriginal2,cmap='gray')
    ax3.imshow(ImgResultado,cmap='gray')
    plt.show()
    
if __name__ == '__main__':
    # mainOpera('Image_(1a)','Image_(1b)','xand')
    mainPreenche('Image_(3a)')
