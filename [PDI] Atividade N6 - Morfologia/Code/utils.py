import matplotlib.image as mpimg
import numpy as np

# leitura da imagem
def LerImagem(nome):
    imagem = mpimg.imread(nome)
    return imagem

# as operações foram interpretadas como sendo as classicas
# utilizando dos pixels nas correspondentes de uma imagem 
# para outra

def operation(img1,img2, operation):
    img1 = np.array(img1[:,:,0], dtype=bool)
    img2 = np.array(img2[:,:,0], dtype=bool)
    x,y = np.shape(img1)
    if(operation == 'and'):
        return [[img1[i][j] and img2[i][j] for j in range(y)]for i in range(x)]
    elif(operation == 'or'):
        return [[img1[i][j] or img2[i][j] for j in range(y)]for i in range(x)]
    elif(operation == 'xor'):
        return [[((not img1[i][j]) and (img2[i][j])) or ((img1[i][j]) and (not img2[i][j])) for j in range(y)]for i in range(x)]
    # seria um xnor?
    elif(operation == 'xand'):
        return [[((not img1[i][j]) and (not img2[i][j])) or ((img1[i][j]) and (img2[i][j])) for j in range(y)]for i in range(x)]

translacao(conjunto):
# TODO será util para implementação da dilatação

reflexao(conjunto):
# TODO será util para implementação da dilatação

complemento(subConjunto, conjunto):
# TODO será util para implementação da dilatação

intersercao(A,B):
# TODO será util para implementação da dilatação