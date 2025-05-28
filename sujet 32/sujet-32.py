# %%

def occurrences(caractere : str, chaine : str) -> int:
    '''
    Cette fonction renvoie le nombre d’occurrences de caractere dans chaine, c’est-à-dire
    le nombre de fois où caractere apparaît dans chaine.
    '''
    compte = 0
    for element in chaine:
        if element == caractere:
            compte += 1
    return compte



# %%

valeurs = [100, 50, 20, 10, 5, 2, 1]

def rendu_glouton(a_rendre, rang):
    if a_rendre == 0:
        return []
    v = valeurs[rang]
    if v <= a_rendre: 
        return [v] + rendu_glouton(a_rendre - v, rang) 
    else:
        return rendu_glouton(a_rendre, rang + 1) 



# %%
