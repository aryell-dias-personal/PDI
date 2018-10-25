import numpy as np
import cv2
import sklearn
from sklearn.svm import SVC
import matplotlib.pyplot as plt

# import create_data
import utils

def caracteristicas(imagem):

    img = utils.rgb2gray(imagem)

    aux = np.shape(img)

    Mom = np.zeros([4,4])

    for p in range(4):
        for q in range(4):
            for x in range(aux[0]):
                for y in range(aux[1]):
                    Mom[p][q] += (x**p)*(y**q)*img[x][y]

    x_barra = Mom[1][0]/Mom[0][0]
    y_barra = Mom[0][1]/Mom[0][0]

    Mi = np.zeros([4,4])
    Mi[0][0] = Mom[0][0]
    Mi[0][1] = 0
    Mi[1][0] = 0
    Mi[1][1] = Mom[1][1] - x_barra*Mom[0][1]
    Mi[2][0] = Mom[2][0] - x_barra*Mom[1][0]
    Mi[0][2] = Mom[0][2] - y_barra*Mom[0][1]
    Mi[2][1] = Mom[2][1] - 2*x_barra*Mom[1][1] - y_barra*Mom[2][0] + 2*(x_barra**2)*Mom[0][1]
    Mi[1][2] = Mom[1][2] - 2*y_barra*Mom[1][1] - x_barra*Mom[0][2] + 2*(y_barra**2)*Mom[1][0]
    Mi[3][0] = Mom[3][0] - 3*x_barra*Mom[2][0] + 2*(x_barra**2)*Mom[1][0]
    Mi[0][3] = Mom[0][3] - 3*y_barra*Mom[0][2] + 2*(y_barra**2)*Mom[0][1]

    Ni = np.zeros([4,4])

    for p in range(4):
        for q in range(4):
            Ni[p][q] = Mi[p][q]/(Mi[0][0]**(1+(p+q)/2))

    Hu = np.zeros(7)

    Hu[0] = Ni[2][0] + Ni[0][2]

    Hu[1] = (Ni[2][0] - Ni[0][2])**2 + 4*Ni[1][1]**2

    Hu[2] = (Ni[3][0] - 3*Ni[1][2])**2 + (3*Ni[2][1] - Ni[0][3])**2

    Hu[3] = (Ni[3][0] + Ni[1][2])**2  + (Ni[2][1] + Ni[0][3])**2

    Hu[4] = (Ni[3][0] - 3*Ni[1][2])*(Ni[3][0] + Ni[1][2])*((Ni[3][0] + Ni[1][2])**2 - 3*(Ni[2][1] + Ni[0][3])**2) + (3*Ni[2][1] - Ni[0][3])*(Ni[2][1] + Ni[0][3])*(3*(Ni[3][0] + Ni[1][2])**2 - (Ni[2][1] + Ni[0][3])**2)

    Hu[5] = (Ni[2][0] - Ni[0][2])*((Ni[3][0]+Ni[1][2])**2 - (Ni[2][1] + Ni[0][3])**2) + 4*Ni[1][1]*(Ni[3][0] + Ni[1][2])*(Ni[2][1] + Ni[0][3])

    Hu[6] = (3*Ni[2][1] - Ni[0][3])*(Ni[0][3] + Ni[1][2])*((Ni[3][0] + Ni[1][2])**2 - 3*(Ni[2][1] + Ni[0][3])**2) - (Ni[3][0] - 3*Ni[1][2])*(Ni[2][1] + Ni[0][3])*(3*(Ni[3][0] + Ni[1][2])**2 - (Ni[2][1] + Ni[0][3])**2)

    return Hu

def features(imagem):
    # sift = cv2.xfeatures2d.SIFT_create()
    # surf = cv2.xfeatures2d.SURF_create()

    # keypoints, descriptors = sift.detectAndCompute(imagem, None)

    winSize = (64,64)
    blockSize = (16,16)
    blockStride = (8,8)
    cellSize = (8,8)
    nbins = 9
    derivAperture = 1
    winSigma = 4.
    histogramNormType = 0
    L2HysThreshold = 2.0000000000000001e-01
    gammaCorrection = 0
    nlevels = 64

    hog = cv2.HOGDescriptor(winSize,blockSize,blockStride,cellSize,nbins,derivAperture,winSigma,histogramNormType,L2HysThreshold,gammaCorrection,nlevels)
    h = hog.compute(imagem)

    return h


def rede():
    train_x_orig, train_y, test_x_orig, test_y, classes = utils.load_dataset()

    carac = []
    # train_y = sklearn.utils.validation.column_or_1d(np.transpose(train_y),warn=True)
    # train_y = np.transpose(train_y)

    for t in range(train_x_orig.shape[0]):
        carac.append(np.ravel(features(train_x_orig[t,:,:,:])))

    svclassifier = SVC(kernel='sigmoid')  
    svclassifier.fit(carac,train_y.ravel())

    carac_test = []

    for t in range(test_x_orig.shape[0]):
        carac_test.append(np.ravel(features(test_x_orig[t,:,:,:])))

    y_pred = svclassifier.predict(carac_test)

    print(sklearn.metrics.confusion_matrix(test_y.ravel(),y_pred))
    print(sklearn.metrics.classification_report(test_y.ravel(),y_pred))




# def MLP():
#     train_x_orig, train_y, test_x_orig, test_y, classes = utils.load_dataset()

#     carac = []

#     for t in range(train_x_orig.shape[0]):
#         carac.append(caracteristicas(train_x_orig[t,:,:,:]))

#     interna = np.zeros(5)
#     peso1 = np.random.uniform(-1,1,[7,5])

#     for t in range(train_x_orig.shape[0]):
#         for d in range(7):
#             for q in range(5):
#                 interna[q] += peso1[q]*carac[t][d]
#         for u in range(5):
#             ativa = 1/(1+np.exp(-(interna[u]+1)/2))
#             if ativa >= 