print ('---------- Récurcivité------------')
#Exemple : Calculer la factorielle d'un nombre : n!. 
#Rappel : n! = n*(n-1)

#3 3*2*1=6
#4 4*3*2*1=24
#5 5*4*3*2*1 = 120 
def factoriel(nombre) :
    if  nombre == 0 : # C'est le cas d'arrêt
        return 1
    else :
        return nombre * factoriel(nombre - 1)

print(factoriel(3))
