import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

from ruidos import ImpulseNoise, GaussianNoise
from filtros import Harmonic, ContraHarmonic, AlphaTrim
from utils import LerImagem, Histograma

def main():
    img = LerImagem('../image_(2).jpg')
    fig, [ax1,ax2, ax3] = plt.subplots(1,3)
    ax1.imshow(img,cmap='gray')

    # ImgRuido = ImpulseNoise(img,10,90)
    # ImgRuido = ImpulseNoise(img,15)
    # ImgRuido = GaussianNoise(img)
    # ax2.imshow(ImgRuido,cmap='gray')
    
    # ImgFiltrada = Harmonic(img, 11, 11)
    # ImgFiltrada = ContraHarmonic(img,2)
    # ImgFiltrada = ContraHarmonic(img,-2)
    ImgFiltrada = AlphaTrim(img,3,5,5)
    ImgFiltrada = ContraHarmonic(ImgFiltrada,2)

    ax2.imshow(ImgFiltrada,cmap='gray')
    
    # histo = Histograma(ImgRuido)
    # histo = Histograma(ImgFiltrada)
    
    # ax3.hist(ImgRuido.reshape([-1],),range(0,256))
    ax3.hist(ImgFiltrada.reshape([-1],),range(0,256))
    
    # ax3.plot(range(256),histo)
    plt.show()

    # plt.imshow(ImgRuido,cmap='gray')
    plt.imshow(ImgFiltrada,cmap='gray')
    plt.show()


if __name__ == '__main__':
    main()