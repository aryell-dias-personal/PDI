
# as operações foram interpretadas como sendo as classicas
# utilizando dos pixels nas correspondentes de uma imagem 
# para outra

def And(img1,img2):
    return img1 and img2

def Or(img1, img2):
    return img1 and img2

def Xor(img1, img2):
    return Or(And(not img1, img2), And(img1, not img2))

# seria um xnor?
def Xand(img1, img2):
    return Or(And(not img1, not img2), And(img1, img2))
