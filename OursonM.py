from ClassGrapheParcours import*
import random
import Graph_Ourson
from AffichageBasicOurson import*

def Creation_Graph():
    """
    Entrée: rien
    Sortie: le graphe du plateau de jeu ainsi que le tableau de position des joueurs
    Sert à initialiser les conditions de jeux
    """
    # Création du dictionnaire du jeu de l'ourson au niveau normal
    GraphOursonNormal={
                0:(1,2,3,4,5),
                1:(0,2,3),
                2:(0,1,4),
                3:(0,1,5),
                4:(0,2),
                5:(0,3)
                }
    # Initialisation du tableau de position
    TableauPosition=[0,4,5,0]
    # Créations des graphes
    GraphOursonNormal=Graph_Ourson.Graph_Ourson(GraphOursonNormal)
    # On renvoie le graphe et la tableau de possition
    return GraphOursonNormal,TableauPosition

def tri_chien(liste):
    """
    Entrée: la liste de position
    Sortie: la liste de posisiotn triée
    Sert à trier la liste de position en mettant les chiens dans l'ordre croissant pour éviter des doublons dans le graphes de parcours
    """
    # Si le premier chien dans la liste est plus grand que le second alors on l'échange
    if liste[1]>liste[2]:
        swap=liste[2]
        liste[2]=liste[1]
        liste[1]=swap
    # On renvoie la liste triée
    return liste

def choixJoueur(Graphe,positionActuelle,TableauPosition):
    """
    Entrée:Le graphe contenant toutes les positions ,la position actuelle du pion que l'on souhaite bouger et le tableau des positions actuelle des pions
    Sortie: reponse qui est le deplacement du joueur
    Fonction pour faire mouvoir le joueur
    """
    def voisins_est_vide(Graphe,positionActuelle,TableauPosition):
        """
        Entrée: La position actuelle du pion que l'on souhaite bouger et le tableau des positions actuelle des pions
        Sortie: La liste des différents voisins où le pion peut bouger
        Fonction qui vérifie si la case adjacente est vide
        """
        # Initialisation de la liste reponse
        rep=[]
        # On récupère la liste des voisins de positionActuelle
        ListeVoisins=Graph_Ourson.Graph_Ourson.voisins(Graphe,positionActuelle)
        # On va regarder si les diffrents voisins correspondent au cases occupés ou non par les autres pions
        for element in ListeVoisins:
            # Si l'élement ne correspond pas aux cases déjà occupées alors on l'ajoute dans la liste réponse
            if element!= TableauPosition[0] and element!= TableauPosition[1] and element!= TableauPosition[2]:
                # On ajoute l'élément dans la liste réponse
                rep.append(element)
        # On renvoie la réponse
        return rep

    def deplacement(Graphe,positionActuelle,TableauPosition):
        """
        Entrée: Le graphe qui correspond au plateau de jeu, la posistion actuelle du pion et le tableau des positions des différents pions
        Sortie: La nouvelle position actuelle du pion et le nouveau tableau position
        Fonction qui permet de bouger un pion
        """
        # On initialise un booléen à False
        bool=False
        # On récupère la liste des voisins de la position actuelle du pion
        listeVoisin=voisins_est_vide(Graphe,positionActuelle,TableauPosition)
        # On met dans une variable affiche la liste des voisins sous forme de chaine de caractère
        affiche=" ".join(str(listeVoisin))
        # On affiche donc les/la propositions de déplacements
        print("Voici les cases où vous pouvez vous déplacer :\n",affiche)
        # On demande à l'utilisateur sur quelle case il souhaite se déplacer
        rep=int(input("Sur quelle case voulez vous vous déplacez ?\n"))
        # On va vérifier si la case choisit par l'utilisateur est dans la liste des voisins
        for element in listeVoisin:
            # Si il y est alors on met le booléen à True
            if rep==element:
                bool=True
        # Si le booléen est égale à True alors on va vérifier qui joue l'ourson(0) ou les chiens(1)
        if bool==True:
            # Si c'est l'ourson qui joue
            if TableauPosition[3]==0:
                # On met à jour la position de l'ourson dans le tableau
                TableauPosition[0]=rep
                # On change de joueur
                TableauPosition[3]=1
            # Si c'est les chiens qui jouent
            else:
                # On change le joueur pour le prochain tour
                TableauPosition[3]=0
                # On regarde quel chien joue
                if TableauPosition[1]==positionActuelle:
                    # On met à jour la position du chien dans le tableau
                    TableauPosition[1]=rep
                else:
                    # On met à jour la position du chien dans le tableau
                    TableauPosition[2]=rep
            # On retourne la position actuelle du pion et le tableau des positions
            return TableauPosition
        # Sinon on recommence la fonction
        else:
            deplacement(Graphe,positionActuelle,TableauPosition)

    # On attribut à reponse le résultat de la fonction deplacement
    reponse = deplacement(Graphe,TableauPosition[0],TableauPosition)

    # On renvoie reponse
    return reponse

def questionReJouer():
    """
    Entrée: rien
    Sortie: Soit 0/1 la réponse, soit on renvoie la fonction
    Sert à demander au joueur si il veut continuer à jouer
    """
    # On essaie la question
    try:
        question=int(input("0:Quitter / 1:Jouer :  "))
    # Si question n'est pas un integer alors on renvoie la fonction
    except ValueError:
        return questionReJouer()
    # Si question n'est pas une réponse attendu (0/1) alors on redemande la fonction
    if question != 0 and question != 1:
        question = questionReJouer()
    # Sinon on renvoie question: la réponse à la question
    else:
        return question

def jeu():
    """
    Entrée: rien
    Sortie: l'objet jeu
    Fonction qui contient le jeu
    """

    #Texte de présentation
    print('----------')
    print("Bienvenue dans le jeu de l'ourson\n")
    print("Le but est de vous déplacer en échappant aux chiens qui n'auront que 14 coups pour le faire")
    print("Bon jeu et bonne chance")
    print('----------\n')

    # On demande si le joueur veut jouer
    question = questionReJouer()

    # On essaie d'appeller le fichier parcours et on génère le graphe du parcours
    try:
        grapheParcours=GrapheParcours()
        grapheParcours.lecture()
    # Si on n'y arrive pas on ne génère que le graphe du parcours
    except FileNotFoundError:
        grapheParcours=GrapheParcours()

    # Tant que l'on veut jouer
    while question ==1:

        # On initialise le plateau de jeu ainsi que les positions de départs
        plateau,TableauPosition=Creation_Graph()
        # On met le compeut de coup à 0
        compteur = 0

        # On dit que l'ourson n'est pas bloqué (car 1er tour -> il a possibilité de se déplacer)
        bloquer = False

        # affichage
        affichageOurson(TableauPosition)

        # Tant que le nombre de coup est inférieur à 15 (donc se joue en 14 coup) et que l'ourson ne'st pas bloqué alors:
        while compteur < 15 and not bloquer:

            # On dit que s'est le tour de l'ourson (pas nécessaire au 1er tour mais obligatoire pour les suivants)
            TableauPosition[3]=0

            # On sauvegarde les dernières positions
            TableauPositionTemporaire = [TableauPosition[indice] for indice in range(len(TableauPosition))]
            ##< déplacement du joueur >
            # On demande le choix au joueur
            TableauPosition = choixJoueur(plateau,TableauPosition[0],TableauPosition)
            # On tri les pions
            TableauPosition = tri_chien(TableauPosition)

            #affichage
            affichageOurson(TableauPosition)
            ##</ >

            # On augmente le compteur de 1 car joueur à joué
            compteur = compteur +1

            # On ajoute les déplacemnts précédents dans le graphes de parcours
            grapheParcours.ajout_connexion(''.join(map(str, TableauPositionTemporaire)),''.join(map(str, TableauPosition)))

            ##< déplacement des chiens >
            # On sauvegarde les dernières positions
            TableauPositionTemporaire = [TableauPosition[indice] for indice in range(len(TableauPosition))]
            # Programme de choix pour le déplacemnt des chiens
            TableauPosition = choixChien(grapheParcours,TableauPosition,plateau)
            ##</ >
            # On ajoute les déplacemnts précédents dans le graphes de parcours
            grapheParcours.ajout_connexion(''.join(map(str, TableauPositionTemporaire)),''.join(map(str, TableauPosition)))
            # Affichage pour séparer les plateaus entre les tours
            print("--------------------------")

            # On regarde si l'ourson est bloqué
            bloquer = ours_bloque(TableauPosition)
            # On augmente le compteur de 1 car joueur à joué
            compteur = compteur +1

        # affichage
        affichageOurson(TableauPosition)

        # Si l'ourson est bloqué alors on affiche la victoire des chiens sinon on affiche la victoire de l'ourson
        if bloquer :
            print("Victoire des chiens")
        else:
            print("Victoire de l'ourson'")

        # On redemande si on veut refaire une partie
        print("Nouvelle partie")
        question = questionReJouer()

    # On sauvergarde le graphe de parcours pour les prochaines parties
    grapheParcours.ecriture()

    return jeu

def choixChien(grapheParcours,tableauPosition,plateau):
    """
    Entrée:Le graphe contenant toutes les positions ,le tableau des positions actuelle des pions et le plateau de jeu
    Sortie: possibilite qui est le deplacement du joueur
    Fonction pour faire mouvoir le chien
    """

    # L'on duplique le tableau de position mais en chaine de caractère
    sommetActuelle = ''.join(map(str, tableauPosition))

    # On teste si il existe un parcours possible
    possibilite = grapheParcours.remonterDeParcours(sommetActuelle)

    # Si il n'y a pas de parcours possible alors
    if possibilite == []:
        def voisins_est_vide(Graphe,positionActuelle,TableauPosition):
            """
            Entrée: La position actuelle du pion que l'on souhaite bouger et le tableau des positions actuelle des pions
            Sortie: rep: la liste des différents voisins où le pion peut bouger
            Méthode qui vérifie si la case adjacente est vide
            """
            # Initialisation de la liste reponse
            rep=[]
            # On récupère la liste des voisins de positionActuelle
            ListeVoisins=Graph_Ourson.Graph_Ourson.voisins(Graphe,positionActuelle)
            # On va regarder si les diffrents voisins correspondent au cases occupés ou non par les autres pions
            for element in ListeVoisins:
                # Si l'élement ne correspond pas aux cases déjà occupées alors on l'ajoute dans la liste réponse
                if element!= TableauPosition[0] and element!= TableauPosition[1] and element!= TableauPosition[2]:
                    # On ajoute l'élément dans la liste réponse
                    rep.append(element)
            # On renvoie rep
            return rep

        def toute_possibilite(graphe,tableauPosition):
            """
            Entrée: graphe étant le plateau de jeu et tableauPosition
            Sortie: possibilite qui le deplacemnt du chien
            Teste toutes les possibilités de déplacement des chiens
            """
            # On initialise une liste vide
            possibilite=[]
            # On parcours tous les indices des chiens dans tableauPosition donc 1 et 2
            for indiceChien in range (1,3):
                # Teste les possibilites pour savoir si les cases adjacentes sont libres voisins etant une liste
                voisins=voisins_est_vide(graphe,tableauPosition[indiceChien],tableauPosition)
                # On parcours alors toutes la liste voisins
                for indice in range (len(voisins)):
                    # On initialise une liste de copie
                    copie=[]
                    # On veut dupliquer tableauPostion donc on parcours tous ces éléments
                    for elt in tableauPosition:
                        # On ajoute à copie l'élément de tableauPostion
                        copie.append(elt)
                    # On remplace le chien selectioné par sa position probable
                    copie[indiceChien]=voisins[indice]
                    # On trie cette copie
                    copie=tri_chien(copie)
                    # Possibilite devient la chaine de caractère des éléments de copie
                    possibilite.append(''.join(map(str, copie)))
            # On renvoie possibilite
            return possibilite

        def string_to_intList(string):
            """
            Entrée: string qui est la chaine que l'on veut transformer
            Sortie: list qui est la chaine transformé
            Convertie une chaine de caractère en une liste
            """
            # On initialise un liste
            list=[]
            # On parcours tous les éléments du mot
            for indice in range(len(string)):
                # On les ajoute à list
                list.append(int(string[indice]))
            # On renvoie list
            return list

        # On teste toutes les possibilitées de déplacement des chiens
        possibilite = toute_possibilite(plateau,tableauPosition)
        # On en choisi une au hasrd
        possibilite = possibilite[random.randint(0,len(possibilite)-1)]
        # Elle est convertie en liste
        possibilite = string_to_intList(possibilite)
        # On met bien de c'est le tour des chiens
        possibilite[3]=1
    # On renvoie la possibilite
    return possibilite

def ours_bloque(TableauPosition):
    """
    Entrée: TableauPosition
    Sortie: un booléen
    Sert à determiner si l'ourson peut encore se déplacer
    """
    # Par défault on dit que non: il peut encore se déplacer
    reponse = False
    # Mais si on n'est sur une de ces deux configurations qui sont les seuls ou les chiens gagnent alors:
    if TableauPosition == [4,0,2,1] or TableauPosition == [5,0,3,1]:
        # On met reponse à vrai
        reponse = True
    # On renvoie le resultat du teste
    return reponse

jeu()