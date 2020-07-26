#---------------------#
#     EXERCICE 02     #
#                     #
#---------------------#

## le but c'est de poser une valeur approxmatif de E en utilisant une somme partielle

##il nous faut de definir la foction factorielle:
def factorial(n):
    if n == 0:
        return 1
    else:
        ##une recursion simple##
        return n * factorial(n-1)

e=0
print('enter la valeur de n :')
n=input()
i=0
while i<n:
 e=e+(1/factorial(i))
 i=i+1
print("l'approximation de e est :"+e)


