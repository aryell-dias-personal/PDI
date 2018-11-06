import numpy as np
import matplotlib.image as mpimg

def LerImage(imagem):
    img = mpimg.imread('../imagens/{}.jpg'.format(imagem))
    return img

def rgb2gray(imagem):
    img = 0.3*imagem[:,:,0] + 0.59*imagem[:,:,1] + 0.11*imagem[:,:,2]

    return img

