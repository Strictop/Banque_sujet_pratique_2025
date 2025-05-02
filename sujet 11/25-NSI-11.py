# %%

def parcours_largeur(arbre):
    if arbre != None :
        (g, x, d) = arbre
        return [x] + [parcours_largeur(g)] + [parcours_largeur(d)]



arbre = ( ( (None, 1, None), 2, (None, 3, None) ),4,( (None, 5, None), 6, (None, 7, None) ) )        
parcours_largeur(arbre)
    







# %%
def somme_max(tab):
    n = len(tab)
    sommes_max = [0]*n
    sommes_max[0] = tab[0]
    # on calcule la plus grande somme se terminant en i
    for i in range(1,n):
        if ... + ... > ...: 
            sommes_max[i] = ... 
        else:
            sommes_max[i] = ... 
    # on en déduit la plus grande somme de celles-ci
    maximum = 0
    for i in range(1, n):
        if ... > ...: 
            maximum = i

    return sommes_max[...] 


