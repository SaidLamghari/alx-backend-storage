#!/usr/bin/env python3
"""
Script Python pour récupérer et afficher des
statistiques sur les logs Nginx stockés dans MongoDB.

Ce script se connecte à une base de données MongoDB locale,
compte les documents dans la collection 'nginx'
du db 'logs', puis affiche le nombre total de logs
ainsi que le décompte des requêtes pour chaque méthode HTTP
(GET, POST, PUT, PATCH, DELETE) et le nombre de
requêtes de vérification de statut (GET /status).

Assurez-vous d'avoir pymongo installé :
    $ pip3 install pymongo
"""

from pymongo import MongoClient
from pymongo.errors import ConnectionFailure


if __name__ == "__main__":
    try:
        # Connexion à MongoDB
        client = MongoClient('mongodb://127.0.0.1:27017')
        nginx_logs = client.logs.nginx

        # Définition des méthodes à compter
        methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

        # Récupération du nombre total de logs
        docs_num = nginx_logs.count_documents({})
        print(f"{docs_num} logs")

        # Récupération du nombre de logs pour chaque méthode
        print("Méthodes:")
        for method in methods:
            method_count = nginx_logs.count_documents({'method': method})
            print(f"\tMéthode {method}: {method_count}")

        # Récupération du nombre de vérifications de statut (GET /status)
        get_status = nginx_logs.count_documents({'method': 'GET',
                                                 'path': '/status'})
        print(f"{get_status} vérifications de statut")

    except ConnectionFailure as e:
        print(f"Erreur de connexion à MongoDB : {e}")

    except Exception as e:
        print(f"Une erreur s'est produite : {e}")

    finally:
        if client:
            client.close()  # Fermeture de la connexion MongoDB
