print("--- Accès à un élément")
liste1 = ['lundi', 'mardi', 'mercredi']
print(liste1[:2]) # Renvoie ['lundi', 'mardi']

print("--- Les références")

L = [1,2,3]
M = ['x',L,'y']

print(M) # Renvoie ['x', [1, 2, 3], 'y']
L[2]=5
print(M) # Renvoie ['x', [1, 2, 5], 'y']

M = ['x',L[:],'y']
print(M) # Renvoie ['x', [1, 2, 3], 'y']
L[2]=0
print(M)

