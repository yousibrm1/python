#!/usr/bin/env python
# coding: utf-8

# # Les Tuples
# les tuples se sont des éléments qu'on crée et ordonée mais sont inchanchables. le contraire de la liste.
# 

# In[1]:


#create tuples
mon_tuple = (3, 6, 7, 8)
mon_tuple


# In[2]:


#read
mon_tuple[0]


# In[3]:


mon_tuple[0]
mon_tuple[-1]


# In[5]:


mon_tuple[1]


# In[6]:


#update
mon_tuple[-1] = 0 # d'ou tuple est inchangeabe, on ne peut pas faire la mise à jour


# In[7]:


#delete: on peut pas supprimer un seul élément mais plutot l'ensemble
del mon_tuple


# # Sets
# ### Un set est une collection d'éléments non ordonnée, modifiable et unique en Python. Chaque élément dans un set est distinct et ne peut apparaître qu'une seule fois.

# ### Avantage : les sets sont optimisés pour vérifier rapidement si un élément est présent dans la collection, ce qui les rend idéaux pour les opérations comme les unions, intersections, et différences d'ensembles

# In[8]:


#create, les élts ne st pas ordonnées mais en liste oui
mon_set = {4, 5, 7, 7, 7, 6, 6}
print(mon_set)


# In[9]:


#read (for)
for element in mon_set:
    print(element)


# In[11]:


#read if pour vérifier la présence

if 3 in mon_set:
    print("3 est disponible")
else :
    print("3 non disponible")


# ## la différence entre une liste,set et tuple
# 1- les tuples, on ne peut pas les modifier, ils sont utlisés pour permuter les élts.
# 2- set on peut modifier mais les éléments non ordonnées et unique
# on peut transformer set en list et le vise-versa, 
# 

# In[12]:


type (mon_set)


# In[13]:


type (list(mon_set))


# In[ ]:




