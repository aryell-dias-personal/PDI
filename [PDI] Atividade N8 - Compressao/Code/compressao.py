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
