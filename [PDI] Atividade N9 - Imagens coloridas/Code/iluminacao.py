import numpy as np

def clarear(imagemOriginal, c): 
    imagemOriginal=np.log(c*imagemOriginal+1) 
    imagemOriginal=imagemOriginal-np.min(imagemOriginal) 
    imagemOriginal=imagemOriginal/np.max(imagemOriginal) 
    imagemOriginal=imagemOriginal*255 
    imagemOriginal=np.array(imagemOriginal,dtype=np.uint8) 
    return imagemOriginal 
def escurecer(imagemOriginal, c): 
    imagemOriginal=np.exp(c*imagemOriginal+1) 
    imagemOriginal=imagemOriginal-np.min(imagemOriginal) 
    imagemOriginal=imagemOriginal/np.max(imagemOriginal) 
    imagemOriginal=imagemOriginal*255 
    imagemOriginal=np.array(imagemOriginal,dtype=np.uint8) 
    return imagemOriginal 