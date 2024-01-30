#!/usr/bin/env python
# coding: utf-8

# # stucture de controle
# 

# ## If: Comment prendre des décisions dans vos programmes
# pour monter en compétence dans une langage de programmation et on travail en Data, posons la question, comment les données sont disposées dans ce langage, qd on comprend cela, on arrive à accéder et les modifier.
# if: nous permet de mettre des conditions si nous programmons 

# In[1]:


#decision simple
temperature = 35
if temperature > 30:
    print("il fait chaud")


# In[2]:


temperature > 30


# In[6]:


#decision avec alternance(Else)
temperature = 20
if temperature > 30:
    print("il fait chaud")
else:
    print("il fait froid")


# In[9]:


#decision avec multiples alternatives (Elif), je prends la moyenne par exemple, une seule condtion ici. elif pr +iers
note = "F"
if note == "A" :
    print("Excellent")
elif note == "B" :
    print("Très bien")
elif note == "C" :
    print("Bien")
elif note == "D" :
    print("Assez-bien")
else:
    print("A améliorer")


# In[19]:


#conditions multiples conditions, ex: je ve accorder une bourse aux etud -20 et note>16
note = 17
age= 18

#dans if on met juste un Boulien et ça passe avec (et,&, or, /)

if (note > 16) and (age <=20):
    print("Bourse accordée")
else:
    print("Pas de Bourse")


# In[20]:


# la condition ci-dessous est un boulien sans la condition if

(note >16) and (age<=20)


# In[22]:


#conditions imbriquées
if age <= 20 :
    if note > 16 :
        print("Bourse acceptée")
    else:
        print("Pas de bourse")
    


# ### Exercice
# 
# ###### Objectif :  Développer une fonction classer_age en Python qui détermine la catégorie d'âge d'une personne à partir de son âge.
# 
# ##### Instructions :
# 
# 1. La fonction classer_age doit accepter un seul argument numérique, age, qui représente l'âge de la personne en années.
# 2. La fonction doit retourner une chaîne de caractères selon l'âge :
#    . Retourner "Enfant" si l'âge est inférieur à 12 ans.
#    . Retourner "Adolescent" si l'âge est entre 12 et 17 ans inclus.
#    . Retourner "Adulte" si l'âge est entre 18 et 59 ans inclus.
#    . Retourner "Senior" si l'âge est de 60 ans ou plus.
# 3. Si l'âge est inférieur à 0 ou n'est pas un nombre valide, la fonction doit retourner "Âge invalide"

# In[31]:


## 1- premiere manière
classer_age = 69
if (classer_age == 1) & (classer_age < 12) :
    print ("Enfant")
elif (classer_age >= 12) & (classer_age < 17) :
    print ("Adolescent")
elif (classer_age >=18 ) & (classer_age < 59) :
    print ("Adulte")
elif (classer_age >= 60 ) :
    print ("senior")
else:
    print("age invalide")


# In[32]:


def classer_age(x):
    
    if (x <= 12) & (x >=0) :
        resultat = "Enfant"
    elif (x > 12) & (x <= 17):
        resultat =  " Adolescent"
    elif (x >= 18) & (x <= 59):
        resultat =  " Adulte"
    elif (x >= 60) :
        resultat =  " Senior"
    else:
        resultat = "Age invalide"
        
    return resultat
classer_age(50)


# ## For: Techniques pour parcourir des données séquentielles
# ### la fonction boucle ça permet de parcourir des séquenciellles

# In[ ]:


# Répresentation de la boucle for simple

for i range(10,100,-3) :
    print(i)


# In[46]:


#For avec une condition if
for i in range(10,0,-1) :
    
    if i % 2 == 0 :
        print(i, " est un Nombre pair")
    else :
        print(i, " est Nombre impair")


# # While: Exécuter des instructions de manière répétitive sous certaines conditions

# In[56]:


#while de base: tant que la condition n'est pas validé, créer un compteur qui compte de 1 à 10
compteur = 1
while compteur < 10 :
    print(compteur)
    compteur += 1   # compteur= compteur + 1
    


# In[2]:


# Boucle infinie avec while et l'instructeur break
compteur = 1
while True :
    print(compteur)
    compteur += 1 
    if compteur == 5 :
        break


# # Types de Données en Python
# les différents types de données qui existent en python, comprendre l'accronyme: CRUD (create, read, update et delete), comprendre cette accronyme dans n'importe quel langage.
# ## Listes
# 
# ## Create:
# comprendre comment on arrive à créer les objets, comprendre les mécanismes qui te permettent de créer l'objets, on crée les listes avec les crochets.

# In[5]:


#List de Listes

liste_age = [15, 17, 23, 29, 45,50,60, 98]  #j'ai créé un objet qui contient +ieurs élément
print(liste_age)
type(liste_age)


# In[12]:


#taille des élements d'une liste
len(liste_age)


# In[8]:


#liste de chaines de caractère
liste_nom = ["Youssouf", "Nassrine", "Vera"]
liste_nom


# In[10]:


#Liste des listes
liste = [liste_age, liste_nom]
print(liste)
type(liste)


# ## Read:
# comprendre comment on arrive à lire les informations dans l'objet, lire les 1ers élements de la liste

# In[19]:


# Lire un élément au début
# Liste de nombre
liste_age = [15, 17, 23, 29, 45,50,60, 98] #le 1er élt en python c'est 0 et dernier -1
liste_age[0]


# In[11]:


# Lire le dernier élément: il y'a 2 élt, -1 et 2nd c'est de récupérer la taille et -1
liste_age[-1]


# In[14]:


liste_age[len(liste_age)-1]


# In[16]:


#lire à une position quelconque
liste_age[4]


# In[21]:


liste[0][0]


# In[22]:


#lire sur plusieurs positions qui se suivent, exple: de 0 à 3
liste_age[0:3]


# In[23]:


#faire une boucle d'une liste

for nom in liste_nom :
    print(nom)


# ## Update:
# comment esk je peux mettre à jour les informations, genre si je veux modifier le nom de Nassrine par Mamadou

# In[24]:


#modification direct à partir d'un index
liste_nom[1]= "Oumar"
print(liste_nom)


# In[27]:


#ajouter un élt et qu'il soit à la fin de la liste (append)
liste_nom.append("Kylian")
liste_nom


# In[30]:


#ajouter cette fois-ci à une position précise avec la fontion (insert)
liste_nom.insert(1,"Floriane")
liste_nom


# ## Delete
# je veux maintenent supprimer un des élts de la liste précédente, 

# In[32]:


#supprimer l'élt à un index spécifique (de la list [index])
del liste_nom[4]
liste_nom


# In[34]:


#supprimer la première occurence de l'élement(remove)
liste_age = [15, 17, 23, 29, 45,50,60, 98]
liste_age.remove(45) #je supprime 45 de ma liste
liste_age


# In[36]:


#supprimer et retourner l'élt à l'index donné pop
liste_age.pop(0)


# In[37]:


liste_age


# ## String 
# 

# In[38]:


nom = "Ibrahim"
nom[4]


# # Tuples
# . un tuple est une collection d'élément ordonnée et immuable en python
# . Avantage: moins d'espace mémoire que les listes
# 

# In[ ]:


#create
mon_tuple = (3, 6, 7, 8)
mon tiple


# In[ ]:




