import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

from ruidos import ImpulseNoise, GaussianNoise
from filtros import Harmonic, ContraHarmonic, AlphaTrim
from utils import LerImagem, Histograma

def main():
    img = LerImagem('../imagens/image_(4).jpg')
    fig, [ax1,ax2,ax3,ax4] = plt.subplots(1,4)
    ax1.imshow(img,cmap='gray')

    ax2.hist(img.reshape([-1],),range(0,256))

    # ImgRuido = ImpulseNoise(img,10,90)
    # ImgRuido = ImpulseNoise(img,15)
    # ImgRuido = GaussianNoise(img)
    # ax3.imshow(ImgRuido,cmap='gray')
    
    # ImgFiltrada = Harmonic(img, 11, 11)
    # ImgFiltrada = ContraHarmonic(img,2)
    # ImgFiltrada = ContraHarmonic(img,-2)
    ImgFiltrada = AlphaTrim(img,3,5,5)
    ImgFiltrada = ContraHarmonic(ImgFiltrada,2)

    ax3.imshow(ImgFiltrada,cmap='gray')
    
    # histo = Histograma(ImgRuido)
    # histo = Histograma(ImgFiltrada)
    
    # ax4.hist(ImgRuido.reshape([-1],),range(0,256))
    ax4.hist(ImgFiltrada.reshape([-1],),range(0,256))
    
    # ax4.plot(range(256),histo)
    plt.show()

    # plt.imshow(ImgRuido,cmap='gray')
    plt.imshow(ImgFiltrada,cmap='gray')
    plt.show()

    SoRuido = img - ImgFiltrada
    # SoRuido = ImgRuido - np.mean(img)

    fig, [AX1,AX2] = plt.subplots(1,2)

    AX1.imshow(SoRuido,cmap='gray')
    AX2.hist(SoRuido.reshape([-1],),range(0,256))
    plt.show()

if __name__ == '__main__':
    main()