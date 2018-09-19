import numpy as np
import utils

# otsu para duas classes
def otsu(imagem, k):
    aux = np.shape(imagem)
    if np.size(aux) > 2:
        imagem = imagem[:,:,0]
        aux = np.shape(imagem) 
    hist = utils.Histograma(imagem)
    prob = hist/np.sum(hist)
    probAcumulada = np.sum(prob[:k])
    medAcumulada = np.sum(x * y for x, y in zip(range(k), hist[:k])) / np.sum(hist[:k])
    mediaGlobal = np.mean(imagem)
    variancia = ((mediaGlobal*probAcumulada-medAcumulada)**2)/(probAcumulada*(1-probAcumulada))
    print(variancia)
    maximo = np.max(variancia)
    i = 0;
    kOtimo = 0;
    while(variancia.count(maximo)):
        i += 1
        aux = variancia.index(maximo)
        kOtimo = kOtiom + aux
        variancia = variancia[aux+1:]
    kOtimo = kOtimo/i
    mediaSeparatibilidade = variancia[kOtimo]/np.var(imagem)
    for x in aux[0]:
        for y in aux[1]:
            imagem[x][y] = 1 if imagem[x][y]>kOtimo else 0
    return imagem
            
def limirizacaoLocal(imagem, tipoMedia = 'local', n = 20, a = 0, b = 1 ): 
    limit = int(n/2)
    aux = np.shape(imagem)
    
    if np.size(aux) > 2:
        imagem = imagem[:,:,0]
        aux = np.shape(imagem) 

    segmImg = np.zeros(aux)
    for j in range(0, aux[0]):
        for i in range(0, aux[1]):
            area = imagem[utils.increment(-limit,j,aux[0]):utils.increment(limit,j,aux[0]), utils.increment(-limit,i,aux[1]):utils.increment(limit,i,aux[1])]
            Txy = a*np.var(area) + b*(np.mean(area) if tipoMedia == 'local' else np.mean(imagem))
            segmImg[j][i] = 1 if imagem[j][i] > Txy else 0
    return segmImg

# def dividirFundirRegioes(imagem)
#   TODO
#   usará os metodos dividiRegiao e uniRegiao em utils