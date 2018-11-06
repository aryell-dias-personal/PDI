import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

def kernel(kernel, imagemOriginal):
    limit = int(kernel.__len__()/2)
    X = imagemOriginal.shape[0]
    Y = imagemOriginal.shape[1]
    imagemReturn = [[]]
    for j in range(limit, int(X)-limit) :
        for i in range(limit, int(Y)-limit):
            pixel = 0
            for l in range(-limit,limit) :
                for k in range(-limit,limit) :
                    pixel += kernel[int(k+limit)][int(l+limit)]*imagemOriginal[k+j][l+i]
            imagemReturn[j-limit] = imagemReturn[j-limit] + [pixel/(kernel.__len__()**2)]
        if(j<X-limit-1):
            imagemReturn += [[]]
    return np.array(imagemReturn, dtype=np.uint8)

def mediana(side, imagemOriginal):
    limit = int(side/2)
    X = imagemOriginal.shape[0]
    Y = imagemOriginal.shape[1]
    imagemReturn = [[]]
    for j in range(limit, int(X)-limit) :
        for i in range(limit, int(Y)-limit):
            imagemReturn[j-limit] = imagemReturn[j-limit] + [np.median(imagemOriginal[j-limit:j+limit, i-limit:i+limit])]
        if(j<X-limit-1):
            imagemReturn += [[]]
    return np.array(imagemReturn, dtype=np.uint8)

def lerImagem(nome):
    imagem = mpimg.imread(nome)
    return imagem

kernel = np.array([
    [1,1,1],
    [1,1,1],
    [1,1,1]
])

plt.imshow(mediana(40, lerImagem('./Imagens/Suavizar_(2).jpg')), cmap='gray')
plt.show();



