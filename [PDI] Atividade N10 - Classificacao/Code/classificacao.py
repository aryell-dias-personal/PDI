import numpy as np
import cv2
import sklearn
import csv
import os
import pandas as pd
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

    # keypoints, h = surf.detectAndCompute(imagem, None)

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

    # print(h.shape)

    return h


def SVM():
    train_x_orig, train_y, test_x_orig, test_y, classes = utils.load_dataset()

    carac = []
    data = []
    
    # train_y = np.transpose(train_y)send_message

    fout = open('train.csv', 'w')

    a = ''

    for t in range(train_x_orig.shape[0]):
        carac.append(np.ravel(features(train_x_orig[t,:,:,:])))
        # carac.append(np.ravel(caracteristicas(train_x_orig[t,:,:,:])))
        
        for d in range(np.shape(carac[t])[0]):
            a += str(carac[t][d])
            a += ', '
        a += str(train_y[0][t])
        a += '\n'
        with open(os.path.join('train.csv'), 'w') as f:
            f.write(a)

    # colnames = ['I1', 'I2', 'I3', 'I4', 'I5', 'I6', 'I7', 'Class']
    # conj = pd.read_csv('train.csv',names=colnames)

    # X = conj.drop('Class', axis=1) #x contains all the features
    # y = conj['Class'] #contains the categories

    cols = list(pd.read_csv('train.csv',nrows=1))

    X = pd.read_csv('train.csv',usecols=[i for i in cols if i != 1764])
    y = pd.read_csv('train.csv',usecols=[1764])

    X_train, X_ts, y_train, y_ts = sklearn.model_selection.train_test_split(X, y, test_size = 0)

    fout.close()

    svclassifier = SVC(C=20.0, tol=1e-10, cache_size=600, kernel='rbf', class_weight='balanced')  
    svclassifier.fit(X_train,y_train)

    carac_test = []

    fin = open('test.csv', 'w')

    b = ''

    for t in range(test_x_orig.shape[0]):
        carac_test.append(np.ravel(features(test_x_orig[t,:,:,:])))
        # carac_test.append(np.ravel(caracteristicas(test_x_orig[t,:,:,:])))

        for d in range(np.shape(carac[t])[0]):
            b += str(carac[t][d])
            b += ', '
        b += str(test_y[0][t])
        b += '\n'
        with open(os.path.join('test.csv'), 'w') as f:
            f.write(b)

    # colnames = ['I1', 'I2', 'I3', 'I4', 'I5', 'I6', 'I7', 'Class']
    # conj = pd.read_csv('test.csv',names=colnames)

    # Xt = conj.drop('Class', axis=1) #x contains all the features
    # yt = conj['Class'] #contains the categories

    cols = list(pd.read_csv('test.csv',nrows=1))

    Xt = pd.read_csv('test.csv',usecols=[i for i in cols if i != 1764])
    yt = pd.read_csv('test.csv',usecols=[1764])

    fin.close()

    X_test, X_tr, y_test, y_tr = sklearn.model_selection.train_test_split(Xt, yt, test_size = 0)

    print(X_tr)

    y_pred = svclassifier.predict(X_test)

    print(y_pred)
    print(sklearn.metrics.confusion_matrix(y_test,y_pred))
    print(sklearn.metrics.classification_report(y_test,y_pred))

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