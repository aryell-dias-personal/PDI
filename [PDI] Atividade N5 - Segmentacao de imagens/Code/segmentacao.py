import numpy as np
import utils
import filters

# otsu para duas classes
def otsu(imagem):
    # informações pertinentes
    aux = np.shape(imagem)
    imagemRetorno = np.zeros(aux)
    if np.size(aux) > 2:
        imagem = imagem[:,:,0]
        aux = np.shape(imagem) 
    hist = utils.Histograma(imagem)
    prob = hist/np.sum(hist)
    # k otimo e a variancia que serão utilizados nos calculos
    kOtimo = 0
    variancia = 0
    i = 1
    for k in range(1,254):
        probAcumulada = np.sum(prob[:k])
        medAcumulada = np.sum(j * i for j, i in zip(range(k), hist[:k])) / np.sum(hist[:k])
        mediaGlobal = np.mean(imagem)
        q = probAcumulada*(1-probAcumulada)
        if q == 0 or q == 1:
            break;
        auxfor = ((mediaGlobal*probAcumulada-medAcumulada)**2)/q
        if auxfor > variancia: 
            kOtimo = k
            variancia = auxfor
        elif auxfor == variancia:
            kOtimo = k + kOtimo
            variancia = auxfor
    kOtimo = kOtimo/i
    # formando a imagem binaria
    for x in range(aux[0]):
        for y in range(aux[1]):
            if imagem[x][y]>kOtimo:
                imagemRetorno[x][y] = 1
            else: 
                imagemRetorno[x][y] = 0
    return imagemRetorno
            
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