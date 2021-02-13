second1 = {}
second2 = {}
second3 = {}

premiere1 = {}
premiere2 = {}
premiere3 = {}

terminale1 = {}
terminale2 = {}
terminale3 = {}

second = [second1,second2,second3]
premiere = [premiere1,premiere2,premiere3]
terminale  = [terminale1,terminale2,terminale3]



information = ()
def ajout(dico,nom_prenom,IDacadémique,age,spécialitées):
    """
    

    Parameters
    ----------
    dico : dictionnaire d'une classe.(dict)
    nom_prenom : nom de l'élève.(str)
    IDacadémique : son identification de l'académique.(int)
    age : son äge.(int)
    spécialitées : sa divisions de matières.(str)

    Returns
    -------
    dico : renvoie le dictionnaire de la classe avec l'élève ajouté.

    """
    dico[nom_prenom] = (IDacadémique, age, spécialitées)
    return dico

def affinom_prenom(dico):
    """
    

    Parameters
    ----------
    dico : dictionnaire d'une classe.

    Returns
    -------
    nom_prenom : nom et prenom des élèves d'une classe.

    """
    for nom_prenom in dico.keys():
        return nom_prenom

def affiID(dico):
    """
    

    Parameters
    ----------
    dico : dictionnaire d'une classe.

    Returns
    -------
    nom_prenom : nom et prenom des élèves d'une classe.
    
    ID: son identification de l'académique.

    """
    for nom_prenom,ID in dico.items():
        return nom_prenom,"Id de l'élève:",ID[0]




def affispés(dico):
    """
    

    Parameters
    ----------
    dico : dictionnaire d'une classe.

    Returns
    -------
    nom_prenom : nom et prenom des élèves d'une classe.
    
    spécialitées : spécialitées prisent par l'élève

    """
    for nom_prenom, spécialitées in dico.items():
        return nom_prenom,"les spécialitées de l'élève:", spécialitées[2]