import numpy as np
import scipy
import scipy.ndimage as scp
import cv2
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

    # imagem = scp.morphology.grey_erosion(borda,size=5)
    imagem = scp.morphology.grey_closing(borda, size=5)
    return imagem

def projeto_rodrigo(imagem):
    borda = feature.canny(imagem,sigma=1)

    block_size = 55
    img = filters.threshold_adaptive(imagem,block_size)
    img = morphology.skeletonize(img)

    return borda, img

# detecta rejunte
def detecta_rejunte(imagem):
    # gray = cv2.cvtColor
    # (imagem,cv2.COLOR_BGR2GRAY)
    # ret, thresh = cv2.threshold(gray,0,255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    # return ret, thresh
    imgf = scp.gaussian_filter(imagem,1.0)
    labeled, nr_objects = scp.label(imgf > (np.min(imagem)+np.max(imagem))/2)
    # labeled = labeled > np.min(labeled)
    # labeled = morphology.erosion(labeled)
    print(nr_objects)
    return labeled

# funciona pra 19
def projeto_aryell(imagem):
    aux = np.shape(imagem)
    retorno = np.zeros(aux)
    
    naoRejunte = detecta_rejunte(imagem)
    bordaDilatada = projeto_canny(imagem)

    for a in range(aux[0]-1):
        for b in range(aux[1]-1):
            retorno[a][b] = bordaDilatada[a][b] and naoRejunte[a][b]

    retorno = scp.morphology.binary_erosion(retorno)

    return retorno