import numpy as np
import scipy
import scipy.ndimage as scp
import cv2
from skimage import feature, filters, morphology
from skimage.transform import hough_line, hough_line_peaks, probabilistic_hough_line
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

def detecta_rejunte(imagem):
    # gray = cv2.cvtColor
    # (imagem,cv2.COLOR_BGR2GRAY)
    # ret, thresh = cv2.threshold(gray,0,255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    # return ret, thresh
    imgf = scp.gaussian_filter(imagem,1.0)
    labeled, nr_objects = scp.label(imgf > (np.min(imagem)+np.max(imagem))/2)
    labeled = labeled > np.min(labeled)
    labeled = morphology.erosion(scp.morphology.binary_erosion(morphology.erosion(labeled)))
    # print(nr_objects)
    return labeled


def projeto_hough(image):
    edges, image = projeto_canny(image)
    lines = cv2.HoughLines(np.array(edges, dtype=np.uint8),1,np.pi/180,150)
    retorno = np.zeros(np.shape(image))
    if(not lines is None):
        for things in lines:
            for rho,theta in things:
                a = np.cos(theta)
                b = np.sin(theta)
                x0 = a*rho
                y0 = b*rho
                x1 = int(x0 + 1000*(-b))
                y1 = int(y0 + 1000*(a))
                x2 = int(x0 - 1000*(-b))
                y2 = int(y0 - 1000*(a))
                retorno = cv2.line(retorno,(x1,y1),(x2,y2),(255,0,0),2)
    return retorno

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
''
def projeto_aryell_2(imagem):
    aux = np.shape(imagem)
    retorno = np.zeros(aux)
    borda = projeto_canny(imagem)[0]
    rejunte = scp.morphology.binary_dilation(projeto_hough(imagem))
    print(rejunte)
    for a in range(aux[0]-1):
        for b in range(aux[1]-1):
            retorno[a][b] = borda[a][b] and not rejunte[a][b]
    return retorno, borda, rejunte, imagem