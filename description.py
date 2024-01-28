#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 12:50:49 2024

@author: yousibrm
"""

"""
   On crée une liste qui prend en entrer une liste et qui va resortir un dictionnnaire dans lequel on aura les élts nécessaire 
   pour faire stat descriptives

"""
def statdescriptive(nom_liste):
    """ cette fonction permet de faire des statistique descriptive sur une liste de parametre : 
        nom_liste: liste de nombre """
    
    minimum = min (nom_liste) 
    maxinum = max (nom_liste)
    somme = sum (nom_liste)
    moyenne = somme/len(nom_liste)
    resultat = {"min":minimum, "max":maxinum, "somme":somme, "moyenne":moyenne}
    
    return resultat
def somme_element(nom_liste):
    
    """ 
    cette fonction permet de calculer une somme
    """
    
    return sum(nom_liste)
