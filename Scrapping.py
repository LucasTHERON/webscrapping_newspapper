# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 09:21:24 2023

@author: cleme
"""

import Madedatabase
import requests
import json
from bs4 import BeautifulSoup

# Vérifier si la requête a réussi
def scrappNewspapper(name, url, title_name, main_container, content_container):
    # Envoyer une requête GET à l'URL
    response = requests.get(url)
    if response.status_code == 200:
        output = ""
        output += name
        output += ("------------------")
        output += ("------------------")
        output += ("------------------")
        # Analyser le contenu HTML de la page
        soup = BeautifulSoup(response.content, "html.parser")
        
        #On boucle sur les conteneurs des titres / liens qui sont logiquement ensemble
        for container in soup.find_all( class_=main_container ):
            #Print du titre grâce à la classe html title_name
            for title in container.find_all( class_=title_name ):
                output += title.text
                output += "\n------------\n"
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
                    output +=(content)
            output += "\n\n\n\n\n"
        print(str(output))
        txt = str(output).encode('utf-8')
        with open("output.txt", "wb") as f:
            f.write(txt)
        f.close

with open('newspapers.json') as json_file:
    data = json.load(json_file)
    
for line in data:
    scrappNewspapper(line['name'], line['url'], line['title_name'], line['main_container'], line['content_container']) 