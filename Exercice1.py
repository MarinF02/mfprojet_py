# -*-coding:Utf-8 -*

#1. Écrire un algorithme qui demande un entier à l’utilisateur, teste si ce nombre est positif (>= 0) ou non, et affiche
#“positif” ou “négatif”.

#a = input("Entrez un nombre entier")
#if int(a) >=0 : print("positif")
#else : print("négatif")




#2. Écrire un algorithme qui demande un entier à l’utilisateur, teste si ce nombre est strictement positif, nul ou strictement
#négatif, et affiche ce résultat.

#b = input("Entrez un nombre entier")
#if int(b)>0 : print("positif")
#elif int(b)<0 : print("négatif")
#else : print("nul")




#3. Écrire un algorithme qui demande un réel à l’utilisateur et affiche sa valeur absolue (sans utiliser de fonction
#prédéfinie évidemment).

#c = input("Entrez un nombre réel")
#if int(c)>=0 : print(c)
#else : print(int(c)-int(c)-int(c))




#4. Écrire un algorithme qui demande un réel à l’utilisateur et l’arrondit à l’entier le plus proche (les x,5 seront arrondis
#à l’entier supérieur).

#d = input("Entrez un nombre réel")
#d_ent = int(float(d))
#d_deci = int(float(d)) - d_ent
#d_sup =d_ent+1
#if d_deci<0.5 : print(d_ent)
#else : print(d_sup)




#5. Écrire un algorithme qui demande le numéro d’un mois et affiche le nombre jours que comporte ce mois (sans tenir
#compte des années bissextiles).

#e = input("Entrez le numéro d'un mois")
#if int(e)==2 : print("28 jours")
#elif int(e)==10 : print("31 jours")
#elif int(e)==12 : print("31 jours")
#elif int(e)==9 : print("30 jours")
#elif int(e)==11 : print("30 jours")
#elif int(e)==8 : print("31 jours")
#elif int(e)%2 !=0 : print("31 jours")
#else : print("30 jours")




#6. Écrire un algorithme qui vérifie si une année est bissextile. On rappelle qu’il y a des années bissextiles tous les
#4 ans, mais la première année d’un siècle ne l’est pas (1800, 1900 n’étaient pas bissextiles) sauf tous les 400 ans
#(2000 était une année bissextile).

#f = input("Entrez une année")
#if int(f)%100==0 :
#    if int(f)%400==0 : print("année bissextile")
#    else : print("année non bissextile")
#elif int(f)%4==0 : print("année bissextile")
#else : print("année non bissextile")




#7. Écrire un algorithme qui demande une date sous la forme de 2 nombres entiers (numéro du jour et numéro du mois)
#et affiche la saison (ex : 12/02; hiver). On supposera que le premier jour de la saison est toujours le 21.
j = input("Entrez un jour (nombre entier)")
m = input("Entrez un mois (nombre entier)")
if int(m)<3 : print("hiver")
elif int(m)==3 :
    if int(j)<21 : print("hiver")
    else : print("printemps")
elif int(m)<6 : print("printemps")
elif int(m)==6 :
    if int(j)<21 : print("printemps")
    else : print("été")
elif int(m)<9 : print("été")
elif int(m)==9 :
    if int(j)<21 : print("été")
    else : print("automne")
elif int(m)<12 : print("automne")
elif int(m)==12 :
    if int(j)<21 : print("automne")
    else : print("hiver")