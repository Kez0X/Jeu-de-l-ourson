def affichageOurson(listePosition):
    """
    Entrée: Prends la liste de position
    Sortie: Rien
    Permet d'afficher la liste de position dans la console
    """
    # Dictionnaire contenant les caractères pour représenter l'ourson et les chiens
    caracterePion=["o","c"]

    # Coordonées des cases ou l'on va placer les pions
    positionCaseListeAffichage={
    0:(1,7),
    1:(5,7),
    2:(8,4),
    3:(8,10),
    4:(11,1),
    5:(11,13)
    }

    # Liste contenant l'affichage graphique
    listeAffichage=[
    [" "," "," "," "," "," ","╔","0","╗"," "," "," "," "," "," "],
    [" "," "," "," ","╔","═","╣"," ","╠","═","╗"," "," "," "," "],
    [" "," "," "," ","║"," ","╚","╦","╝"," ","║"," "," "," "," "],
    [" "," "," "," ","║"," "," ","║"," "," ","║"," "," "," "," "],
    [" ","╔","═","═","╣"," ","╔","╩","╗"," ","╠","═","═","╗"," "],
    [" ","║"," "," ","║"," ","1"," ","║"," ","║"," "," ","║"," "],
    [" ","║"," "," ","║"," ","╚","╦","╝"," ","║"," "," ","║"," "],
    [" ","║"," ","╔","╩","╗"," ","║"," ","╔","╩","╗"," ","║"," "],
    [" ","║"," ","2"," ","╠","═","╩","═","╣"," ","3"," ","║"," "],
    [" ","║"," ","╚","╦","╝"," "," "," ","╚","╦","╝"," ","║"," "],
    ["╔","╩","╗"," ","║"," "," "," "," "," ","║"," ","╔","╩","╗"],
    ["4"," ","╠","═","╝"," "," "," "," "," ","╚","═","╣"," ","5"],
    ["╚","═","╝"," "," "," "," "," "," "," "," "," ","╚","═","╝"]
    ]

    # On parours toutes la liste de posistions sauf le témoin de joueur
    for indice in range(len(listePosition)-1):
        # Si l'élément de la liste de position est comme clé dans positionCaseListeAffichage alors:
        if listePosition[indice] in positionCaseListeAffichage:
            # On extrait les coordonées en accédant au dictionnaire par la clé, on obtient alors un tuple contenant en indice 0 la coordonées en X et en indice 1 la coordonées en Y
            indiceX=positionCaseListeAffichage[listePosition[indice]][0]
            indiceY=positionCaseListeAffichage[listePosition[indice]][1]

            # Si indice < 1 donc si c'est l'ourson on change la case par le symbole adapté
            if indice<1:
                listeAffichage[indiceX][indiceY]=str(caracterePion[0])
            # Sinon l'on fait pareil mais pour les chiens
            else:
                listeAffichage[indiceX][indiceY]=str(caracterePion[1])

    # On parcours la liste d'affichage et on l'affiche ligne par ligne
    for indice in range (len(listeAffichage)):
        print("".join(listeAffichage[indice]))