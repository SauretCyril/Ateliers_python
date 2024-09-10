#  Soit une liste de fichiers d’extension différentes ( .txt, .pdf, .py…)
#  ▪ Ecrire un programme qui retourne la liste des pdfs, en supprimant les extensions et en mettant en majuscule
#  ▪ indications: 
# ▪ Utiliser le slicing (chaine[i:j]) pour récupérer une partie d'une chaine
#  ▪ Utiliser la méthode upper pour mettre une chaine en majuscule
#  ▪ fichiers = ['f1.txt', 'f2.pdf', 'pdf.txt', 'f4.py', 'f5.pdf', 'f6.xpdf']



fichiers = ['f1.txt', 'f2.pdf', 'pdf.txt', 'f4.py', 'f5.pdf', 'f6.xpdf']
for fi in fichiers:file=fi[0:2].upper();print (file)
    
    