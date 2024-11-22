import streamlit as st
import requests
import time

# Titre de l'application
st.title("My Content - Recommandations d'articles")

# Section pour ajouter un nouvel utilisateur
st.header("Ajouter un nouvel utilisateur")

# Saisie de l'ID utilisateur
new_user_id = st.number_input("Entrez un nouvel ID utilisateur", min_value=1, step=1)

if st.button("Ajouter l'utilisateur"):
    # URL de l'Azure Function pour l'ajout d'un utilisateur
    url = "https://mycontentapp.azurewebsites.net/api/add_user?code=xCTRUhr8713XhEZixMOzeW4vF6idGl2mas7Co-YNKakaAzFu7kjtTQ=="
    
    # Créer le payload pour la requête
    payload = {"user_id": new_user_id}
    
    try:
        # Effectuer une requête POST à l'Azure Function
        response = requests.post(url, json=payload)
        
        if response.status_code == 201:
            st.write(f"Utilisateur {new_user_id} ajouté avec succès.")
        elif response.status_code == 400:
            st.write("L'utilisateur existe déjà.")
        else:
            st.write("Erreur lors de l'ajout de l'utilisateur.")
    
    except Exception as e:
        st.write(f"Une erreur est survenue lors de l'ajout de l'utilisateur : {e}")

# Section pour obtenir des recommandations
st.header("Obtenir des recommandations")

# Saisie de l'ID utilisateur pour les recommandations
user_id = st.number_input("Entrez votre ID utilisateur pour les recommandations", min_value=1, step=1)

# Bouton pour obtenir des recommandations
if st.button("Obtenir des recommandations"):
    # URL de l'Azure Function pour obtenir les recommandations
    url = f"https://mycontentapp.azurewebsites.net/api/recommend?user_id={user_id}&code=reApGZ8y_3u5LW5o3gFJSF6vFvgyH6JpYThQT7fiWj-gAzFuYjL2dg=="
    
    try:
        # Effectuer une requête GET à l'Azure Function
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            st.write(f"Recommandations d'articles pour l'utilisateur : {user_id}")
            for rec in data['recommendations']:
                st.write(f"Article ID: {rec['article_id']} - Titre : {rec['title']} - Score: {rec['score']}")
        elif response.status_code == 404:
            st.write("Utilisateur non trouvé. Ajoutez d'abord l'utilisateur.")
        else:
            st.write("Erreur lors de la récupération des recommandations.")
    
    except Exception as e:
        st.write(f"Une erreur est survenue : {e}")

# Section pour ajouter un nouvel article
st.header("Ajouter un nouvel article")

# Saisie des informations pour l'article
new_article_id = st.number_input("ID de l'article", min_value=1, step=1)
category_id = st.number_input("Catégorie ID", min_value=0, step=1)
publisher_id = st.number_input("ID de l'éditeur", min_value=0, step=1)
words_count = st.number_input("Nombre de mots", min_value=0, step=1)

# Génération automatique du timestamp
created_at_ts = int(time.time() * 1000)  # Timestamp en millisecondes

# Bouton pour ajouter l'article
if st.button("Ajouter l'article"):
    # URL de l'Azure Function pour l'ajout d'article
    url = "https://mycontentapp.azurewebsites.net/api/add_article?code=7bnzqUVxSblfxkv2jCf_2sfZCzcYzOtR-hsAaBk9AMfDAzFuxnXQzg=="
    
    # Créer un payload avec les informations de l'article
    payload = {
        "article_id": new_article_id,
        "category_id": category_id,
        "publisher_id": publisher_id,
        "words_count": words_count,
        "created_at_ts": created_at_ts
    }
    
    try:
        # Effectuer une requête POST à l'Azure Function
        response = requests.post(url, json=payload)
        
        if response.status_code == 201:
            st.write("L'article a été ajouté avec succès.")
        elif response.status_code == 400:
            st.write("L'article existe déjà.")
        else:
            st.write("Erreur lors de l'ajout de l'article.")
    
    except Exception as e:
        st.write(f"Une erreur est survenue lors de l'ajout de l'article : {e}")

    # Afficher le timestamp pour information
    st.write(f"Timestamp de création : {created_at_ts}")
