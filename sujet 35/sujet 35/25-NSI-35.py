# %%

def max_dico(dico : dict) -> tuple :
    '''
    Prend en compte un dictionnaire dico et renvoie un tuple (clé , valeur)
    dont la valeur est la plus élevée dans dico
    '''

    noms = [element for element in dico.keys()]

    maxi = dico[noms[0]]
    max_nom = noms[0]
    for i in range[noms]:
        if dico[noms[i]] > maxi:
            maxi = dico[noms[i]]
            max_nom = noms[i]

    return (max_nom, maxi)



# %%

class Pile:
    """Classe définissant une structure de pile."""
    def __init__(self):
        self.contenu = []

    def est_vide(self):
        """Renvoie un booléen indiquant si la pile est vide."""
        return self.contenu == []

    def empiler(self, v):
        """Place l'élément v au sommet de la pile"""
        self.contenu.append(v)

    def depiler(self):
        """
        Retire et renvoie l'élément placé au sommet de la pile,
        si la pile n’est pas vide. Produit une erreur sinon.
        """
        assert not self.est_vide()
        return self.contenu.pop()

def eval_expression(tab):
    p = Pile()
    for element in tab: 
        if element != '+' and element != '*': 
            p.empiler(element) 
        else:
            if element == '+': 
                resultat = p.depiler() + p.depiler() 
            else:
                resultat = p.depiler() * p.depiler() 
            p.empiler(resultat) 
    return resultat



# %%
