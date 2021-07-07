# -*-coding:Utf-8 -*
print("hello")

######################EXERCICE 1###########################
# from random import *
# s=[]
# tailleliste=100
#
# nb_valeurs= int(float(input("Nombre de valeurs à tirer au hasard (défaut = 100)")))
# for i in range(nb_valeurs):
#     s.append(random())

###############################################################

from random import *
valeurs=[]
nb_valeurs=1000
nb_fractions=5
indice_fraction=0

nb_valeurs= int(float(input("Nombre de valeurs à tirer au hasard (défaut = 1000)")))
nb_fractions=int(float(input("Nombre de fractions dans l'intervalle 0-1 (entre 2 et 10, défaut = 5)")))

compteurs=[0]*nb_fractions

print("Tirage au sort des",nb_valeurs,"valeurs...")

for i in range(nb_valeurs):
    valeurs.append(random())
    if (indice_fraction*(1/nb_fractions) < valeurs[i] <= (indice_fraction+1)*(1/nb_fractions)):
        compteurs[indice_fraction]+=1
    else: indice_fraction+=1

print("Comptage des valeurs dans chacune des", nb_fractions, "fractions...")


print(compteurs)
