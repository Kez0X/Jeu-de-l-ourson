class Pile():
    """ Classe implémentant ue structure de Pile """
    def __init__(self):
        """ Construit une Pile vide """
        self._pile = []
        
    def PileVide(self):
        """ Permet de savoir si la Pile est vide.
        Entrée : aucune
        Sortie : Bool, True si la Pile est vide, False sinon.
        """
        return self._pile == []
        
    def Empiler(self,elt):
        """ Permet d'empiler un nouvel élément dans la pile.
        Entrée : elt -> élément à empiler
        Sortie : aucune.
        """
        self._pile.append(elt)
        
    def Depiler(self):
        """ Permet de dépiler le dernier élément de la pile.
        Entrée : aucune
        Sortie : l'élément dépilé.
        """
        return self._pile.pop()