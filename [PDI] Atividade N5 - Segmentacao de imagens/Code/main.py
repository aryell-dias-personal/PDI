import matplotlib.pyplot as plt

import utils
from bordas import Prewitt


def main():
    ImgOriginal = utils.LerImagem('../imagens/Image_(1).jpg')
    fig, [ax1,ax2] = plt.subplots(1,2)
    ax1.imshow(ImgOriginal,cmap='gray')
    ImgFiltrada = Prewitt(ImgOriginal)
    # BinaryImg = utils.Threshold(ImgFiltrada)
    ax2.imshow(ImgFiltrada,cmap='gray')
    
    # plt.savefig('./resultados/prewitt'+  + '.png')
    plt.show()


if __name__ == '__main__':
    main()