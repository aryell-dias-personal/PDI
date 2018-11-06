import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

def ImpulseNoise(imagem,Pl,Ph=255):
    imagem = np.mean(imagem,-1)
    aux = np.shape(imagem)
    print(aux)
    ImgNoise = np.zeros(aux)

    for x in range(aux[0]):
        for y in range(aux[1]):
            rand = np.random.randint(0,100)
            if rand <= Pl:
                ImgNoise[x][y] = 0
            elif rand >= Ph:
                # name = 'bipolar'
                ImgNoise[x][y] = 255
            else:
                ImgNoise[x][y] = imagem[x][y]

    return ImgNoise

def GaussianNoise(imagem):
    imagem = np.mean(imagem,-1)
    mean = 10
    std = 30

    aux = np.shape(imagem)
    ImgGaussian = np.zeros(aux)
    u1 = np.zeros(aux)
    u2 = np.zeros(aux)
    z0 = np.zeros(aux)

    for x in range(aux[0]):
        for y in range(aux[1]):
            # z = 100*np.random.rand()
            u1[x][y] = np.random.rand()
            u2[x][y] = np.random.rand()
            z0[x][y] = np.sqrt(-2*np.log(u1[x][y]))*np.cos(2*np.pi*u2[x][y])
            # prob = np.exp(-((z-mean)**2)/(2*(std**2)))/(std*np.sqrt(2*np.pi))
            # if prob > 
    
    z0 = std*((z0-np.mean(z0))/np.std(z0)) + mean
    
    ImgGaussian = imagem + z0

    mini = np.min(ImgGaussian)
    ImgGaussian = ImgGaussian - mini
    maxi = np.max(ImgGaussian)

    for x in range(aux[0]):
        for y in range(aux[1]):
            ImgGaussian[x][y] = np.rint(ImgGaussian[x][y]*255/(maxi-mini))

    return ImgGaussian

