# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 09:21:24 2023

@author: cleme
"""

import Madedatabase
import requests
from bs4 import BeautifulSoup

# URL du site à scraper
url = "https://www.leparisien.fr/"

# Envoyer une requête GET à l'URL
response = requests.get(url)

# Vérifier si la requête a réussi
if response.status_code == 200:
    # Analyser le contenu HTML de la page
    soup = BeautifulSoup(response.content, "html.parser")

    # Trouver les balises <a> contenant les titres des articles
    main_title_links = soup.find_all(  class_="lp-card-article__media")
    sub_title_links  = soup.find_all(  class_="article__title")
    # Parcourir les liens d'articles et extraire les titres
    for link in main_title_links:
        # Extraire le texte du lien (titre de l'article)
        title = link.text.strip()
        print(title)
        print( )
        
     
    for link in sub_title_links:
        # Extraire le texte du lien (titre de l'article)
        title = link.text.strip()
        # Afficher le titre de l'article
        print(title)
        print( )
        Madedatabase.enregistrer_csv("donnees.csv", title, '0')

else:
    print("La requête a échoué avec le code de statut:", response.status_code)