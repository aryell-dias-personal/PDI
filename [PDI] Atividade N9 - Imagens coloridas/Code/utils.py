import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt 

def LerImage(imagem):
    img = mpimg.imread('../imagens/{}.jpg'.format(imagem))
    return img

def rgb2hsi(imagem):
    r = imagem[:,:,0]
    g = imagem[:,:,1]
    b = imagem[:,:,2]

    r = Normalizar(r)
    g = Normalizar(g)
    b = Normalizar(b)

    aux = np.shape(r)
    H = np.zeros(aux)
    S = np.zeros(aux)
    I = np.zeros(aux)

    for x in range(aux[0]):
        for y in range(aux[1]):
            teta = np.arccos(((r[x][y]-g[x][y]+r[x][y]-b[x][y])/2)/((r[x][y]-g[x][y])**2+(r[x][y]-b[x][y])*(g[x][y]-b[x][y]))**(1/2))

            # print(r[x][y],g[x][y],b[x][y])

            if b[x][y] <= g[x][y]:
                H[x][y] = teta
            else:
                H[x][y] = 2*np.pi - teta

            S[x][y] = 1 - (3*min(r[x][y],g[x][y],b[x][y]))/(r[x][y]+g[x][y]+b[x][y])

            I[x][y] = (r[x][y]+g[x][y]+b[x][y])/3

    imagemHSI = []
    imagemHSI.append(H)
    imagemHSI.append(S)
    imagemHSI.append(I)

    imagemHSI = np.einsum('abc->bca',imagemHSI)

    # fig,[ax1,ax2,ax3] = plt.subplots(1,3)
    # ax1.imshow(H,cmap='gray')
    # ax2.imshow(S,cmap='gray')
    # ax3.imshow(I,cmap='gray')
    # plt.show()

    return imagemHSI

def hsi2rgb(imagem):
    h = imagem[:,:,0]
    s = imagem[:,:,1]
    i = imagem[:,:,2]

    aux = np.shape(h)
    R = np.zeros(aux)
    G = np.zeros(aux)
    B = np.zeros(aux)


    # for x in range(aux[0]):
    #     for y in range(aux[1]):
    #         if h[x][y] > 1:
    #             print('aaaaaa',h[x][y])
    #         if s[x][y] > 1:
    #             print('bbbbbbbb',s[x][y])
    #         if i[x][y] > 1:
    #             print('cccccc',i[x][y])

    for x in range(aux[0]):
        for y in range(aux[1]):
            if h[x][y] >= 0 and h[x][y] < (2*np.pi/3):
                B[x][y] = i[x][y]*(1-s[x][y])
                R[x][y] = i[x][y]*(1+((s[x][y]*np.cos(h[x][y]))/np.cos((np.pi/3) - h[x][y])))
                G[x][y] = 3*i[x][y] - (R[x][y]+B[x][y])
            elif h[x][y] >= (2*np.pi/3) and h[x][y] < (4*np.pi/3):
                h[x][y] = h[x][y] - (2*np.pi/3)
                R[x][y] = i[x][y]*(1 - s[x][y])
                G[x][y] = i[x][y]*(1+((s[x][y]*np.cos(h[x][y]))/np.cos((np.pi/3) - h[x][y])))
                B[x][y] = 3*i[x][y] - (R[x][y]+G[x][y])
            elif h[x][y] >= (4*np.pi/3) and h[x][y] <= 2*np.pi:
                h[x][y] = h[x][y] - (4*np.pi/3)
                G[x][y] = i[x][y]*(1 - s[x][y])
                B[x][y] = i[x][y]*(1+((s[x][y]*np.cos(h[x][y]))/np.cos((np.pi/3) - h[x][y])))
                R[x][y] = 3*i[x][y] - (G[x][y]+B[x][y])
            R[x][y] = int(np.rint(255*R[x][y]))
            G[x][y] = int(np.rint(255*G[x][y]))
            B[x][y] = int(np.rint(255*B[x][y]))
    
    img = []
    img.append(R)
    img.append(G)
    img.append(B)

    img = np.einsum('abc->bca',img)
    
    # fig,[ax1,ax2,ax3] = plt.subplots(1,3)
    # ax1.imshow(img[:,:,0],cmap='gray')
    # ax2.imshow(img[:,:,1],cmap='gray')
    # ax3.imshow(img[:,:,2],cmap='gray')
    # plt.show()

    return img

def Normalizar(imagem):
    mini = np.min(imagem)
    maxi = np.max(imagem)

    img = 255*(imagem - mini)/(maxi-mini)

    return img