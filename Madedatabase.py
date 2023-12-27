# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 11:30:21 2023

@author: cleme
"""
# Madedatabase 
# Goal: Add informations to the donnée csv

import csv

def enregistrer_csv(chemin_fichier, phrases, themes):
    # Vérifier que le nombre de phrases est égal au nombre de thèmes
    if len(phrases) != len(themes):
        raise ValueError("Le nombre de phrases doit être égal au nombre de thèmes.")

    # Créer une liste de tuples (phrase, thème)
    donnees = list(zip(phrases, themes))

    # Écrire les données dans le fichier CSV
    with open(chemin_fichier, "w", newline="") as fichier_csv:
        writer = csv.writer(fichier_csv)
        writer.writerow(["phrase", "thème"])  # Écrire l'en-tête des colonnes
        writer.writerows(donnees)  # Écrire les données

    print("Les données ont été enregistrées au format CSV avec succès.")

# Exemple d'utilisation
phrases = ["Je suis heureux", "Il pleut aujourd'hui", "Le film était super"]
themes = ["positif", "négatif", "positif"]

enregistrer_csv("donnees.csv", phrases, themes)



