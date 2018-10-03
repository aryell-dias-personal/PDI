import numpy as np
import matplotlib.pyplot as plt

import utils

def SeguidorBorda(imagem):
    aux = np.shape(imagem)

    zeros = np.zeros(aux[1])
    x = 0
    y = 0
    borda = []

    while np.allclose(imagem[x][:],zeros):
        x += 1
    
    while imagem[x][y] == 0:
        y += 1

    B0 = [x,y]
    borda.append(B0)
    C = [x,y-1]
    B1 = aux
    pos = [[B0[0],B0[1]-1],[B0[0]-1,B0[1]-1],[B0[0]-1,B0[1]],[B0[0]-1,B0[1]+1],[B0[0],B0[1]+1],[B0[0]+1,B0[1]+1],[B0[0]+1,B0[1]],[B0[0]+1,B0[1]-1]]
    # count = 0

    while B1 != B0:
        for i in range(8):
            if C == pos[i]:
                mem = i

        flag = 0

        for t in range(mem,8):
            if imagem[pos[t][0]][pos[t][1]] == 1 and flag == 0:
                B1 = pos[t]
                if t-1 >= 0:
                    C = pos[t-1]
                else:
                    C = pos[7]
                flag = 1
        
        if flag == 0:
            for f in range(0,mem):
                if imagem[pos[f][0]][pos[f][1]] == 1 and flag == 0:
                    B1 = pos[f]
                    if f-1>=0:
                        C = pos[f-1]
                    else:
                        C = pos[7]
                    flag = 1

        borda.append(B1)
        pos = [[B1[0],B1[1]-1],[B1[0]-1,B1[1]-1],[B1[0]-1,B1[1]],[B1[0]-1,B1[1]+1],[B1[0],B1[1]+1],[B1[0]+1,B1[1]+1],[B1[0]+1,B1[1]],[B1[0]+1,B1[1]-1]]

    return borda

def ChainCode(imagem, vizinhanca):
    aux = np.shape(imagem)

    padImg = np.zeros(aux)
    size = aux

    while size[0]%10 != 0:
        padImg = np.zeros([size[0]+1,size[1]])
        size = np.shape(padImg)
    while size[1]%10 != 0:
        padImg = np.zeros([size[0],size[1]+1])
        size = np.shape(padImg)

    for i in range(aux[0]):
        for j in range(aux[1]):
            padImg[i][j] = imagem[i][j]

    grid = np.zeros([10,10])
    chain = []
    zeros = np.zeros(aux[1])
    x = 0
    y = 0

    while np.allclose(imagem[x][:],zeros):
        x += 1
    
    while imagem[x][y] == 0:
        y += 1

    borda = SeguidorBorda(padImg)

    pontos, dc = np.shape(borda)
    newborda = []
    img = np.zeros([911,881])

    for r in range(pontos):
        if borda[r][0] >= 0 and borda[r][0] < size[0]/20:
            x1 = 0
        elif borda[r][0] >= size[0]/20 and borda[r][0] < 3*size[0]/20:
            x1 =1
        elif borda[r][0] >= 3*size[0]/20 and borda[r][0] < 5*size[0]/20:
            x1 =2
        elif borda[r][0] >= 5*size[0]/20 and borda[r][0] < 7*size[0]/20:
            x1 =3
        elif borda[r][0] >= 7*size[0]/20 and borda[r][0] < 9*size[0]/20:
            x1 =4
        elif borda[r][0] >= 9*size[0]/20 and borda[r][0] < 11*size[0]/20:
            x1 =5
        elif borda[r][0] >= 11*size[0]/20 and borda[r][0] < 13*size[0]/20:
            x1 =6
        elif borda[r][0] >= 13*size[0]/20 and borda[r][0] < 15*size[0]/20:
            x1 =7
        elif borda[r][0] >= 15*size[0]/20 and borda[r][0] < 17*size[0]/20:
            x1 =8
        elif borda[r][0] >= 17*size[0]/20 and borda[r][0] < 19*size[0]/20:
            x1 =9
        elif borda[r][0] >= 19*size[0]/20:
            x1 =10
        
        if borda[r][1] >= 0 and borda[r][1] < size[1]/20:
            y1 = 0
        elif borda[r][1] >= size[1]/20 and borda[r][1] < 3*size[1]/20:
            y1 =1
        elif borda[r][1] >= 3*size[1]/20 and borda[r][1] < 5*size[1]/20:
            y1 =2
        elif borda[r][1] >= 5*size[1]/20 and borda[r][1] < 7*size[1]/20:
            y1 =3
        elif borda[r][1] >= 7*size[1]/20 and borda[r][1] < 9*size[1]/20:
            y1 =4
        elif borda[r][1] >= 9*size[1]/20 and borda[r][1] < 11*size[1]/20:
            y1 =5
        elif borda[r][1] >= 11*size[1]/20 and borda[r][1] < 13*size[1]/20:
            y1 =6
        elif borda[r][1] >= 13*size[1]/20 and borda[r][1] < 15*size[1]/20:
            y1 =7
        elif borda[r][1] >= 15*size[1]/20 and borda[r][1] < 17*size[1]/20:
            y1 =8
        elif borda[r][1] >= 17*size[1]/20 and borda[r][1] < 19*size[1]/20:
            y1 =9
        elif borda[r][1] >= 19*size[1]/20:
            y1 =10
        
        t = [x1,y1]
        img[t[0]*91][t[1]*88] = 1
        ig = 0

        for h in range(np.shape(newborda)[0]):
            if t == newborda[h]:
                ig = 1
        if ig == 0:
            newborda.append(t)

    plt.imshow(img,cmap='gray')
    plt.show()

    if vizinhanca == 8:
        for q in range(np.shape(newborda)[0]):
            pos = [[newborda[q][0],newborda[q][1]+1], [newborda[q][0]-1,newborda[q][1]+1], [newborda[q][0]-1,newborda[q][1]], [newborda[q][0]-1,newborda[q][1]-1], [newborda[q][0],newborda[q][1]-1], [newborda[q][0]+1,newborda[q][1]-1], [newborda[q][0]+1,newborda[q][1]], [newborda[q][0]+1,newborda[q][1]+1]]
            
            for h in range(0,8):
                if q < 7:
                    if pos[h] == newborda[q+1]:
                        mem = h                
                else:
                    if pos[h] == newborda[0]:
                        mem = h                
            chain.append(mem)

    # chain = 

    return chain
        

def Esqueleto(imagem):
    aux = np.shape(imagem)
    # zeros = np.zeros(aux[1])
    # x = 0
    # y = 0

    # while np.allclose(imagem[x][:],zeros):
    #     x += 1
    
    # while imagem[x][y] == 0:
    #     y += 1

    # B0 = [x,y]
    para = 0

    while para == 0:
        deletar = []
        borda = SeguidorBorda(imagem)

        plt.imshow(borda)
        plt.show()

        for s in range(np.shape(borda)[0]):
            N = 0
            T = 0
            B0 = [borda[s][0],borda[s][1]]
            pos = [[B0[0],B0[1]-1],[B0[0]-1,B0[1]-1],[B0[0]-1,B0[1]],[B0[0]-1,B0[1]+1],[B0[0],B0[1]+1],[B0[0]+1,B0[1]+1],[B0[0]+1,B0[1]],[B0[0]+1,B0[1]-1]]
            
            for i in range(-1,2):
                for j in range(-1,2):
                    if B0[0]+i >= 0 and B0[0]+i<aux[0] and B0[1]+j>=0 and B0[1]+j<aux[1]:
                        if imagem[B0[0]+i][B0[1]+j] == 1:
                            N += 1
            
            for a in range(8):
                if a > 0:
                    if pos[a][0] - pos[a-1][0] == 1 or pos[a][1] - pos[a-1][1] == 1:
                        T += 1
                else:
                    if pos[0][0] - pos[7][0] == 1 or pos[0][1] - pos[7][1] == 1:
                        T += 1
            
            if (N <= 6 or N >= 2) and T == 1 and imagem[pos[2][0]][pos[2][1]]*imagem[pos[4][0]][pos[4][1]]*imagem[pos[6][0]][pos[6][1]] == 0 and imagem[pos[0][0]][pos[0][1]]*imagem[pos[4][0]][pos[4][1]]*imagem[pos[6][0]][pos[6][1]] == 0:
                deletar.append(B0)

        for g in range(np.shape(deletar)[0]):
            x = deletar[g][0]
            y = deletar[g][1]
            imagem[x][y] = 0

        borda = SeguidorBorda(imagem)

        for s in range(np.shape(borda)[0]):
            N = 0
            T = 0
            B0 = [borda[s][0],borda[s][1]]
            pos = [[B0[0],B0[1]-1],[B0[0]-1,B0[1]-1],[B0[0]-1,B0[1]],[B0[0]-1,B0[1]+1],[B0[0],B0[1]+1],[B0[0]+1,B0[1]+1],[B0[0]+1,B0[1]],[B0[0]+1,B0[1]-1]]
            
            for i in range(-1,2):
                for j in range(-1,2):
                    if B0[0]+i >= 0 and B0[0]+i<aux[0] and B0[1]+j>=0 and B0[1]+j<aux[1]:
                        if imagem[B0[0]+i][B0[1]+j] == 1:
                            N += 1
            
            for a in range(8):
                if a > 0:
                    if pos[a][0] - pos[a-1][0] == 1 or pos[a][1] - pos[a-1][1] == 1:
                        T += 1
                else:
                    if pos[0][0] - pos[7][0] == 1 or pos[0][1] - pos[7][1] == 1:
                        T += 1
            
            if (N <= 6 or N >= 2) and T == 1 and imagem[pos[2][0]][pos[2][1]]*imagem[pos[4][0]][pos[4][1]]*imagem[pos[0][0]][pos[0][1]] == 0 and imagem[pos[0][0]][pos[0][1]]*imagem[pos[2][0]][pos[2][1]]*imagem[pos[6][0]][pos[6][1]] == 0:
                deletar.append(B0)

        for g in range(np.shape(deletar)[0]):
            x = deletar[g][0]
            y = deletar[g][1]
            imagem[x][y] = 0

        print(deletar)

        if np.size(deletar) == 0:
            para = 1

    return imagem