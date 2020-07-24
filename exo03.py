import random
#---------------------#
#     EXERCICE 03     #
#                     #
#---------------------#
#init
L = []
##definition de la fonction
def REMPLIR_LISTE(n):
    for i in range(1,n):
        nbr_aleatoire = random.randint(-20,20)
        L.append(nbr_aleatoire)
return L
#   q2
def REMPLACER_NEGATIF_CARRE():
    for i in range(L):
        if L[i]<0
           L[i]=L[i]*L[i]


#program principale
L = []
n=input()
REMPLIR_LISTE(n)
print(L)
REMPLACER_NEGATIF_CARRE()
print("la nouvelle list apres le remplacement est :"+L)



           




