import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

# imagem original
imagemOrignal = mpimg.imread('./Images/Agucar_(5).jpg')
if(len(imagemOrignal.shape)>2):
    imagemOrignal = imagemOrignal[...,0]
def getMoveCenter(imagemOrignal):
    shape = imagemOrignal.shape
    (ylen, xlen) = shape
    (x,y) = np.meshgrid(range(xlen), range(ylen))
    moveCenterOriginal = (-1)**(x+y)
    return moveCenterOriginal

# imagem na frequência
def getImageFrequence(imagemOrignal, moveCenterOriginal):
    imagemFrequencia = np.fft.fft2(imagemOrignal*moveCenterOriginal)
    return imagemFrequencia;

def gaussianFilter(ylen, xlen, cut):
    (x,y) = np.meshgrid(range(xlen), range(ylen))
    gaussian = 1-np.exp(-((x-xlen/2)**2+(y-ylen/2)**2)/(cut**2))
    return gaussian

def idealFilter(ylen, xlen, cut):
    (x,y) = np.meshgrid(range(xlen), range(ylen))
    ideal = (((x-xlen/2)**2+(y-ylen/2)**2))**0.5 <= cut
    return np.array(ideal, dtype='uint8')
    
def butterWorthFilter(ylen, xlen, cut, n):
    (x,y) = np.meshgrid(range(xlen), range(ylen))
    ideal = 1-1/(1+(((x-xlen/2)**2+(y-ylen/2)**2)/cut)**(2*n))
    return ideal

# processo
moveCenterOriginal = getMoveCenter(imagemOrignal)
imagemFrequenciaPura = getImageFrequence(imagemOrignal, moveCenterOriginal)
(ylen, xlen) = imagemFrequenciaPura.shape
imagemFrequenciaResult = butterWorthFilter(ylen,xlen,15,35)*imagemFrequenciaPura
moveCenterFrequencia = getMoveCenter(imagemFrequenciaResult)
imagemResultado = moveCenterFrequencia*np.fft.ifft2(imagemFrequenciaResult).real+imagemOrignal

# plot
(fig, (ax1, ax2, ax3)) = plt.subplots(1,3)
ax1.imshow(imagemOrignal, cmap='gray')
ax3.imshow(np.log(np.abs(imagemFrequenciaPura)), cmap='gray')
ax2.imshow(imagemResultado, cmap='gray', vmin=0,vmax=255)
plt.show()
