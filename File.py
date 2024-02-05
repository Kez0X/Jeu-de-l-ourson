import Pile as P

class File():
    """ Classe implémentant ue structure de File """
    def __init__(self):
        """ Construit une File vide """
        self._pileE = P.Pile()
        self._pileS = P.Pile()
        
    def FileVide(self):
        """ Permet de savoir si la File est vide.
        Entrée : aucune
        Sortie : Bool, True si la File est vide, False sinon.
        """
        return self._pileE.PileVide() and self._pileS.PileVide()
        
    def Inserer(self,elt):
        """ Permet d'insérer un nouvel élément dans la File.
        Entrée : elt -> élément à insérer
        Sortie : aucune.
        """
        self._pileE.Empiler(elt)
        
    def Extraire(self):
        """ Permet d'extaire le premier élément de la File.
        Entrée : aucune
        Sortie : l'élément extrait.
        """
        if self._pileS.PileVide():
            while not self._pileE.PileVide():
                elt  = self._pileE.Depiler()
                self._pileS.Empiler(elt)
        return self._pileS.Depiler()