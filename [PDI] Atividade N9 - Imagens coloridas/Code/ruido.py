import numpy as np
import matplotlib.pyplot as plt
import utils

def average(imagem,m=3,n=3):
    r = imagem[:,:,0]
    g = imagem[:,:,1]
    b = imagem[:,:,2]

    aux = np.shape(r)

    rfil = np.zeros(aux)
    gfil = np.zeros(aux)
    bfil = np.zeros(aux)

    media_r = 0
    media_b = 0
    media_g = 0

    for x in range(aux[0]):
        for y in range(aux[1]):
            for u in range(m*n):
                if (x+u%m-1 >= 0) and (x+u%m-1 < aux[0]) and (y+u%n-1 >= 0) and (y+u%n-1 < aux[1]):
                    media_r += r[x+u%m-1][y+u%n-1]
                    media_b += b[x+u%m-1][y+u%n-1]
                    media_g += g[x+u%m-1][y+u%n-1]
            rfil[x][y] = int(np.rint(media_r/(m*n)))
            gfil[x][y] = int(np.rint(media_g/(m*n)))
            bfil[x][y] = int(np.rint(media_b/(m*n)))
            media_r = 0
            media_g = 0
            media_b = 0

    rfil = utils.Normalizar(rfil)
    gfil = utils.Normalizar(gfil)
    bfil = utils.Normalizar(bfil)

    filterImg = []

    filterImg.append(np.uint8(rfil))
    filterImg.append(np.uint8(gfil))
    filterImg.append(np.uint8(bfil))

    filterImg = np.einsum('abc->bca',filterImg)

    fig,[ax1,ax2,ax3] = plt.subplots(1,3)
    ax1.imshow(rfil,cmap='gray')
    ax2.imshow(gfil,cmap='gray')
    ax3.imshow(bfil,cmap='gray')
    plt.show()    

    return filterImg

def Median(imagem,m=3,n=3):
    r = imagem[:,:,0]
    g = imagem[:,:,1]
    b = imagem[:,:,2]

    aux = np.shape(r)

    rfil = np.zeros(aux)
    gfil = np.zeros(aux)
    bfil = np.zeros(aux)
    
    ker_r = np.zeros(m*n)
    ker_g = np.zeros(m*n)
    ker_b = np.zeros(m*n)

    for x in range(aux[0]):
        for y in range(aux[1]):
            for u in range(m*n):
                if (x+u%m-1 >= 0) and (x+u%m-1 < aux[0]) and (y+u%n-1 >= 0) and (y+u%n-1 < aux[1]):
                    ker_r[u] = r[x+u%m-1][y+u%n-1]
                    ker_g[u] = g[x+u%m-1][y+u%n-1]
                    ker_b[u] = b[x+u%m-1][y+u%n-1]
            for v in range(m*n):
                for t in range(v,m*n):
                    if ker_r[v] > ker_r[t]:
                        auxr = ker_r[t]
                        ker_r[t] = ker_r[v]
                        ker_r[v] = auxr   
                    if ker_g[v] > ker_g[t]:
                        auxg = ker_g[t]
                        ker_g[t] = ker_g[v]
                        ker_g[v] = auxg   
                    if ker_g[v] > ker_g[t]:
                        auxb = ker_b[t]
                        ker_b[t] = ker_b[v]
                        ker_b[v] = auxb
            if (m*n)%2 > 0:
                rfil[x][y] = ker_r[int((m*n-1)/2)]
                gfil[x][y] = ker_g[int((m*n-1)/2)]
                bfil[x][y] = ker_b[int((m*n-1)/2)]
            else:
                rfil[x][y] = (ker_r[int(np.floor(m*n/2))]+ker_r[int(np.ceil(m*n/2))])/2
                gfil[x][y] = (ker_g[int(np.floor(m*n/2))]+ker_g[int(np.ceil(m*n/2))])/2
                bfil[x][y] = (ker_b[int(np.floor(m*n/2))]+ker_b[int(np.ceil(m*n/2))])/2

    filterImg = []

    filterImg.append(rfil)
    filterImg.append(gfil)
    filterImg.append(bfil)

    filterImg = np.einsum('abc->bca',filterImg)

    # fig,[ax1,ax2,ax3] = plt.subplots(1,3)
    # ax1.imshow(filterImg[:,:,0],cmap='gray')
    # ax2.imshow(filterImg[:,:,1],cmap='gray')
    # ax3.imshow(filterImg[:,:,2],cmap='gray')
    # plt.show()

    return filterImg

# def 