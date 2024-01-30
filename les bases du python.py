#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("bonjour Youssouf")


# ## les bases de python

# ## bien demarrer avec python

# In[3]:


nombre=5
print(nombre)


# # Syntaxe de base
# 

# ## comment ecrire un code propre et lisible en python
# 

# In[4]:


#En programation en général il y'a des règles à respecter, en python, 
#il y'a la convention PEP8(qd on écrit des variables, on se rassure 
#chaque fois que les noms variables commence tjrs par un caractère, 
#le nom de la variable doit signifier quelques chose, qd on code 
#on ne code pas pour soi 
nom_abonnées= "Ronald"
print(nom_abonnées)


# In[5]:


# variables intiger= entier
nombre_vidéos=200
print(nombre_vidéos)


# In[6]:


#en python, pas besoin de mettre le type car python est un langage qui
# n'est pas typé.
taille_abonnées=1.7
print(taille_abonnées)


# # Différents type de données
# 
# # Types Intégrés : Utilisez 
# int(=integer, c'est entier), float(nbre décimaux), str(c'est caractère, noms des abonnées), et list pour représenter les différents type de données.
# si on a une variables dans ntr code et on veut savoir son type, il suffit d'écrire: type(noms d'abonnee pa exemple) et exécuter, ça va nous afficher.
# Vérification de Type: La fonction type() permet de vérifier le type 
# d'une variable.
# Opérations de Base: Effectuez des opérations comme l'addition de int, 
# ou la concaténation de str.

# In[7]:


type(taille_abonnées)


# In[9]:


bool= False
print(bool)


# In[10]:


bool= True
print(bool)


# In[11]:


temp= True
print(temp)


# In[12]:


str(temp)


# ### python est sensible à la case, lorsqu'on écrit en majuscule on doit 
# ### se rassurer c'est une majuscule

# Opérations Arithmétiques Simples:
# 
# Opérations de Base: Addition +, soustraction -, multiplication *, et division /.
# Opérations Avancées: Division entière //, modulo %, et puissance **.
# Priorité: Python suit l'ordre opérationnel mathématique standard

# In[21]:


#addition
x=5
y=2
z=x+y
print(z)


# In[15]:


#multiplication
z=x*y
print(z)


# In[16]:


#divison
z=x/y
print(z)


# In[22]:


#recuperer la partien entière de la divison 
z=x//y
print(z)


# In[23]:


#le rest de la division euclidienne(modulo)
z=x%y
print(z)


# In[24]:


#puissance
z=x**y
z


# ## Opérations Logiques Simples:
# 
# Opérateurs Logiques: and, or, not pour les opérations booléennes.
# Comparaisons: ==, !=, >, <, >=, <= pour comparer des valeurs.
# Opérations logiques

# In[25]:


x=True
y=False
#par exple x=l'age de l'individu est inférieur à 18ans et y= son revenu
# sup à 5000
z=x and y
print(z)


# In[26]:


z=x or y
z


# In[27]:


not x


# In[28]:


age=24
age 


# In[35]:


# le signe = c'est l'affectation et == c'est comparaison
x=5
z=x
z


# # Opérations de comparaison

# In[29]:


# tester si l'age=24
age==24


# In[30]:


age<24


# In[31]:


age>24


# In[32]:


# tester si l'age est inf ou égale à 24ans
age<=24


# In[33]:


# tester si l'age est sup ou égale à 24ans
age>=24


# In[34]:


# tester si l'age est diff de 24ans
age!=24


# # Les Fonctions en Python
# 
# ### Fonctions lambda
# ### Fonctions avancées: Définiton et les valeurs par défaut

# une fonction est une suite d'inscription qui m'évite à rédiger une code plusieurs fois, par exple, si je veux 
# calculer la moyenne des notes dans une classe, au lieu d ecrire à chaque fois la formule mathematique pour calculer 
# la moyenne, je peux écrire une fonction qui calcule la moyenne et ré use dans plusieurs 

# # fonction lamda: est une fonction qu'on peut rédiger en une seule code,

# In[38]:


addition=lambda x,y:x+y


# In[39]:


addition=(x=5,y=15)


# In[40]:


temp=addition(x=5,y=15)
temp


# In[48]:


#si on veut changer l'opération de la fonction, juste on change et c'est tt

multiplication=lambda x,y,z:x-y-z


# In[49]:


temp=multiplication(x=5,y=9,z=8)
temp


# #création fonction classique

# In[51]:


# je definis ma fonction (def)
def addition(a,b,c):
    resultat=a+b+c
    return resultat


# In[52]:


addition(a=2,b=3,c=4)


# In[53]:


test=addition(a=2,b=3,c=4)
test


# In[56]:


def multiplication(a,b,c):
    resultat=a*b
    resultat=resultat*c
    return resultat


# In[57]:


multiplication(a=4,b=8,c=9)


# # Exercice 1 : Fonction Lambda
# 
# ## Objectif : Écrire une fonction lambda qui multiplie deux nombres.
# 
# ### Instructions :
# 
# 1-Créez une fonction lambda qui accepte deux arguments et retourne leur produit.
# 2-Testez cette fonction en lui passant différents couples de nombres et affichez les résultats.

# In[ ]:




