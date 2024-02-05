class Graph_Ourson():
    """
    Classe implémentant des graphes pour le jeu de l'ourson
    """

    def __init__(self, dictionnaire = None):
        """
        Entrée: un dictionnaire par défaut None
        Sert à initialiser le graphe
        """
        # Si dictionnaire est None alors on défini dico par un dictionnaire
        if dictionnaire == None:
            self.dico = {}
        # Sinon on défini dico par le dictionnaire introduit dans les paramètres
        else:
            self.dico = dictionnaire


    def voisins(self,sommet):
        """ Renvoie la liste des voisins d'un sommet du graphe. Renvoie une erreur de type AssertionError si le sommet n'est pas dans le graphe.
        Entrée : un sommet du graphe
        Sortie : list -> la liste des voisins du sommet.
        """
        assert sommet in self.dico, "sommet n'est pas un sommet du graphe."
        return self.dico[sommet]









