#---------------------#
#     EXERCICE 01     #
#                     #
#---------------------#


### Supposons que la matrice est deja remplis la fonction qui affecte cette matrice par une matrice idendite est : ###
##q1 :
T_colonnes=len(M) Height
T_lignes=len(M) Width
def Remplir_Matrice_Identite(M):
  if T_colonnes == T_lignes:
    for i in T_colonnes:
        for j in T_lignes:
            if i==j:
                M[i][j]=1
            elif i<>j:
                M[i][j]=0
##q2 :
def Affichage(M):
  if T_colonnes == T_lignes:
    for i in T_colonnes:
        for j in T_lignes:
            print(M[i][j]+' ')
    print('\n')       


##PROGRAM PRINCIPALE:
print('Enter l'ordre de la matrice')
O = input()
##tjr supposons que la matrice existe et carre 
T_colonnes=O
T_lignes=O
Remplir_Matrice_Identite(M)
Affichage(M)

















