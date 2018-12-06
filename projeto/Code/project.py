import numpy as np
import scipy
import matplotlib.pyplot as plt 
import scipy.ndimage as scp
import cv2

from skimage import feature, filters, morphology, color, util, exposure, segmentation
from skimage.measure import find_contours
from skimage.transform import hough_line, hough_line_peaks, probabilistic_hough_line
from sklearn import cluster
import utils


def projeto_sobel(imagem):
    
    imagem = 1 - (np.max(imagem)-imagem)/(np.max(imagem)-np.min(imagem))

    img = filters.rank.minimum(imagem, morphology.square(7)) 

    imagem = scp.morphology.grey_opening(img,size=7) 
    imagem = scp.morphology.grey_closing(imagem,size=5)

    borda = feature.canny(imagem,sigma=1) 

    borda = scp.morphology.binary_closing(borda) 

    return borda,imagem

def projeto_canny(imagem):

    img = scp.morphology.grey_closing(imagem,size=17) 
    img = scp.morphology.grey_opening(img,size=17)

    imagem = imagem - img 

    img = 1 - (np.max(imagem)-imagem)/(np.max(imagem)-np.min(imagem))

    borda = feature.canny(imagem,sigma=1) 

    return borda, imagem

def canny_por_canal(imagem):
    red = imagem[:,:,0]
    green = imagem[:,:,1] 
    blue = imagem[:,:,2]

    canny_r = feature.canny(red,sigma=1)
    canny_r = scp.morphology.binary_closing(canny_r,structure=np.ones((3,3)))
    canny_r = scp.morphology.binary_opening(canny_r, structure=np.ones((3,3)))

    canny_g = feature.canny(green,sigma=1)
    canny_g = scp.morphology.binary_closing(canny_g,structure=np.ones((3,3)))
    canny_g = scp.morphology.binary_opening(canny_g,structure=np.ones((3,3)))

    canny_b = feature.canny(blue,sigma=1)
    canny_b = scp.morphology.binary_closing(canny_b,structure=np.ones((3,3)))
    canny_b = scp.morphology.binary_opening(canny_b,structure=np.ones((3,3)))

    a,b,c = np.shape(imagem)
    result = np.zeros((a,b))

    for x in range(np.shape(imagem)[0]):
        for y in range(np.shape(imagem)[1]):
            if canny_r[x][y] and canny_b[x][y]:
                result[x][y] = 1
            elif canny_r[x][y] and canny_g[x][y]:
                result[x][y] = 1
            elif canny_b[x][y] and canny_g[x][y]:
                result[x][y] = 1
            else:
                result[x][y] = 0

    return canny_r, canny_g, canny_b, result

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
    
def projeto_aryell_2(imagem):
    aux = np.shape(imagem)
    retorno = np.zeros(aux)
    
    # extrai borda
    borda,_ = projeto_canny(imagem)
    # o threshold parece mudar para cada imagem
    retas = utils.extraiRetas(borda,100)
    # cria imagem de retorno apartir das bordas e das retas
    for a in range(aux[0]-1):
        for b in range(aux[1]-1):
            retorno[a][b] = borda[a][b] and (not retas[a][b])
    
    return retorno, borda, retas, imagem 

# laplace = filters.laplace(frangi)
    # selem = morphology.disk(5)
    # print(imagem)
    # median = filters.median(color.rgb2gray(imagem),selem=selem)
    # high_contr = exposure.equalize_adapthist(imagem)
    # filtered_img = scp.morphology.grey_opening(high_contr,size=17)
    # filtered_img = scp.morphology.grey_closing(filtered_img,size=7)
    # imagem = abs(high_contr - filtered_img)
    # borda,_ = projeto_canny(color.rgb2gray(imagem))

def teste1(imagem):
    imagem = color.rgb2gray(imagem)
    # limba e aumenta o contraste daimagem
    imagem = filters.gaussian(exposure.adjust_gamma(imagem,3,3))
    # destaca os detalhes
    imagem = imagem + filters.laplace(imagem)
    filtrada = filters.roberts(imagem)
    # erodi e dilata
    # erodida = morphology.erosion(filtrada)
    # dilatada = morphology.dilation(erodida)
    # segmenta
    tresh = filters.threshold_otsu(filtrada)
    result = filtrada > tresh
    # extrai retas
    lines = probabilistic_hough_line(result, threshold=80, line_length=50, line_gap=40)

    return result, lines, filtrada 

def teste(imagem):
    imagem = color.rgb2gray(imagem)
    # limpa e aumenta o contraste da imagem
    
    imagem = filters.gaussian(exposure.adjust_gamma(imagem,3,3))
    # destaca os detalhes
    lowpass = ndimage.gaussian_filter(imagem, 3)
    gauss_highpass = imagem - lowpass
    imagem = imagem + filters.laplace(imagem)
    filtrada = filters.sobel(imagem)
    # segmenta
    tresh = filters.threshold_otsu(filtrada)
    segmentada = filtrada > tresh

    # close
    closed = morphology.binary_dilation(segmentada)
    # esqueleto
    esqueleto = morphology.skeletonize(closed)
    # extrai retas
    lines = probabilistic_hough_line(esqueleto, threshold=80, line_length=50, line_gap=40)

    return segmentada, lines, gauss_highpass 

# prewitt = filters.prewitt(frangi)
    # prewitt = np.median(prewitt)/10 < prewitt
    # retas = utils.extraiRetas(prewitt,130)
    # lines = probabilistic_hough_line(prewitt,threshold=10,line_length=300,line_gap=1)
    # lines = []

def rodrigo(imagem):
    # img = scp.morphology.grey_opening(imagem,size=17)
    # close = scp.morphology.grey_closing(img,size=7)

    # dila = scp.morphology.grey_dilation(img,size=7)

    # retorno = abs(dila - imagem)

    # retorno = projeto_canny(retorno)[0]

    # fd,retorno = feature.hog(img, orientations=8, pixels_per_cell=(16, 16),cells_per_block=(1, 1), visualize=True, multichannel=True)

    # retorno = exposure.rescale_intensity(retorno,in_range=(0,10))

    img = 1 - (np.max(imagem)-imagem)/(np.max(imagem)-np.min(imagem))
    # filtered_img = filters.median(high_contr,morphology.square(3))



    high_contr = exposure.equalize_adapthist(img)
    filtered_img = scp.morphology.grey_opening(high_contr,size=17)
    filtered_img = scp.morphology.grey_closing(filtered_img,size=7)
    enhanced_img = abs(high_contr - filtered_img)

    edges = feature.canny(enhanced_img, sigma=1.5)
    # edges = filters.sobel(enhanced_img)
    aaa = clean_up(edges)

    return edges, aaa

def clean_up(imagem):
    s = np.ones([3,3])
    labels = scipy.ndimage.label(imagem,s)

    conta = utils.Histograma(labels[0])    

    copia = np.copy(conta)

    mem = np.zeros(np.shape(conta)[0])

    for i in range(np.shape(conta)[0]):
        for j in range(i,np.shape(conta)[0]):
            if conta[i] < conta[j]:
                aux = conta[j]
                conta[j] = conta[i]
                conta[i] = aux

    for i in range(np.shape(conta)[0]):
        for t in range(np.shape(conta)[0]):
            if conta[i] == copia[t] and (t not in mem):
                mem[i] = t

    cortados = np.zeros(np.shape(conta)[0] - int(np.rint(0.3*np.shape(conta)[0])))

    for h in range(int(np.rint(0.3*np.shape(conta)[0])),np.shape(conta)[0]):
        cortados[h-int(np.rint(0.3*np.shape(conta)[0]))] = mem[h]

    clean = np.zeros(np.shape(imagem))

    for x in range(np.shape(imagem)[0]):
        for y in range(np.shape(imagem)[1]):
            if labels[0][x][y] not in cortados:
                clean[x][y] = 1

    # print(cortados)
    # plt.plot(conta)
    # plt.show()

    return clean
