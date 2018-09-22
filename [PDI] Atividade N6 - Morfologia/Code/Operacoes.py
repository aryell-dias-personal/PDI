import Utils as *
import numpy as np

dilata(A,B):
    # B é o elemento estruturante simétrico responsável 
    # pelo preenchimento dos buracos
    return intersercao(translacao(reflexao(B)), complemento(A)) 

