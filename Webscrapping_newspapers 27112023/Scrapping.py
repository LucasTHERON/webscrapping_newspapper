# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 09:21:24 2023

@author: cleme
"""

import Madedatabase
import requests
from bs4 import BeautifulSoup

# Ouvrir le fichier en mode lecture
with open('Newspapers_FR.txt', 'r') as text:
    lines = text.readlines()

# Initialiser une liste pour stocker les listes de chaque ligne
newspappers_list = []

# Parcourir chaque ligne et créer une liste de 4 éléments en utilisant la virgule comme séparateur
for line in lines:
    el = line.strip().split(', ')
    newspappers_list.append(el)

# Vérifier si la requête a réussi
def scrappNewspapper(name, url, title_name, main_container, content_container):
    # Envoyer une requête GET à l'URL
    response = requests.get(url)
    if response.status_code == 200:
        print(name)
        print("------------------")
        print("------------------")
        print("------------------")
        # Analyser le contenu HTML de la page
        soup = BeautifulSoup(response.content, "html.parser")
        
        #On boucle sur les conteneurs des titres / liens qui sont logiquement ensemble
        for container in soup.find_all( class_=main_container ):
            #Print du titre grâce à la classe html title_name
            for title in container.find_all( class_=title_name ):
                print(title.text)
            print ("------------")
            #Récupération du lien à scrapper pour le contenu de l'article
            for link in container.find_all('a', href=True):
                article = requests.get(link['href'])
                if article.status_code == 200:
                    soup = BeautifulSoup(article.content, "html.parser")
                    content = ""
                    #On utilise une classe html pour cibler uniquement les contenus des articles
                    #On boucle au cas ou cette classe se répète à chaque paragraphe et on entre tout le contenu dans une balise
                    for container in soup.find_all(class_=content_container):
                       content += container.text
                    
                    print(content)
            print("\n-\n\n-\n\n-\n\n-\n")
        
# Données test
name = "LE MONDE"
url = "https://www.lemonde.fr/"
title_name = "article__title"
main_container = "article"
content_container = "article__paragraph"

scrappNewspapper(name, url, title_name, main_container, content_container)




# import Madedatabase
# import requests
# from bs4 import BeautifulSoup

# # URL du site à scraper
# url = "https://www.leparisien.fr/"

# # Envoyer une requête GET à l'URL
# response = requests.get(url)

# # Vérifier si la requête a réussi
# if response.status_code == 200:
#     # Analyser le contenu HTML de la page
#     soup = BeautifulSoup(response.content, "html.parser")

#     # Trouver les balises <a> contenant les titres des articles
#     main_title_links = soup.find_all(  class_="lp-card-article__media")
#     sub_title_links  = soup.find_all(  class_="article__title")
#     # Parcourir les liens d'articles et extraire les titres
#     for link in main_title_links:
#         # Extraire le texte du lien (titre de l'article)
#         title = link.text.strip()
#         print(title)
#         print( )
        
     
#     for link in sub_title_links:
#         # Extraire le texte du lien (titre de l'article)
#         title = link.text.strip()
#         # Afficher le titre de l'article
#         print(title)
#         print( )
#         Madedatabase.enregistrer_csv("donnees.csv", title, '0')

# else:
#     print("La requête a échoué avec le code de statut:", response.status_code)