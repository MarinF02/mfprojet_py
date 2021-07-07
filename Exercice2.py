# -*-coding:Utf-8 -*
print("hello")

# 1. Écrire un algorithme qui demande un entier positif, et le rejette tant que le nombre saisi n’est pas conforme.

# a = -1
# while(a<0):
#     a = int(float(input("Entrez un entier positif")))
#     if a<0:
#         print("Le nombre n'est pas positif")
#     else : print("Le nombre est positif")
#



# 2. Écrire un algorithme qui demande 10 entiers, compte le nombre d’entiers positifs saisis, et affiche ce résultat.

# p=0
# c=0
# while (c<10):
#     b = int(float(input("Entrez un entier")))
#     if b>0 :
#         p=p+1
#     c=c+1
# print(p,"nombres positifs")






# 3. Écrire un algorithme qui demande des entiers positifs à l’utilisateur, les additionne, et qui s’arrête en affichant le
# résultat dès qu’un entier négatif est saisi.

# c=0
# d=1
# while(d>0):
#     d = int(float(input("Entrez un entier positif")))
#     if(d>0):
#         c=c+d
#     else : print("Un nombre négatif a été saisi --> STOP")
# print("somme : ",c)





# 4. Modifier ce dernier algorithme pour afficher la moyenne de la série d’entiers positifs saisis.

c=0
cpt=0
d=1
while(d>0):
    d = int(float(input("Entrez un entier positif")))
    if(d>0):
        c=c+d
        cpt=cpt+1
    else : print("Un nombre négatif a été saisi --> STOP")
m=c/cpt
print("somme : ",c)
print("moyenne : ",m)