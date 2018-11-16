import numpy as np
import scipy.ndimage as scp
from skimage import feature, filters, morphology
import utils


def projeto(img):
    imagem = scp.morphology.grey_closing(img,size=9)
    # imagem = scp.median_filter(img,9)
    imagem = scp.morphology.grey_opening(imagem,size=9)

    # borda = utils.Canny(imagem,0.04,0.2)
    # borda = feature.canny(imagem, sigma=8)
    borda = filters.sobel(imagem)
    bor = filters.sobel(img)

    borda = bor - borda

    borda = abs(np.rint(borda))

    borda = filters.threshold_minimum(borda)
    binary_min = borda > thresh_min

    # borda = filters.median(borda, morphology.square(5))

    return borda, imagem
