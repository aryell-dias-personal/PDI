import numpy as np
import utils

def limirizacaoLocal(imagem, tipoMedia = 'local', n = 20, a = 0 , b = 0.5 ): 
    limit = int(n/2)
    aux = np.shape(imagem)

    if np.size(aux) > 2:
        imagem = imagem[:][:][0]
        aux = np.shape(imagem)
        
    segmImg = np.zeros(aux)
    for j in range(0, aux[0]):
        for i in range(0, aux[1]):
            area = imagem[utils.increment(-limit,j,aux[0]):utils.increment(limit,j,aux[0]), utils.increment(-limit,i,aux[1]):utils.increment(limit,i,aux[1])]
            Txy = a*np.var(area) + b*(np.mean(area) if tipoMedia == 'local' else np.mean(imagem))
            segmImg[j][i] = 1 if imagem[j][i] > Txy else 0
    return segmImg