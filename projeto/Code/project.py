import numpy as np
import scipy
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

def teste(imagem):
    # laplace = filters.laplace(frangi)
    # selem = morphology.disk(5)
    # print(imagem)
    # median = filters.median(color.rgb2gray(imagem),selem=selem)
<<<<<<< HEAD
    borda,_ = projeto_canny(color.rgb2gray(imagem))
    lines = probabilistic_hough_line(borda,line_length=150, line_gap=150, threshold=100)
=======

    borda,_ = projeto_canny(color.rgb2gray(imagem))
    lines = probabilistic_hough_line(borda, threshold=80, line_length=50, line_gap=40)
>>>>>>> 6680b227f7e291a7a7c55cb3c9d1a3b1569e0a2b
    imagem = exposure.equalize_adapthist(filters.gaussian(imagem))
    laplace = filters.laplace(imagem)
    gray = color.rgb2gray(laplace)
    frangi = filters.frangi(gray)
    # prewitt = filters.prewitt(frangi)
    # prewitt = np.median(prewitt)/10 < prewitt
    # retas = utils.extraiRetas(prewitt,130)
    # lines = probabilistic_hough_line(prewitt,threshold=10,line_length=300,line_gap=1)
<<<<<<< HEAD
    return frangi, lines, borda
=======
    # lines = []

    return frangi, lines, borda 

def rodrigo(imagem):
    # img = scp.morphology.grey_opening(imagem,size=17)
    # close = scp.morphology.grey_closing(img,size=7)

    # dila = scp.morphology.grey_dilation(img,size=7)

    # retorno = abs(dila - imagem)

    # retorno = projeto_canny(retorno)[0]

    # fd,retorno = feature.hog(img, orientations=8, pixels_per_cell=(16, 16),cells_per_block=(1, 1), visualize=True, multichannel=True)

    # retorno = exposure.rescale_intensity(retorno,in_range=(0,10))

    img = 1 - (np.max(imagem)-imagem)/(np.max(imagem)-np.min(imagem))

    high_contr = exposure.equalize_adapthist(img)

    # filtered_img = filters.median(high_contr,morphology.square(3))
    filtered_img = scp.morphology.grey_opening(high_contr,size=17)
    filtered_img = scp.morphology.grey_closing(filtered_img,size=7)

    enhanced_img = abs(high_contr - filtered_img)

    # edges = feature.canny(enhanced_img, sigma=1.5)
    # edges = filters.sobel(enhanced_img)
    edges = cluster.KMeans(n_clusters=2,random_state=0).fit(enhanced_img)
    edges.labels_
    edges = np.float(edges)

    return edges
>>>>>>> 6680b227f7e291a7a7c55cb3c9d1a3b1569e0a2b
