#!/usr/bin/env python
# coding: utf-8

# ## Les Modules et les packages en python
# qd on crée une fonction, la puissance de la fonc on est caoable de l'utiliser dans d'autre besoins, juste appeler la fontion qui a été créée
# 
# ## les modules en python
# un module= un fichier python qui contient la def de plusieurs fonctions qu'on peut réutiliser dans plusieurs prog
#  Si on parle des modules,c'est un fichier d'extention .py qui contient plusieurs fonctions qu'on peut utliser dans plusieurs projet . 
# les modules, si on a fait un projet x en entreprise au paravant et dans le prjet Y j'ai envie d'utliser une fonction que j'ai déja utlisé et c'est mainte 
# 
# ### Créer son propre module

# In[ ]:


#création: on vient de créer sur spyder


# In[21]:


#importation et renommer tout le module: importer veut dire je veux utiliser l'ens de mes fonctions qui y sont dispo 

import description as desc  #descrip as desc : c'est une façon de renommer le fichier


# In[22]:


#création une liste

CA = [3000, 4000, 5000, 6000, 10000]


# In[24]:


#application. Je pe utliser cette fonction dans plusieurs projet,
statdes = desc.statdescriptive(CA)
print(statdes)


# ## grace au module,pour pouvoir calculer la stat desc sur  la variable CA, j'ulise 2 lignes de code,car on a deja preparer mes codes dans un fichier separer. Voir la module comme une possibilité d'organiser son programme, avoir le programme plus clair et plus simple possible

# In[26]:


#soe du CA
somme_ca = desc.somme_element(CA)
somme_ca


# In[27]:


# importer une partie

from description import statdescriptive


# In[28]:


statdescriptive(CA)


# In[29]:


# si on peut faire la somme, ça refuse, car on a pas importer si on veut, on ajoute
somme_element(CA)


# # Modules Externes

# Exemple de structure ici: https://docs.python.org/fr/3/tutorial/modules.html#
# 
# Ensemble des modules https://docs.python.org/3/py-modindex.html

# ### On a la possibilité d'importer des modules externes developpées pa d'autres personnes, les liens ci-dessus

# ### Quelques modules utiles en data science
# 
# ###### math:  Pour les fonctions mathématiques de base.
# ###### statistics Pour faire des statistiques
# ###### os: Pour interagir avec le système d'exploitation, comme la gestion des chemins de fichiers et les commandes du système d'exploitation.
# ###### sys: Fournit un accès à certaines variables et fonctions qui interagissent fortement avec l'interpréteur Python.
# ###### json: Pour la lecture et l'écriture de données au format JSON.
# ###### csv: Pour lire et écrire des fichiers CSV.
# ###### datetime: Pour manipuler les dates et les heures.
# ###### random: Pour la génération de nombres aléatoires.
# ###### re: Pour les expressions régulières, utiles dans le traitement de texte et le nettoyage des données.
# ###### sqlite3: Pour la gestion de bases de données SQL légères.
# ###### pickle: Pour la sérialisation et la désérialisation de structures de données Python.

# In[30]:


#Exemple d'utilisation du module math
import math   #ici je peux ne pas renommer, math en soi deja assez court


# In[35]:


#pour afficher tout en mm temps, on met print
print("racine carré",math.sqrt(4))
print("sinus:",math.sin(90))
print("exponentielle",math.exp(90))


# In[36]:


#Exemple d'utilisation du module stat
import statistics as st


# In[38]:


st.mean([30, 50, 70])


# In[39]:


st.mode([30, 50, 70])


# 
# ### On a souvent en tant que Dataanalyste avoir besoin de generer des nombres aléatoires,random qui permet de faire ce travail

# In[40]:


#Exemple d'utilisation du module random(choice, seed, sample, randint, shuffle)
import random


# In[42]:


#choisir un élement aléatoire dans une lite(liste de nom)
liste_nom = ["Rodriguez", "Tsunami", "Youssouf", "Armand"]
random.choice(liste_nom)


# ### losqu'on travaille en tant que Analyste, on a besoin de choisir aléatoirement mais de fixer l'aléa, si une personne prend le code et lance aléatoirement un nom da la liste, il faut qu'il soit capable de récuperer le nom que j'ai  choisie et pour faire cela on besoin de la fonction seed

# In[45]:


# fixer la raine (seed), au debut de mon algo, au lieu de géner aléatoirement , je choisie random, avec seed,
# je suis capable de controler mon seed
random.seed(23333)
#choisir un élement aléatoire dans une lite(liste de nom)
liste_nom = ["Rodriguez", "Tsunami", "Youssouf", "Armand"]
random.choice(liste_nom)


# In[46]:


random.sample(liste_nom,2)


# In[47]:


#aléatoie float (random.random)
random.random()


# In[48]:


#alearoire  integer
random.randint(1,100)


# In[51]:


#mélanger aléatoirement des données dans une liste(shuffle): En gros on a liste au départ(liste est ordonnée),
# shuffle permet de changer aléatoirement 

random.shuffle(liste_nom)
liste_nom



# # Packages
# est une fonction qui contient plusieurs modules

# Lien pour en sarvoir plus https://packaging.python.org/en/latest/tutorials/packaging-projects/

# ## utlisation de mon packages 

# In[53]:


import monpackage.module as md


# In[54]:


md.statdescriptive


# In[55]:


# une autre façon d'importer
from monpackage import module


# In[56]:


#liste des packages dispo dans, pour avoir les noms

get_ipython().system(' pip list')


# trouver des packages disponibles ici: https://pypi.org/

# In[57]:


#installer un package 
get_ipython().system('pip install dash')


# In[58]:


#installer un package 
get_ipython().system('pip install tensorflow')


# In[60]:


#une fois installer, comment on peut l'utiliser?  il suffit juste de l'importer

import numpy as np


# # QCM

# ## Q1, Quelle est la principale différence entre un module et un package en Python ?
# A. Un module est une collection de fonctions, tandis qu'un package est une collection de modules.
B. Un module est un fichier contenant du code Python, tandis qu'un package est un dossier contenant un ou plusieurs modules.
C. Un module ne peut pas être importé, tandis qu'un package peut être importé dans d'autres scripts Python.
D. Il n'y a pas de différence; les termes module et package sont interchangeables en Python.

Question 2

Considérons le package mypackage contenant deux modules : module1 et module2. Comment importeriez-vous une fonction nommée myfunction du module1 ?

A. import mypackage.module1.myfunction
B. from mypackage import module1.myfunction
C. from mypackage.module1 import myfunction
D. import myfunction from mypackage.module1
# In[61]:


#from mypackage.module1 import myfunction
from monpackage.description import statdescriptive


# # Travailler avec les fichiers

# https://docs.python.org/fr/3/library/functions.html#open

# ## Open

# In[62]:


#ecrire dans le fichier et créer le fichier(1er approche)
f = open("resultat.txt", "w")
f.write("Bonjour")
f.close()


# In[64]:


#pour lire
f = open("resultat.txt", "r")
f.read()


# In[67]:


#Ecriture 2ème approche

with open("resultatbisv2.txt", "w") as f:
    for i in range(0,10):
        f.write(f"La valeur est {i}\n")


# In[71]:


# Lecture deuxième approche (readlines et read().splitlines())
with open("resultatbisv2.txt", "r") as f:
    resultat = f.readlines()
resultat


# # Bien démarrer avec Numpy
# ## Bien démarrer avec une dimensions (Create)
# si on a un objet, il y'a l'accronyme CRUD, comment je crée un tableau,...
# la puissance de numpy on fait des matrices

# In[72]:


#ipmportation
import numpy as np


# In[73]:


#création d'un nd array à une dim à partir d'une liste
tableau_dim1 = np.array([33,4,66,8,9])
tableau_dim1


# In[79]:


tableau_dim1 = np.array([[33,4,66,8,9],[33,4,66,8,9],[33,4,66,8,9]])
tableau_dim1


# In[80]:


# dimention
tableau_dim1.shape


# In[75]:


#taille
tableau_dim1.size


# ## Créer un nompy array à partir des fonctions integrées
# 

# In[76]:


#tableau avec des zéros
tableau_zero = np.zeros((2,2))
tableau_zero


# In[81]:


tableau_zero = np.zeros((7,8))
tableau_zero


# In[82]:


tableau_one = np.ones((2,2))
tableau_one


# In[83]:


#créer une matriseidentité
tableau_eye = np.eye(3)
tableau_eye


# In[ ]:


#Créer un numpy array avec la fonction arange: pour créer des nombre entre le minimum et le maximum avec un pas


# In[86]:


np.arange(0,10,1)


# In[87]:


#Créer un numpay array avec la fonction linspace #générer une séquence de nombre # Très utile pour les graphiques
#entre deux valeurs données avec un nombre de points donné
np.linspace(0,1,50)


# In[88]:


np.linspace(0,1,1000)


# In[89]:


np.linspace(0,1000,50)


# In[ ]:


# Créer un numpy array de valeurs aléatoires avec la fonction random avec np.random.random
np.random


# # Accéder aux éléments, sélectionner (Read)

# In[90]:


# Accès aux éléments
# Création d'un nd array à une dimension à partir d'une liste
tableau_dim1 = np.array([33,4,4,5,6,4,3,11])
tableau_dim1


# In[91]:


tableau_dim1[-1]


# In[97]:


# Sélection des éléments qui respectent une condition
tableau_dim1[tableau_dim1 >6]


# In[99]:


tableau_dim1[tableau_dim1 >3]


# In[98]:


tableau_dim1 >3


# In[95]:


# utilisation de np.where(): la possiblité de filtrer 
np.where(tableau_dim1>10)
nb_superieur_10 = tableau_dim1[np.where(tableau_dim1>10)]
nb_superieur_10


# # Fonctions mathématiques et statistiques avec Numpy

# #les suites dans un autres fichier
# #module: un fichier dans lequel on crée des fonction qui sont réutilisable dans plusieurs autres applications
# #il ya des modules on crée en interne et y'a d'autres on les crée en externe
# ##les packages sont des dossiers qui contient plusieurs modules: 
# -pypi.org: dans lequel on trouve l'ensemble des packages disponible sur python
#     -fichier: sera le modele
#         -numpy: il nous permet de travailler sur np.array: le tablo en plusieurs dimentions(np.where,np.liste)

# In[ ]:




