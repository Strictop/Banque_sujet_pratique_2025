# %%
def multiplication(n1 : int ,n2 : int ) -> int :
    '''
    Si tu ne sais pas ce qu'est une multiplication sérieux...
    '''
    resultat = 0
    if n2 < 0 and n1 < 0:
        return multiplication(abs(n1),abs(n2))
    elif n2 < 0 :
        return multiplication(n2,n1)
    else:
        for _ in range(n2):
            resultat += n1
        return resultat
    

# %%
def chercher(tab, x, i, j):
    '''Renvoie l'indice de x dans tab, si x est dans tab, 
    None sinon.
    On suppose que tab est trié dans l'ordre croissant.'''
    if i > j:
        return None
    m = (i + j) // 2 
    if tab[m] < x: 
        return chercher(tab, x, i , m-1) 
    elif tab[m] > x:
        return chercher(tab, x, m+1 , j) 
    else:
        return m 



# %%
