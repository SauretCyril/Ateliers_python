
def f(l,word):
    word.count(l)
    


dicL={}
chaine='aaaeed'
for l in chaine:
    if not dicL.get(l):
       dicL[l]=chaine.count(l)
     
print(dicL)