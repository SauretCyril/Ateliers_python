


print ('----------Passage d\'arguments-------')
a = 2
def f(x):
    x += 1
    return x

a = f(a); print(a)

print ('----------Les arguments-------')
def puissance(nombre, exposant=2) :
    return  nombre ** exposant 
print(puissance(3, 4)) # Renvoie 27
print(puissance(3)) # renvoie 9

print ('---Appel désordonné-------')
print(puissance(exposant=4, nombre=3)) # Renvoie 81

print ('--- Nombre indéfini d\'arguments-------')
def fonction(*arguments) :
    for element in arguments :
        print(element)
    
print (fonction(43, 38, "Bonjour !", True)) # Renvoie 43 38 Bonjour ! True


print ('--- arguments **kwargs-------')
def fonction(**kwargs) :
 print(kwargs)

fonction(a=1, b=2, c=3)