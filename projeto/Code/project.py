import numpy as np
import scipy.ndimage as scp
from skimage import feature, filters, morphology
import utils


def projeto_sobel(img):
    imagem = scp.morphology.grey_closing(img,size=9)
    imagem = scp.morphology.grey_opening(imagem,size=9)

    borda = filters.sobel(imagem)
    bor = filters.sobel(img)

    borda = bor - borda

    borda = abs(borda)

    block_size = 35
    local_thr = filters.threshold_local(borda,block_size,method='gaussian')
    borda = borda > local_thr     

    # borda = feature.canny(borda,sigma=2)

    return borda,imagem

def projeto_canny(imagem):

    img = scp.morphology.grey_closing(imagem,size=17)
    img = scp.morphology.grey_opening(img,size=17)

    imagem = imagem - img

    imagem = 1 - (np.max(imagem)-imagem)/(np.max(imagem)-np.min(imagem))

    borda = feature.canny(imagem,sigma=1)

    print(np.max(imagem) - np.min(imagem), np.mean(imagem), np.max(imagem))

    return borda

def projeto_rodrigo(imagem):
    borda = feature.canny(imagem,sigma=1)

    block_size = 55
    img = filters.threshold_adaptive(imagem,block_size)
    img = morphology.skeletonize(img)

    return borda, img