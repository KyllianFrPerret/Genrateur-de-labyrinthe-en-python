def File():
    """
        Implémente une File en Python
        Entrée : aucune
        Sortie : une File vide
    """
    return []

def Enfiler(F, elt):
    """
        prend en entrée: F-> une file
                         elt -> un élèment
        renvoie la File avec comme dernière valeur elt
    """
    F.append(elt)
    return F

def Defiler(F):
    """
        prend en entrée : F -> une file
        en sortie : F sans sa première valeur et sa première valeur
    """
    return F.pop(0),F

def FileVide(F):
    """
        prend en entrée: F -> une file
        en sortie: si elle est vide renvoire False sinon True
    """
    return F == []

