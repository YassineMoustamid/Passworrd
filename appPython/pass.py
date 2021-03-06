
i=1
while i<=5:
    pwd=input("saisir votre mot de passe")
    if pwd=="yassine123":
        print("Bienvenue ,yassine")
        break
    elif pwd!="yassine123":
        print("le mot de passe incorrect!")
        i=i+1 
else:
    print("Erreur! vous avez depassé le nombre de tentavies possibles!") 
        
    
    