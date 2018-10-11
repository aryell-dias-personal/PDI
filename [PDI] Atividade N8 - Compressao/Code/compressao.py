import numpy as np 
import os
import matplotlib.pyplot as plt 

import utils

def Huffman(imagem):
    img = utils.LerImage(imagem)

    p = utils.Probabilidade(img)

    mem = np.zeros(256)    
    count = 0

    for i in range(256):
        for j in range(i,256):
            if p[i] < p[j]:
                mem[i] = i
                aux = p[i]
                p[i] = p[j]
                p[j] = aux

    new_p = []
    new_p.append(p)

    while np.size(new_p[-1])>2:
        huff = np.zeros(np.size(new_p[-1])-1)

        for t in range(np.size(new_p[-1])-2):
            huff[t] = new_p[-1][t]
        
        huff[-1] = new_p[-1][-1]+new_p[-1][-2]
        new_p.append(huff)
        for i in range(np.size(new_p[-1])):
            for t in range(i,np.size(new_p[-1])):
                if new_p[-1][i] < new_p[-1][t]:
                    aux = new_p[-1][i]
                    new_p[-1][i] = new_p[-1][t]
                    new_p[-1][t] = aux

    # for h in range(np.shape(new_p)[0]-1,-1,-1):
    #     if h == np.shape(new_p)[0]-1:


    huffcode = new_p

    return huffcode

def Quant(imagem, bit):
    ImgOriginal = utils.LerImage(imagem)
    aux = np.shape(ImgOriginal)
    img = np.zeros(aux)

    norma = (255 - ImgOriginal)/255

    img = np.floor(bit - (bit*norma))
    
    img = img.astype(int)

    plt.imsave('../Resultados/{}_{}'.format(imagem,bit), img, cmap='gray', vmin=0,vmax=bit)

    return img


def Block(imagem):
    padImg = utils.Pad(imagem,8,8)

    size = np.shape(padImg)

    x = size[0]/8
    y = size[1]/8


# def LZW(imagem,tamanho):
#     dictionary = np.zeros(tamanho,dtype=object)
#     memoria = np.zeros(tamanho)
#     for s in range(tamanho): # cria o dicionário inicial
#         if s < 256:
#             dictionary[s] = s
#         else:
#             dictionary[s] = -1
        
#     aux = np.shape(imagem)    

#     vetor = imagem[0][0]
#     mem = 256

#     for x in range(aux[0]): # loop pra cobrir td imagem
#         for y in range(aux[1]):
#             check = 0
#             if dictionary[-1] != -1: # comecei a fazer isso aqui pra resetar as entradas do dicionário menos usadas, mas não terminei ainda
#                 temporario = np.min(memoria)
#             for t in range(tamanho): # loop pra olhar td o dicionário
#                 # print(dictionary[t], vetor)
#                 if np.array_equal(vetor,dictionary[t]): # verifica se a estrutura tá no dicionário
#                     if y+1 < aux[1]: # verifica qual pixel tá sendo analisado
#                         memoria[t] += 1 # isso é pra fazer o reset do dicionário, deixa pra lá
#                         copia = np.zeros(np.size(vetor)+1) # cria a nova estrutura para analise
#                         if np.size(vetor) > 1:
#                             for k in range(np.size(vetor)):
#                                 copia[k] = vetor[k]
#                         else:
#                             copia[0] = vetor
#                         copia[-1] = imagem[x][y+1]
#                         vetor = copia
#                         check = 1
#                         break
#                     elif x+1 < aux[0]: # a mesma coisa, só pra evitar q passe dos limites da imagem
#                         memoria[t] += 1
#                         copia = np.zeros(np.size(vetor)+1)
#                         if np.size(vetor) > 1:
#                             for k in range(np.size(vetor)):
#                                 copia[k] = vetor[k]
#                         else:
#                             copia[0] = vetor
#                         copia[-1] = imagem[x+1][0]
#                         vetor = copia
#                         check = 1
#                         break
            
#             if check == 0: # caso não se tenha a estrutura no dicionário, ela é adicionada
#                 # print(dictionary[mem-1], vetor, mem)
#                 dictionary[mem] = vetor
#                 mem += 1
#                 if y+1 < aux[1]:
#                     # print('aaaa')
#                     vetor = [imagem[x][y],imagem[x][y+1]]
#                 elif x+1 < aux[0]:
#                     # print('bbbb')
#                     vetor = [imagem[x][y],imagem[x+1][0]]

#     return dictionary


def LZW(imagem):
    #cores de 0 a 255 são mapeadas diretamente, 
    #sem necessidade de codificação   
    dictionary = {x:x for x in range(256)}  
    aux = np.shape(imagem)  
    # loop pra cobrir td imagem  
    memoria = []
    for x in range(aux[0]): 
        for y in range(aux[1]):
            valores = list(dictionary.values())
            lastKey = list(dictionary.keys())[-1]
            pixel = imagem[x][y]
            if(memoria!=[]):
                memoria.append(pixel)
                if(not valores.__contains__(memoria)):
                    dictionary[lastKey+1] = memoria
                    memoria = []
    return dictionary