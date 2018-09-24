import Utils
import numpy as np

def dilata(A,B):
    # B é o elemento estruturante simétrico responsável 
    # pelo preenchimento dos buracos
    return Utils.intersecao(Utils.translacao(Utils.reflexao(B)), A) 

