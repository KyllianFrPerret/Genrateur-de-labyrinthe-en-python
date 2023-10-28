import File as F

class ABR():
    def __init__(self,a,b):
        """
            Créer un arbre vide.
        """
        self.racine = [a,b]#prend en racine un couple de valeur( position sur un plan)
        self.filsG = None
        self.filsD = None

    def parcours_largeur(self):
        result=[]
        f=F.File()
        F.Enfiler(f,self)
        while not F.FileVide(f):
            elt,f=F.Defiler(f)
            if elt.filsG != None:
                F.Enfiler(f,elt.filsG)
            if elt.filsD!= None:
                F.Enfiler(f,elt.filsD)
            result.append(elt.racine)
        print(result)
        return result

    def parcoursProfondeurInfixe(self,rep=[]):
        if self.filsG != None:
            self.filsG.parcoursProfondeurInfixe(rep)
        rep.append(self.racine)
        if self.filsD != None:
            self.filsD.parcoursProfondeurInfixe(rep)
        return rep


    def traiter(self):
        print(self.racine, end="  ")



    def inserer(self,elt,elt2):
        """
            prend en entrée : elt et elt2 -> deux éléments nécessaire à la construction d'arbre
                                             binaire
            Fonction qui permet de créer un arbre bianire manuellement en chosissant ou va la
            valeur en entrant "g" ou "d"
        """
        print("\n",elt)
        self.parcours_largeur()
        a=input ("g ou d \n")
        if a== "g":
            if self.filsG == None:
                self.filsG = ABR(elt,elt2)
            else:
                self.filsG.inserer(elt,elt2)
        elif a=="d":
            if self.filsD == None:
                self.filsD = ABR(elt,elt2)
            else:
                self.filsD.inserer(elt,elt2)



    # str , celui ci permet de mieux comprendre et lire des arbres binaires
    # très utile lors des tests
    def __str__(self):
            rep=[self.racine,"_","_"]
            rep=self.parcoursProfondeu(rep)
            return str(rep)

    #fonction qui place les élements de l'arbre dans une liste [racine,filsG,filsD]
    def parcoursProfondeu(self,rep):
        rep[0]=self.racine
        if self.filsG != None:
            rep[1]=self.filsG.parcoursProfondeu(["_","_","_"])
        if self.filsD != None:
            rep[2]=self.filsD.parcoursProfondeu(["_","_","_"])
        return rep

