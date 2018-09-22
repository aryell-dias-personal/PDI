import matplotlib.image as mpimg
import numpy as np

# leitura da imagem
def LerImagem(nome):
    imagem = mpimg.imread(nome)
    return imagem

