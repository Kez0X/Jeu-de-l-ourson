import File
import csv

class GrapheParcours():
    """
    Classe permettant la création du graphe
    """
    def __init__(self, dictionnaire={'0450':[]}):
        """
        Fonction permettant d'initialiser le dictionnaire du graphe
        Entrée: dictionnaire--> un dictionnaire
        Sortie: aucune sortie mais le dico est devenu le dictionnaire
        """
        # Le dico est le dictionnaire
        self.dico = dictionnaire

    def _ajoutSommet(self,sommet):
        """ Ajoute un nouveau sommet au graphe. Si le sommet est déjà dans le graphe, on ne fait rien.
        Entrée : sommet -> le sommet à ajouter
        Sortie : aucune mais le sommet a été ajouté dans le graphe.
        """
        # Si l'élément n'est pas dans le dico
        if not sommet in self.dico:
            # Alors le sommet est ajouté dans le graphe sous la forme d'une liste vide
            self.dico[sommet] = []

    def _ajoutArc(self,s1,s2):
        """ Ajoute un nouvel arc au graphe, allant de s1 vers s2. Renvoie une erreur de type AssertionError si un des sommets s1 ou s2 n'est pas dans le graphe.
        Entrées : s1 -> un sommet, l'origine de l'arc
                s2 -> un sommet, l'extrémité de l'arc
        Sortie : aucune mais un arc a été ajouté de s1 vers s2.
        """
        # Si le sommet s2 n'est pas présent dans la liste dico clé s1
        if not s2 in self.dico[s1]:
            # Alors on le rajoute
            self.dico[s1].append(s2)

    def ajout_connexion(self,noeudOrigine,noeudArriver):
        """
        Cette fonction permet de sélectionner deux sommets non reliés et de les relier ensemble
        Entrée: noeudOrigine --> sommet d'origine du chemin crée
                noeudArriver --> sommet d'arrivée du chemin crée
        Sortie: Aucune mais le chemin entre les deux sommets a été crée
        """
        # Selection du sommet d'origine
        self._ajoutSommet(noeudOrigine)
        # Selection du sommet d'arrivée
        self._ajoutSommet(noeudArriver)
        # Relie les deux sommets séléctionnés entre eux
        self._ajoutArc(noeudOrigine,noeudArriver)

    def voisins(self,sommet):
        """ Renvoie la liste des voisins d'un sommet du graphe. Renvoie une erreur de type AssertionError si le sommet n'est pas dans le graphe.
        Entrée : un sommet du graphe
        Sortie : list -> la liste des voisins du sommet.
        """
        #renvoie la liste des voisins du sommet selectionné
        return self.dico[sommet]

    def ecriture(self):
        """
        Entrée: prends en entrée un objet GrapheParcours
        Sortie: rien
        Permet de sauvegarder GrapheParcours dans un fichier csv
        """
        # On demande l'ouverture du fichier parcours.csv
        with open('parcours.csv', 'w', newline='') as csvfile:
            # On définit comme colonnes 'racine' et 'fils'
            fieldnames = ['racine', 'fils']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            # Pour toutes les clé se situant de le dico de GrapheParcours
            for cle in self.dico:
                # On parcours tous leurs éléments associés
                for indiceElement in range(len(self.dico[cle])):
                    # Et on les écrit dans le fichier
                    writer.writerow({'racine': cle, 'fils': self.dico[cle][indiceElement]})

    def lecture(self):
        """
        Entrée: prends en entrée un objet GrapheParcours
        Sortie: rien
        Permet de lire un fichier csv pour définir le dico de GrapheParcours
        """
         # On demande l'ouverture du fichier parcours.csv
        with open('parcours.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            # On parcours le fichier csv
            for row in reader:
                # On établie les connexions entre les racines et les fils pour reconstituer un graphe conteant toutes les possibilités déjà sauvegardées
                self.ajout_connexion(row['racine'],row['fils'])

    def _parcoursLargueur(self,sommetDepart):
        """
        Parcours en largueur du graphe g depuis le sommet sommetDepart
        Entrée:
            g -> un graphe
            sommetDepart -> un sommet du graphe
        Sortie:
            aucune mais affichage des sommets visités
        """
        #On utilise une file pour un parcours en largueur
        F=File.File()
        #dictionnaire recensant les sommets découverts (mais pas forcément visités)
        decouverts = {}
        #on commence par le sommet de départ
        F.Inserer(sommetDepart)
        decouverts[sommetDepart]=None
        #tant qu'il reste des sommets à visiter
        while not F.FileVide():
            sommet = F.Extraire()
            #pour chaque voisin du sommet, on  l'ajoute dans les sommets à visiter
            #si'l n'a pas encore été découvert
            for voisin in self.voisins(sommet):
                if not voisin in decouverts:
                    F.Inserer(voisin)
                    decouverts[voisin]=sommet
            # #on traite le sommet
            # print(sommet,end=' ')
        return decouverts

    def remonterDeParcours(self,sommetDepart):
        """
        Entrée: prends en entrée un objet GrapheParcours
        Sortie: renvoie une liste du chemin le plsu court
        Sert à déterminer le chemin le plus court jusqu'aux positions de blocage de l'ourson
        """
        # On effectue le parcours en largueur que l'on sauvegarde dans un dictionnaire
        dictionnairePlusCourt = self._parcoursLargueur(sommetDepart)
        # On initialise une liste pour contenir le chemin le plus optimiser
        minimum=[]
        # On parcours toutes les clés du parcours en largueur
        for cle in dictionnairePlusCourt:
            # print(cle,dictionnairePlusCourt[cle])
            # if cle != sommetDepart and len(cle)>4:

            # Si la clé est une des deux clés qui permettent de bloqués l'ourons alors
            if cle == "4021" or cle == "5031":
                # On initialise une liste pour contenir un chemin
                temporaire=[]
                # On ajoute la clé
                temporaire.append(cle)
                # On sauvegarde la clé
                cle_a_voir=cle
                # Tant que la clé n'est pas None (condition d'arret)
                while cle_a_voir!=None:
                    # print(cle_a_voir)
                    # On ajoute à la liste l'élément de dictionnairePlusCourt avec la clé cle_a_voir
                    temporaire.append(dictionnairePlusCourt[cle_a_voir])
                    # On définit comme cle_a_voir à l'élément ajouter
                    cle_a_voir=dictionnairePlusCourt[cle_a_voir]
                # print(temporaire)
                ##--##
                """" p.remonterDeParcours('1')
                     ['2', '1', None]
                     ['4', '1', None]
                     ['3', '2', '1', None]
                     []                          """
                ##--##
                # Si la liste minimum est vide ou qu'elle est plus grande que temporaire alors
                if minimum == [] or len(minimum)>len(temporaire):
                    # On réinitialise minimum comme liste vierge
                    minimum=[]
                    # On parcours tous les éléments de la liste temporaire pour les ajouter à minimum
                    for indice in range (len(temporaire)):
                        minimum.append(temporaire[indice])
        # On renvoie la liste minimum
        return minimum
##--##
# p=GrapheParcours({})
# p.ajout_connexion('1457','2654')
# p.ajout_connexion('2654','3147')
# p.ajout_connexion('3147','4021')
# p.ajout_connexion('2654','4021')