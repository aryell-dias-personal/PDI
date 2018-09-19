import matplotlib.image as mpimg
import numpy as np

def P(regiao):
    (x,y) = np.shape(regiao)
    retornoAux = np.abs(regiao-np.mean(regiao))<=2*np.std(regiao)
    return  (np.sum(retornoAux)/(x*y)>=0.8)

# leitura da imagem
def LerImagem(nome):
    imagem = mpimg.imread(nome)
    return imagem

def increment(value, initial, limit):
    if(value + initial > limit or value + initial < 0):
        return initial
    else:
        return value + initial

# normalização da imagem
def Normalizar(imagem):
    mini = np.min(imagem)
    maxi = np.max(imagem)
    imagem = imagem - mini
    # diferença entre a imagem e o mínimo vezes 
    # 255 dividido pela diferença entre o máximo
    # e o minimo
    imagem = imagem*255/(maxi-mini)
    return imagem


def Histograma(imagem):
    aux = np.shape(imagem)
    count = np.zeros(256)
    mem = 0

    for x in range(aux[0]):
        print(x)
        for y in range(aux[1]):
            mem = imagem[x][y]
            count[mem] = count[mem] + 1
    return count

def Threshold(imagem):
    aux = np.shape(imagem)

    # caso a imagem possua mais de dois shapes (duas dimensões)
    # ignoramos algumas coordenadas
    if np.size(aux) > 2:
        imagem = imagem[:][:][1]
        aux = np.shape(imagem)

    # imagem preenchida apenas com zeros
    BinImg = np.zeros(aux)

    for x in range(aux[0]):
        for y in range(aux[1]):
            if imagem[x][y] > 0.33*np.max(imagem):
                # se maior o máximo da imagem é 1
                BinImg[x][y] = 1
            else:
                # se não é 0
                BinImg[x][y] = 0

    return BinImg
    
# aparentemente não surti efeito com as imagens que precisam ser divididas em regiões
# (a águia e a melancia), nenhuma das duas passa pela função P como True com facilidade,
# não dividindo a imagem original e regiões menores
def dividiRegiao(regiao):
    aux = np.shape(regiao)

    if np.size(aux) > 2:
        regiao = regiao[:,:,0]
        aux = np.shape(regiao) 

    regioes = [regiao]
    # percorrendo a imagem original
    if((not utils.P(regiao)) and aux[0]/2>1 and aux[1]/2>1):
        regioes = dividiRegiao(regiao[0:int(aux[0]/2), 0:int(aux[1]/2)]) +\
            dividiRegiao(regiao[int(aux[0]/2):, 0:int(aux[1]/2)])+\
            dividiRegiao(regiao[0:int(aux[0]/2), int(aux[1]/2):])+\
            dividiRegiao(regiao[int(aux[0]/2):, int(aux[1]/2):])
    return regioes

# def unirRegioes(regioes):
#   TODO