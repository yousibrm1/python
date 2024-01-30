#!/usr/bin/env python
# coding: utf-8

# ### la plate forme de Google qui permet de coder est googlecolab
#  dictionnaire de python sur les strutures des données:  https://docs.python.org/fr/3/tutorial/datastructures.html

# # Rappel sur les listes
# ## Exercice : Trouve et Remplace Automatiquement dans une Liste
# 
# ### Objectif :
# 
# 

# Écrire un programme Python qui parcourt une liste prédéfinie de nombres entiers, recherche un nombre spécifique dans cette liste, et remplace toutes ses occurrences par un autre nombre spécifié.

# ### Instructions :
# 
# Utilisez la liste suivante de nombres entiers : [12, 35, 12, 9, 56, 24, 35, 12, 89, 24, 35, 12].
# 
# #### Nombre à Rechercher et à Remplacer :
# 
# Définissez une variable pour le nombre à rechercher dans la liste. Par exemple, nombre_recherche = 12.
# Définissez une autre variable pour le nombre qui remplacera les occurrences trouvées. Par exemple, nombre_remplacement = 100.
# 
# #### Recherche et Remplacement :
# 
# Parcourez la liste avec une boucle. À chaque fois que le nombre_recherche est trouvé, remplacez-le par le nombre_remplacement.
# Affichage des Résultats :
# 
# Avant de commencer le processus de remplacement, affichez la liste originale.
# Après avoir effectué les remplacements, affichez la liste modifiée pour montrer les changements effectués.

# In[3]:


#solution de l'exercice
# 1--
liste_nombre = [ 12, 35, 12, 9, 56, 24, 35, 12, 89, 24, 35, 12 ]
nombre_cherche = 12
nombre_remplace = 100      #1- on parcourt la liste avec for

print("liste avant remplacement", liste_nombre)

for i in range(len(liste_nombre)):
    if liste_nombre[i] == nombre_cherche :
        liste_nombre[i] = nombre_remplace
        
print("liste après remplacement", liste_nombre)


# In[4]:


# 2- 

liste_nombre = [ 12, 35, 12, 9, 56, 24, 35, 12, 89, 24, 35, 12 ]
nombre_cherche = 12
nombre_remplace = 100      #1- on parcourt la liste avec for

liste_apres = liste_nombre

print("liste avant remplacement", liste_nombre)

cpt = 0   #compteur

for i in liste_apres :                # i=la valeur du nbr recherche
    if i == nombre_cherche :
        liste_apres[cpt] = nombre_remplace
        
    cpt+= 1 # équivalent à cpt = cpt +1 on incrimente le cpteur
        
print("liste après remplacement", liste_nombre)


# In[5]:


# on peut définir une foction

liste_nombre = [ 12, 35, 12, 9, 56, 24, 35, 12, 89, 24, 35, 12 ]
nombre_cherche = 12
nombre_remplace = 100      #1- on parcourt la liste avec for

print("liste avant remplacement", liste_nombre)

def remplacer (liste_nombre, nombre_cherche, nombre_remplace) :
    for i in range(len(liste_nombre)):
        if liste_nombre[i] == nombre_cherche :
            liste_nombre[i] = nombre_remplace
    return liste_nombre
        
print("liste après remplacement", liste_nombre)


# # Les dictionnaires

# ### Source: http://www.science-du-numerique.fr/comment-visualiser-une-structure-de-donnee-de-type-dictionnaire

# ### Un dictionnaire en Python est une collection d'éléments non ordonnée, modifiable et indexée. Chaque élément dans un dictionnaire est une paire clé-valeur, où chaque clé est unique.

# ### Avantage : les dictionnaires sont optimisés pour récupérer rapidement des valeurs lorsque vous connaissez la clé, ce qui les rend idéaux pour stocker des données qu'il est nécessaire de récupérer efficacement

# ## create
# 

# In[7]:


# creation d'un dictionnaire
depense_mensuelle = {"loyer" : 500, 
                      "divertissement" : 200,
                    " santé" : 100, 
                    "transport" : 20} # ici à chaque clé, une seule vleur
depense_mensuelle


# In[9]:


# type
type(depense_mensuelle)


# In[46]:


#utilisation en machine learning

param = {"nb_iteration" : 500,
                   "loyer" : 500, 
                   "nombre" : 200,
                   "santé" : 100, 
                   "transport" : 20} 
param


# In[19]:


# possiblité de créer dictio dans dictio

depense_janvier = {"loyer" : 500, 
                      "divertissement" : 200,
                    " santé" : 100, 
                    "transport" : 20}

depense_fevrier = {"loyer" : 500, 
                      "divertissement" : 2800,
                    " santé" : 100, 
                    "transport" : 70}

depense_mars = {"loyer" : 500, 
                      "divertissement" : 200,
                    " santé" : 100, 
                    "transport" : 69}

depense_annuelle = {"janvier" : depense_janvier,
                    "fevrier" : depense_fevrier, 
                    "mars" : depense_mars}

print(depense_annuelle)


# In[21]:


len(depense_annuelle)
len(depense_janvier)


# ## Read

# In[23]:


#lire unE clé
loyer = depense_mensuelle["loyer"]
print(loyer)


# In[35]:


depense_mensuelle["loyer"]


# In[24]:


#tester une autre clé
depense_mensuelle["TEMP"] #car la clé


# In[26]:


depense_mensuelle.get("loyer")


# In[36]:


#obtenir les clés dspos dans dictionnaires avec fonction keys
depense_mensuelle.keys()


# In[31]:


# acceder à une clé spécifique
depense_mensuelle[ list(depense_mensuelle.keys())[1]]


# In[32]:


#obtenir les valeurs
depense_mensuelle.values()


# In[34]:


#obtenir les items

depense_mensuelle.items()


# # Update
# je veux modifier une des valeurs, mise à jours

# In[37]:


#mettre à jour la valeur d'une clé dans le dictionnaire
# pour changer une valeur, j'identifie ma clé et je l'attribue la nvle valeur
depense_mensuelle["loyer"] = 600
print(depense_mensuelle)


# In[39]:


#ajouter une nvle info dans la base

depense_mensuelle["vetement"] = 400
print(depense_mensuelle)


# # delete

# In[40]:


#supprimer une clé
del depense_mensuelle ["vetement"]
print(depense_mensuelle)


# In[47]:


# pop sup l'info mais la stock dans une autre variable
transport = depense_mensuelle.pop("transport")


# In[48]:


print(transport)
print(depense_mensuelle)


# ## Utilisation des dictionnaires dans les boucles for 

# In[50]:


# for avec ls clé, ce qui est mis après for ça n'a pas d'importance, tu pe just mtre v

for keys in depense_mensuelle.keys():
    print(keys)


# In[51]:


# for avec des valeurs
for val in depense_mensuelle.values():
    print(val)


# # for avec les clés et les valeurs
# for keys, val in depense_mensuelle.items():
#     print("ceci est la", keys,"ceci est la", val)

# In[53]:


depense_mensuelle.items()


# ### on a vu comment on crée la dictio, la lire, la mettre à jour, supprime les infos, et comment on parcours un dictionnaire
# ### avec la boucle for

# # QUIZ

# Q1 - Comment accède-t-on à la valeur associée à la clé 'b' dans le dictionnaire suivant ? mon_dictionnaire = {'a': 1, 'b': 2, 'c': 3}
# 
# Options :
# 
# a) mon_dictionnaire(2)
# b) mon_dictionnaire[b]
# c) mon_dictionnaire['b']
# d) mon_dictionnaire.get('b')
# Q2 - Comment supprime-t-on une clé 'b' d'un dictionnaire mon_dictionnaire en Python ?
# 
# a) del mon_dictionnaire['b']
# b) mon_dictionnaire.remove('b')
# c) mon_dictionnaire.delete('b')
# d) remove mon_dictionnaire['b']

# In[54]:


# réponse1: c et d
mon_dictionnaire = {'a': 1, 'b': 2, 'c': 3}
mon_dictionnaire.get("b")


# In[56]:


mon_dictionnaire["b"]


# In[65]:


#reponse 
del mon_dictionnair["b"]


# # Listes en compréhension
# disponible Source: [https://www.freecodecamp.org/news/list-comprehension-in-python/)

# # Formule générale
# [nouvel element for element in list_original if condition]

# In[ ]:


# créer la liste des carrées des nombres de 0 à 99.


# In[67]:


#approche classique
liste_carre = []
for i in range(100) :
    liste_carre.append(i**2)  # avec append j'ajoute un élt à la dernière position d'une liste
print(liste_carre)


# In[68]:


#Définition en compréhension
liste_carre_com = [x ** 2 for x in range(99)] # je récuorère x dans range(99)
# l'utlité de liste en compréhen, ça ns permet de créer des liste à partir d'une seule ligne
print(liste_carre_com)


# In[72]:


# maintena on veut slma les nbre pairs, la reste de la divi euclidienne est 0
liste_carre_com_pair = [x ** 2 for x in range(99) if x%2 == 0] 

print(liste_carre_com_pair)
type(liste_carre_com_pair)


# In[74]:


# Transformer des noms en majuscules
liste_nom = ["jean", "paul", "marie"]
liste_nom_majus = [x.upper() for x in liste_nom] #qui permet de transformer une chaine de caract en majuscule
liste_nom_majus


# # Exercice liste en compréhension
#  Étant donné une liste de chaînes de caractères, par exemple mots = ["Bonjour", "le", "monde", "Python", "est", "génial"], créez une liste en compréhension qui contient la longueur de chaque mot dans la liste, mais seulement pour les mots qui ont plus de trois lettres.

# In[75]:


mots = ["Bonjour", "le", "monde", "Python", "est", "génial"]
#la fonction len qui me donne la taille des chaine
# on fait avec la liste en compréhention: [nouvel element for element in list_original if condition]
[x for x in mots if len(x)>3]


# # Dictionnaires en compréhension

# Source: [https://www.programiz.com/python-programming/dictionary-comprehension)

# ## Formule générale
# 
# {cle_expression: valeur_expression for element in iterable if condition}

# In[77]:


# Dictionnaire avec les nombres au carré de 0 à 99

dict_carre = {k:k**2 for k in range(0,99)}
print(dict_carre)


# In[78]:


# Dictionnaire uniquement avec les nombres pairs

dict_carre = {k:k**2 for k in range(0,99) if k%2 == 0} # le reste de la division euclidiene est ligne
print(dict_carre)


# ## Exercice
# 
# Considérer le dictionnaire suivant inventaire = {'pommes': 30, 'bananes': 15, 'cerises': 20} Creer un dictionnaire en compréhension qui va inverser les clés et les valeurs du dictionnaire inventaire

# In[80]:


inventaire = {'pommes': 30, 'bananes': 15, 'cerises': 20}
dict_inverse = {v: k for k, v in inventaire.items()} # items nous donne à la fois la clé et la valeur
print(dict_inverse)


# # Fonctions natives en Python
# La documentation des fonctions natives est disponible ici: https://docs.python.org/fr/3/library/functions.html

# In[81]:


#print
print("bonsoir")


# In[83]:


# format à connaitre
temperature = 25
ville = "marseille"
resultat = "la température à {} est de {} ". format(ville, temperature)
print(resultat)


# In[84]:


print("la température à",ville, "est de ",temperature)


# In[85]:


#input: qui permet de récuperer les infos de l'utilisateur
age = input("Quel est votre age?")


# In[88]:


print(age)
type(age)


# In[90]:


#transformer les string en integer
age_int =int(age)
print(age_int)
type(age_int)


# In[91]:


#abs: 
x = -5
abs(x)


# In[92]:


#round: arrondir
y = 1.08276
round(y)


# In[95]:


#max (liste) maximum d'une liste
liste=[4,6,8,9,6,1,3]
max(liste)


# In[94]:


min(liste)


# In[96]:


#sum: la somme
sum(liste)


# In[97]:


# all (vrai diff de zéro), en python 0 c'est vrai et ts les autres élts sont faux
all(liste)


# In[99]:


liste_bool=[False,True,False, False,True]
all(liste_bool)


# In[100]:


#any: au moins un qui est diff de zéro
any(liste_bool)


# In[101]:


#len: la taille d'un élément
len(liste_bool)


# In[103]:


#range:pour avoir des plages des valeurs
plage = range(0,199,6)
plage


# In[104]:


type(plage)


# In[109]:


# conversion list, tuple, dictionnaire
list(plage) # tranforme plage en liste
trans_tuple = tuple(plage)
trans_tuple


# In[108]:


# conversion  float, int
test = str(0)
test


# In[ ]:




