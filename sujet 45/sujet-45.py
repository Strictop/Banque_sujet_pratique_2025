# %%
def correspond(mot : str, mot_a_trous : str) -> bool:
    '''
    Prend en paramètres deux chaînes de caractères mot et mot_a_trous

    Renvoie True si on peut obtenir mot en remplaçant convenablement 
    les caractères '*' de mot_a_trous
    '''

    if len(mot) != len(mot_a_trous):
        return False
    
    for i in range(len(mot)):
        if mot_a_trous[i] != '*' and mot_a_trous[i] != mot[i]:
            return False

    return True



# %%

def est_cyclique(plan):
    '''Prend en paramètre un dictionnaire `plan` correspondant à 
    un plan d'envoi de messages (ici entre les personnes A, B, C,
    D, E, F).
    Renvoie True si le plan d'envoi de messages est cyclique et 
    False sinon.'''
    expediteur = 'A'
    destinataire = plan[expediteur] 
    nb_destinataires = 1

    while destinataire != expediteur:
        destinataire = plan[destinataire] 
        nb_destinataires = nb_destinataires + 1

    return nb_destinataires == len(plan) 


# %%
