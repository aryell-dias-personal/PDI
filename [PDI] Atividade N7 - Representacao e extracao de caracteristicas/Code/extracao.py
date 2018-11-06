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
            if pos[t][0] >= 0 and pos[t][0] < aux[0] and pos[t][1] >= 0 and pos[t][1] < aux[1]:
                if imagem[pos[t][0]][pos[t][1]] == 1 and flag == 0:
                    B1 = pos[t]
                    if t-1 >= 0:
                        C = pos[t-1]
                    else:
                        C = pos[7]
                    flag = 1
        
        if flag == 0:
            for f in range(0,mem):
                if pos[f][0] >= 0 and pos[f][0] < aux[0] and pos[f][1] >= 0 and pos[f][1] < aux[1]:
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

def ChainCode(imagem, vizinhanca,g,l):
    aux = np.shape(imagem)

    padImg = np.zeros(aux)
    size = aux

    while size[0]%g != 0:
        padImg = np.zeros([size[0]+1,size[1]])
        size = np.shape(padImg)
    while size[1]%l != 0:
        padImg = np.zeros([size[0],size[1]+1])
        size = np.shape(padImg)

    if (aux[0]-size[0])%2 > 0:
        complemento = 1 
    else:
        complemento = 0

    if (aux[1]-size[1])%2 > 0:
        comp = 1 
    else:
        comp = 0
    
    for i in range(int(np.floor((size[0]-aux[0])/2)),int(size[0]-np.floor((size[0]-aux[0])/2)-complemento)):
        for j in range(int(np.floor((size[1]-aux[1])/2)),int(size[1]-np.floor((size[1]-aux[1])/2)-comp)):
            padImg[i][j] = imagem[i-int(np.floor((size[0]-aux[0])/2))][j-int(np.floor((size[1]-aux[1])/2))]

    zeros = np.zeros(aux[1])
    x = 0
    y = 0

    while np.allclose(imagem[x][:],zeros):
        x += 1
    
    while imagem[x][y] == 0:
        y += 1
    
    dim = np.shape(padImg)
    grid = np.zeros([g,l])

    if dim[0]%2 > 0:
        xcomp = 1 
    else:
        xcomp = 0

    if dim[1]%2 > 0:
        ycomp = 1 
    else:
        ycomp = 0

    for u in range(g):
        for v in range(l):
            for t in range(u*g-int(np.floor(dim[0]/(2*g))),u*g+int(np.floor(dim[0]/(2*g)))-xcomp):
                for k in range(v*l-int(np.floor(dim[1]/(2*l))),v*l+int(np.floor(dim[1]/(2*l)))-ycomp):
                    if t+u-xcomp >= 0 and t+u-xcomp < dim[0] and k+v-ycomp >= 0 and k+v-ycomp < dim[1]:
                        if padImg[t+u-xcomp][k+v-ycomp] == 1:
                            grid[u][v] = 1
    
    plt.imshow(grid,cmap='gray')
    plt.show()

    newborda = SeguidorBorda(grid)
    chain = []
    cope = []

    if vizinhanca == 8:
        for q in range(np.shape(newborda)[0]):
            pos = [[newborda[q][0],newborda[q][1]+1], [newborda[q][0]-1,newborda[q][1]+1], [newborda[q][0]-1,newborda[q][1]], [newborda[q][0]-1,newborda[q][1]-1], [newborda[q][0],newborda[q][1]-1], [newborda[q][0]+1,newborda[q][1]-1], [newborda[q][0]+1,newborda[q][1]], [newborda[q][0]+1,newborda[q][1]+1]]
            
            for h in range(0,8):
                if q < (np.shape(newborda)[0]-1):
                    if pos[h] == newborda[q+1]:
                        if q == 0:
                            for m in range(8):
                                if pos[m] == newborda[-1]:
                                    if m == 0:
                                        chain.append(8 - h)
                                    else:
                                        if h - m >= 0:
                                            chain.append(h-m)
                                        else:
                                            chain.append(h-m+8)        
                        else:
                            if h == 0:
                                chain.append(8 - mem)
                            else:
                                if h - mem >= 0:
                                    chain.append(h-mem)
                                else:
                                    chain.append(h-mem+8)
                        mem = h
                else:
                    if pos[h] == newborda[0]:
                        if h == 0:
                            chain.append(8 - mem)
                        else:
                            if h - mem >= 0:
                                chain.append(h-mem)
                            else:
                                chain.append(h-mem+8)
                        mem = h 
            cope.append(mem)

    print(cope)
    return chain

def Esqueleto(imagem):
    aux = np.shape(imagem)
    copia = np.copy(imagem)
    para = 0
    count = 0

    while para == 0:
        deletar = []
        borda = SeguidorBorda(copia)
        count += 1

        if count == 20:
            plt.imshow(copia,cmap='gray')
            plt.show()
            count = 0

        for s in range(np.shape(borda)[0]):
            N = 0
            T = 0
            B0 = [borda[s][0],borda[s][1]]
            pos = [[B0[0],B0[1]-1],[B0[0]-1,B0[1]-1],[B0[0]-1,B0[1]],[B0[0]-1,B0[1]+1],[B0[0],B0[1]+1],[B0[0]+1,B0[1]+1],[B0[0]+1,B0[1]],[B0[0]+1,B0[1]-1]]
            
            for i in range(-1,2):
                for j in range(-1,2):
                    if B0[0]+i >= 0 and B0[0]+i<aux[0] and B0[1]+j>=0 and B0[1]+j<aux[1]:
                        if copia[B0[0]+i][B0[1]+j] == 1 and (i != 0 and j!= 0):
                            N += 1
            
            for a in range(8):
                if a > 0:
                    if copia[pos[a][0]][pos[a][1]] - copia[pos[a-1][0]][pos[a-1][1]] == 1:
                        T += 1
                else:
                    if copia[pos[0][0]][pos[0][1]] - copia[pos[7][0]][pos[7][1]] == 1:
                        T += 1
            
            if (N <= 6 and N >= 2) and T == 1 and copia[pos[2][0]][pos[2][1]]*copia[pos[4][0]][pos[4][1]]*copia[pos[6][0]][pos[6][1]] == 0 and copia[pos[4][0]][pos[4][1]]*copia[pos[6][0]][pos[6][1]]*copia[pos[0][0]][pos[0][1]] == 0:
                deletar.append(B0)
        
        for g in range(np.shape(deletar)[0]):
            x = deletar[g][0]
            y = deletar[g][1]
            copia[x][y] = 0

        borda = SeguidorBorda(copia)

        for s in range(np.shape(borda)[0]):
            N = 0
            T = 0
            B0 = [borda[s][0],borda[s][1]]
            pos = [[B0[0],B0[1]-1],[B0[0]-1,B0[1]-1],[B0[0]-1,B0[1]],[B0[0]-1,B0[1]+1],[B0[0],B0[1]+1],[B0[0]+1,B0[1]+1],[B0[0]+1,B0[1]],[B0[0]+1,B0[1]-1]]
            
            for i in range(-1,2):
                for j in range(-1,2):
                    if B0[0]+i >= 0 and B0[0]+i<aux[0] and B0[1]+j>=0 and B0[1]+j<aux[1]:
                        if copia[B0[0]+i][B0[1]+j] == 1 and (i != 0 and j!= 0):
                            N += 1
            
            for a in range(8):
                if a > 0:
                    if copia[pos[a][0]][pos[a][1]] - copia[pos[a-1][0]][pos[a-1][1]] == 1:
                        T += 1
                else:
                    if copia[pos[0][0]][pos[0][1]] - copia[pos[7][0]][pos[7][1]] == 1:
                        T += 1
            
            if (N <= 6 and N >= 2) and T == 1 and copia[pos[2][0]][pos[2][1]]*copia[pos[4][0]][pos[4][1]]*copia[pos[0][0]][pos[0][1]] == 0 and copia[pos[2][0]][pos[2][1]]*copia[pos[6][0]][pos[6][1]]*copia[pos[0][0]][pos[0][1]] == 0:
                deletar.append(B0)

        for g in range(np.shape(deletar)[0]):
            x = deletar[g][0]
            y = deletar[g][1]
            copia[x][y] = 0

        # print(deletar)

        if np.size(deletar) == 0:
            para = 1

    return copia

# def MPP(imagem):
