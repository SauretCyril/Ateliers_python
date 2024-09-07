dictionnaire = {"Hello !" : "Bonjour !", " Thanks !" : "Merci !", "Bye !" : "Au revoir !"}
dictionnaire1 = dict([["a", 1], ["b", 2], ["c", 3], ["d", 4]])

liste = 'abcd'
dictionnaire2 = dict([(liste[i], i+1) for i in range(4)])
print (dictionnaire2 )

dictionnaire3 = dict(a=1, b=2, c=3, d=4)

print('-------- Add')

dictionnaire = {}
dictionnaire["pseudo"] = "user"
dictionnaire["mot de passe"] = "*"

print('-------- acceder')
cle="pseudo"
dictionnaire[cle]
print(dictionnaire["mot de passe"])

print('-------- update')
dico1 = dict([('abcdef'[i], i) for i in range(6)])
dico2 = dict(clé1=1,clé2=2,clé3=3)
dico1.update(dico2)
print(dico1)

print('-------- clear')
dico1 = dict([('abcdef'[i], i) for i in range(6)])
dico1.clear()
print(dico1)

print('-------- pop')
placard = {"chemise":3, "pantalon":6, "tee shirt":7}
print (placard.pop("chemise")) # Renvoie 3

print('-------- del')

placard = {"chemise":3, "pantalon":6, "tee shirt":7}
del placard["chemise"]
print(placard) # Renvoie

print('-------- values')
inventaire = {'pommes': 430, 'bananes': 312, 'oranges' : 274, 'poires' : 137}
print(inventaire.values())

print('-------- key')

print(inventaire.keys())


print('--------  Accéder aux clés')
for cle in inventaire :
    print("La clé %s est associée à la valeur %d" %(cle,inventaire[cle]))
    
print('--------   la liste des clés ')
print(f"keys {inventaire.keys()} - {type(inventaire.keys())}")

print('--------    Accéder aux clé et valeurs ')
for cle, valeur in dico1.items() :
 print("La clé %s est associée à la valeur %d" %(cle,valeur))
 
print('--------    test d\'appartennance ')
dico1 = dict([('abcdef'[i], i) for i in range(6)])
print('a' in dico1) # Renvoie True
print( 't' in dico1) # Renvoie False
print('t' not in dico1) # Renvoie True


 
print('--------   Set ')
set1 = {1, 1, 2}  # set1 correspond à {1, 2}
set2 = set([2, 2, 3])  # set2 correspond à {2, 3}

print('--------#RenvoieTruesi l’ensemble set1 n’a aucun élément en commun avec set2')
print (f"{set1}.isdisjoint({set2}) = {set1.isdisjoint(set2)}") #RenvoieTruesi l’ensemble set1 n’a aucun élément en commun avec set2

print('--------#si tous les éléments du set1 sont dans set2')
print (f"{set1}.issubset({set2}) = {set1 < set2}")

print('--------#Teste si l’ensemble set1 est un sous-ensemble de set2')
print (f"{set1}<{set2} = {set1 < set2}")


set1 = {3,1, 1}
set2 = set([1, 2, 3,4])
set3 = set([1,10, 2, 9,4])
print('--------#Teste si tous les éléments de set2 sont dans l’ensemble set1')
print (f"{set1}>{set2} = {set1 > set2}")

print('--------#Renvoie un nouvel ensemble dont les éléments viennent de l’ensemble set1 et de tous les autres')
print (f"{set1}.union({set2}|{set3} ) = {set1.union(set2|set2)}")

print('--------#Renvoie un nouvel ensemble dont les éléments sont commun à l’ensemble et à tous les  autres')
print (f"{set1}.intersection({set2}&{set3} ) = {set1.intersection(set2&set3)}")