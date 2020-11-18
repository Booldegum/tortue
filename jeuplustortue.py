#tp : jeu du juste Prix
    # choisir un nombre entre 1 et 1000
    # tant que le jeu n'est pas fini
    #  -> demander à l'utilisateur "entrer un prix"
    #  -> si il trouve le juste prix "C'est gagné !"
    #  -> sinon on affiche "c'est moins" ou "c'est plus"
    
    

import random
nb = random.randint(0,1000)

player=int(input("Veuillez choisir un nombre entre 0 et 1000: " ))

while player != nb:
    if nb < player:
        player=int(input("C'est moins: " ))
    if nb > player:
        player=int(input("C'est plus: "))
        
if player == nb:
    import turtle           # Importation du module turtle
turtle.up()             # tant que la tortue est en mode "up",
                        # son déplacement ne trace rien
turtle.shape('turtle')  # change la forme de la tortue (en tortue)
turtle.goto(-80,0)      # la tortue se place en coordonnées (-80,0)
                        # (-80 pour l'axe des "x" et 0 l'axe des "y")
turtle.color('black')   # la tortue est noire
turtle.down()           # tant que la tortue est "down",
                        # elle tracera la ligne de ses déplacements
turtle.begin_fill()     # va remplir l'intérieur de ce qui est tracé entre
                        # maintenant et le turtle.end_fill() ultérieur
turtle.forward(300)     # la tortue avance de 300 (à droite)
turtle.right(120)       # la tortue effectue une rotation à droite
turtle.forward(300)     # la tortue avance de 300 (à droite)
turtle.right(60)
turtle.forward(300)
turtle.right(120)
turtle.forward(300)
turtle.right(60)
turtle.forward(300)
turtle.end_fill()       # fin du premier lozange

    # retour de la tortue à ça place initiale
turtle.color('blue')    # la tortue devient bleu
turtle.begin_fill()     # va remplir l'intérieur en bleu

turtle.left(120)
turtle.forward(300)
turtle.left(60)
turtle.forward(300)
turtle.left(120)
turtle.forward(300)
turtle.end_fill()
    # Fin de la tortue bleu place à la tortue rouge
turtle.color('red')    # la tortue devient red
turtle.begin_fill()    # va remplir l'intérieur en rouge

turtle.right(60)
turtle.forward(300)
turtle.right(120)
turtle.forward(300)
turtle.right(60)
turtle.forward(300)
turtle.right(120)
turtle.forward(300)
turtle.end_fill()

turtle.hideturtle()
turtle.done()