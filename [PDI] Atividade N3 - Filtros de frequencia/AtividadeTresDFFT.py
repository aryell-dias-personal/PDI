import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

def LerImagem(nome):
    imagem = mpimg.imread(nome)
    return imagem

def pad(ImagemOriginal):
    size = np.shape(ImagemOriginal)
    padImg = np.zeros((size))
    while size[0]%2 != 0: 
        padImg = np.zeros((size[0]+1,size[1]))
        size = np.shape(padImg)

    while size[1]%2 != 0:
        padImg = np.zeros((size[0],size[1]+1))
        size = np.shape(padImg)

    return padImg

# def Fourier(paddedImg):

if __name__ == '__main__':
    imagem = LerImagem('./Images/Agucar_(1).jpg')
    plt.imshow(imagem,cmap='gray')
    padImg = pad(imagem)
    

