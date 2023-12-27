# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 10:47:31 2023

@author: cleme
"""

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Charger les données d'entraînement (exemple avec un jeu de données fictif)
data = pd.read_csv("donnees.csv")  # Remplacez "donnees.csv" par le chemin vers votre jeu de données

# Diviser les données en phrases (X) et les thèmes correspondants (y)
X = data["phrase"]
y = data["theme"]

# Créer une représentation vectorielle des phrases en utilisant TF-IDF
vectorizer = TfidfVectorizer()
X_vectorized = vectorizer.fit_transform(X)

# Diviser les données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X_vectorized, y, test_size=0.2, random_state=42)

# Entraîner un modèle de classification RandomForest
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Noter une nouvelle phrase et prédire son thème
nouvelle_phrase = "Votre phrase à noter et à classer"
nouvelle_phrase_vectorized = vectorizer.transform([nouvelle_phrase])
note = model.predict(nouvelle_phrase_vectorized)[0]

# Afficher la note et le thème prédit
print("Note :", note)
print("Thème prédit :", note)