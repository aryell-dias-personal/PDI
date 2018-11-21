import numpy as np
import scipy
import scipy.ndimage as scp
import cv2
from skimage import feature, filters, morphology
import utils


def projeto_sobel(imagem):
    
    imagem = 1 - (np.max(imagem)-imagem)/(np.max(imagem)-np.min(imagem))

    img = filters.median(imagem,morphology.square(3))
    # bor = filters.sobel(imagem)

    # imagem = scp.morphology.grey_closing(imagem,size=9)
    # imagem = scp.morphology.grey_opening(imagem,size=9)

    imagem = abs(imagem - img)

    borda = filters.sobel(imagem)    

    # borda = bor - borda

    # borda = abs(borda)

    # block_size = 55
    # local_thr = filters.threshold_local(borda,block_size,method='gaussian')
    # borda = borda > local_thr     

    # borda = morphology.skeletonize(borda)
    # borda = scp.morphology.binary_closing(borda)

    # print(np.max(img), np.min(img), np.max(borda), np.min(borda))

    return borda,imagem

def projeto_canny(imagem):

    img = scp.morphology.grey_closing(imagem,size=17)
    img = scp.morphology.grey_opening(img,size=17)

    imagem = imagem - img

    img = 1 - (np.max(imagem)-imagem)/(np.max(imagem)-np.min(imagem))

    borda = feature.canny(img,sigma=1)

    # print(np.max(img) - np.min(img), np.mean(img), np.max(img))

    return borda, imagem

def projeto_rodrigo(imagem):
    borda = feature.canny(imagem,sigma=1)

    block_size = 45
    img = filters.threshold_adaptive(imagem,block_size,offset=10)
    img = 1 - img
    img = morphology.skeletonize(img)

    res = borda + img

    for x in range(np.shape(res)[0]):
        for y in range(np.shape(res)[1]):
            if res[x][y] > 0:
                res[x][y] = 1

    res = scp.morphology.grey_closing(res,size=9)

    return borda, img, res
