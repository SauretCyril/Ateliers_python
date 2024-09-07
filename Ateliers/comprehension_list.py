print ('------------Comprehension list--------')
entiers = [1, 3, 5, 6, 9]
multiples_trois_au_carre = [e**2 for e in entiers if e%3==0]

#extraire les multiples de 3 = (element puissance 2) modulo =0
print (f"extraire les multiples de 3= {multiples_trois_au_carre}")


def f(e):
    return e**2

def cdt(e):
    return e%3==0

def g(e):
    return e%3

nouvelle_liste = [f(e) if cdt(e) else g(e) for e in entiers] 
print (f"extraire les multiples de 3= {nouvelle_liste}")

#page 62 ->Dict & set compréhension ?
# Dict & set compréhension
#  ▪ Dict– {x: f(x) for x in seq if cdt(x)}
#  ▪ Set– {f(x) for x in seq if cdt(x)}
#  ▪ Generator– (f(x) for x in seq if cdt(x))