
# En utilisant la fonction input, écrire un programme qui propose de saisir le nom est renvoie « Bonjour nom ! »
#  ▪ Ajouter au programme précédant la prise en compte du genre et renvoyer « Bonjour genre nom »
#  ▪ Limiter le choix du genre en proposant de choisir un code (1) pour madame et (2) pour monsieur.
#  ▪ Prendre en compte l’heure, pour afficher bonjour ou bonsoir

from datetime import datetime


#print (now)
#print (now.hour)

name=input("quel est votre nom ?: ")
genre=input("Votre Genre (1=Femme , 2=Homme ): ")


if int(genre)   == 1:
   genre="Madame"
elif int(genre) == 2:
   genre="Mosieur" 
else:
    print("Veuillez saisir un chifre 1 ou 2 !")
now = datetime.now()
hour = now.hour



formatted_date = now.strftime("%A, %d %B %Y")
if hour >17:
     poli ="Bonsoir"
else:
     poli ="Bonjour"

print(f"{poli} {genre} {name} il est {hour}h, nous sommes le {formatted_date}")
    
