import classABR as A
import random
import turtle as t



### Fonction créant la labyrinthe
def all_case(n,m):
    """
        prend en entrée la longueur et la largeur du labyrinthe
        et créer une liste de liste contenant toute les positions
    """
    rep=[]
    for i in range(n):
        for y in range(m):
            rep.append([i+1,y+1])
    return rep

def TF(a):
    """
        fonction prenant en entrée un nombre et renvoie un nombre au hasard entre celui ci
        et 0 . Fonction ayant pour unique but de ne pas réécrire random.randint(0,a) à chque fois
    """
    return random.randint(0,a)


def neighbour(AB,liste):
    """
        prend en entrée: AB-> une liste comprenant 2 int
                         liste -> tab contenant toute les coordonnées ( obtenue via
                         all_case(n,m))
        renvoie : lst -> une liste contenant toutes les coordonées voisine d'AB

    """
    lst=[]
    # ajoute à une liste toute les coordonéers voisine de AB si elle sont présente dans la liste
    #des coordonnées
    haut=[AB[0],AB[1]+1]
    if haut in liste:
        lst.append(haut)

    bas=[AB[0],AB[1]-1]
    if bas in liste:
        lst.append(bas)

    gauche=[AB[0]-1,AB[1]]
    if gauche in liste:
        lst.append(gauche)

    droit=[AB[0]+1,AB[1]]
    if droit in liste:
        lst.append(droit)

    return lst




def choix(lst):
    """
        prend en entrée : lst -> liste contenant les voisins de la racine
        renvoie : choose -> valeur qui sera ajouter à l'arbre
                  lst -> liste contenant les voisins de la racine - la valeur choisie
        Fonction qui choisie au hasard dans une liste une valeur
    """
    choose=None
    if lst !=[]:#si il reste des voisins non utiliser
        i=len(lst)-1
        index=TF(i)
        choose=lst[index]#chosis au hasard parmi les voisins
        lst.remove(choose)#supprime l'heureux élu dans la liste des voisins
    return choose,lst



def lymbirith(arbre,liste):
    """
        prend en entrée: arbre -> un arbre binaire de recherche
                         liste -> liste contenant toute les coordonnées du labyrinthe
        renvoie en sortie : la même chose mais modifier
        fonction réccursive qui génère le labyrinthe, celle ci part d'un point et explore tout le
        chemin puis remonte et recherche tous les chemins possible selon les valeurs restantes
        dans la liste liste
    """
    #génère la liste contenant toute les valeures voisine à la racine
    racine_arbre=arbre.racine
    lst=neighbour(racine_arbre,liste)

    if not lst==[] : #si la liste des voisins n'est pas vide
        choose,lst=choix(lst) # en choisi la future racine
        if choose in liste:
            liste.remove(choose) # supprime la valeur choisie de la liste de coordonées
            arbre.filsG=A.ABR(choose[0],choose[1])#créer un fils gauche de type arbre
            lymbirith(arbre.filsG,liste)#récursivité
    if not lst==[] :
        choose,lst=choix(lst)
        if choose in liste:
            liste.remove(choose)
            arbre.filsD=A.ABR(choose[0],choose[1])
            lymbirith(arbre.filsD,liste)
    else:
        return arbre , liste



def generer(n,m):
    """
        prend en entrée : n et m -> longueur et largeur du labyrinthe
        en sortie : arbre -> arbre contenant la labyrinthe
        fonction qui lance la fonction récursive

    """
    liste=all_case(n,m)# les coordonnées

    #créer l'arbre
    start=[1,random.randint(1,m)]
    liste.remove(start)
    arbre=A.ABR(start[0],start[1])
    #fonction récursive
    lymbirith(arbre,liste)
    return arbre


### Fonction du traçage du labyrinthe

def grille(n, m):
    """
        prend une largeure et une longueur et trace une grille via turtle
    """
    tur=t.Turtle()
    t.speed(10)
    t.penup()
    t.goto(0,0)
    t.pendown()
    for _ in range(2):
        t.forward(n*20)
        t.left(90)
        t.forward(m*20)
        t.left(90)

    t.left(90)
    for i in range (n):
        t.penup()
        t.goto(i*20,0)
        t.pendown()
        t.forward(m*20)
    t.right(90)
    for i in range (m):
        t.penup()
        t.goto(0,i*20)
        t.pendown()
        t.forward(n*20)
    t.left(90)




def parcourgraph(arbre):
    """
        prend en entrée un arbre
        trace le labyrinthe
    """
    #reagrde la racine actuelle
    racine_actuelle=arbre.racine
    u=[a,b]=racine_actuelle[0],racine_actuelle[1]

    #parcours de l'arbre
    if arbre.filsG != None:
        racine_actuelleG=arbre.filsG.racine
        v=[racine_actuelleG[0],racine_actuelleG[1]]
        difference(v,u)


        parcourgraph(arbre.filsG)

    if arbre.filsD != None:
        racine_actuelleD=arbre.filsD.racine
        w=[racine_actuelleD[0],racine_actuelleD[1]]
        difference(w,u)
        parcourgraph(arbre.filsD)
    return


def difference(u,v):
    """
        prend en entrée u et v repsectivement la racine et l'un des deux fils
        fait la diférence des deux et selon le résultat repasse sur le mur en blanc
    """
    c=[u[0]-v[0],u[1]-v[1]]
    t.color("white")
    t.penup()
    if c==[0,-1]:#mur haut (n,m+1)
        t.goto((u[0]-1)*20,(u[1]-1+1)*20)
        t.pendown()
        t.right(90)
        t.forward(1*20)
        t.left(90)
        t.penup()




    if c==[0,1]:#mur bas (n+1,m)
        t.goto((u[0]-1+1)*20,(u[1]-1)*20)
        t.pendown()
        t.right(270)
        t.forward(1*20)
        t.left(270)
        t.penup()




    if c==[-1,0]:#mur droite (n+1,m+1)
        t.goto((u[0]-1+1)*20,(u[1]-1+1)*20)
        t.pendown()
        t.right(180)
        t.forward(1*20)
        t.left(180)
        t.penup()




    if c==[1,0]:#mur gauche (n,m)
        t.goto((u[0]-1)*20,(u[1]-1)*20)
        t.pendown()
        t.forward(1*20)
        t.penup()

    t.penup()
    return


def forme_(n,m):
    """
        prend en entrée la largeure et la longueur du labyrinthe et trace la forme
    """
    t.color("black")
    t.penup()
    t.goto(0,0)
    t.pendown()
    for _ in range(2):
        t.forward(m*20)
        t.right(90)
        t.forward(n*20)
        t.right(90)

    t.right(180)
    t.penup()




### Fonction concernant la résolution du labyrinthe et son traçage

def solution(arbre,end,lst=[]):
    """
        prend en entrée: arbre-> le labyrinthe
                         end-> arrivée du labyrinthe
                         lst-> une liste vide
        en sortie : lst-> la liste contenant lz chemin le plus court de la sortie à l'entrée
        Simple parours en profondeur , a partir du moment où la racine est égale à end , remonte
        et ajoute dans la liste toutes les racines.

    """
    if arbre.racine == end:
        lst.append(arbre.racine)

    #parcours
    if end not in lst and arbre.filsG!=None:
        lst=solution(arbre.filsG,end,lst)
    if end not in lst and arbre.filsD!=None:
        lst=solution(arbre.filsD,end,lst)


    if end in lst:
        lst.append(arbre.racine)
    return lst





def tracer_solution(lst):
    """
        prend en entrée: lst-> la liste contenant la soloution du labyrinthe
        trace la solution depuis la sortie jusqu'à l'entrée
    """
    t.color("red")
    t.penup()
    t.goto((lst[1][0]-1)*20+10,(lst[1][1]-1)*20+10)#place le curseur au milieu de la case de la sortie
    t.pendown()
    t.left(180)
    for i in range(1,len(lst)-1):
        a=[lst[i][0]-lst[i+1][0],lst[i][1]-lst[i+1][1]]#différence entre l'élement actuelle de la liste et le suivant , permet de déterminer la direction

        if a==[1,0]:#vers la gauche
            t.left(90)
            t.forward(1*20)
            t.right(90)

        if a==[-1,0]:#vers la droite
            t.right(90)
            t.forward(1*20)
            t.left(90)

        if a==[0,1]:#vers le bas
            t.right(180)
            t.forward(1*20)
            t.left(180)

        if a==[0,-1]:#vers le haut
            t.forward(1*20)




### Fonction principale


def laby(n,m):
    """
        Fonction principale permettant de tracer la labyrinthe
        ATTENTION N'oublie pas d'indiquer si vous voulez ou non la solution Oui=o et Non=n
        prend en entrée: n et m -> réspectivement la lageure et la longeure du labyrinthe
    """
    soluce="r"
    while not (soluce=="o" or soluce=="n"):
        soluce=input("Voulez vous la solution ? o/n \n")
    abr=generer(n,m)
    t.update()
    grille(n,m)
    parcourgraph(abr)
    forme_(n,m)
    #start et end
    start=abr.racine
    end=[n+1,random.randint(1+1,m+1)]
    #trace l'entrée et la sortie
    #start
    t.goto((start[0]-1)*20,(start[1]-1)*20)
    t.color("white")
    t.pendown()
    t.right(180)
    t.forward(1*20)
    t.left(180)
    t.penup()
    #end
    t.goto((end[0]-1)*20,(end[1]-1)*20)
    t.pendown()
    t.color("white")
    t.forward(1*20)

    #solution
    if soluce=="o":
        chemin=solution(abr,[end[0]-1,end[1]-1])
        tracer_solution(chemin)
    t.done()


