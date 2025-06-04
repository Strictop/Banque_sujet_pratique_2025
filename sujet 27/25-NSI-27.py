# %%

def verifie(tab : list)-> bool:
    '''
    prend en paramètre un tableau de valeurs numériques et  
    renvoie True si ce tableau est trié dans l’ordre croissant, False sinon.
    '''
    if tab == []:
        return True
    
    for i in range(len(tab)-1):
        if tab[i] > tab[i+1]:
            return False
    return True



# %%

def depouille(urne):
    '''prend en paramètre une liste de suffrages et renvoie un 
    dictionnaire avec le nombre de voix pour chaque candidat'''
    resultat = dict() 
    for bulletin in urne:
        if bulletin in resultat.keys(): 
            resultat[bulletin] = resultat[bulletin] + 1
        else:
            resultat[bulletin] = 1
    return resultat

def vainqueurs(election):
    '''prend en paramètre un dictionnaire non vide avec le nombre de voix
    pour chaque candidat et renvoie la liste des vainqueurs'''
    nmax = 0
    for candidat in election:
        if election[candidat] > nmax : 
            nmax = election[candidat]
    liste_finale = [ nom for nom in election if election[nom] == nmax ] 
    return liste_finale



# %%
