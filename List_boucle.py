liste=['lundi','mardi','mercredi','jeudi','vendredi','samedi','dimanche']
liste1=[2,4,1,25,12,4,7]


print('--- while---') 
i = 0
while i<len(liste) :
    print(liste[i])
    i += 1
    
print('--- for---')
for element in liste :
 print(element)
 
print('---  fonction enumerate ---')
for i,element in enumerate(liste1) :
    liste1[i] += 100
    print(liste1[i]) # Renvoie l'élément initial + 100
    print(element) # Renvoie l'élément initial
    