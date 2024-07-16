#!/usr/bin/env python3
"""
Script Python pour se connecter à une base de données MongoDB
et récupérer des statistiques de logs Nginx.

Ce script se connecte à MongoDB et compte les documents dans la
collection 'nginx' du db 'logs'. Il affiche ensuite
le nombre total de logs, ainsi que le décompte des requêtes pour
chaque méthode HTTP (GET, POST, PUT, PATCH, DELETE) et
le nombre de requêtes de vérification de statut (GET /status).

Assurez-vous d'avoir pymongo installé:
    $ pip3 install pymongo
"""

from pymongo import MongoClient


def log_stats():
    """
    Fonction pour récupérer et afficher
    les statistiques des logs Nginx depuis MongoDB.
    """
    # Connexion au client MongoDB
    client = MongoClient('mongodb://127.0.0.1:27017')
    # Sélection de la collection 'nginx' dans la base de données 'logs'
    nginx_collection = client.logs.nginx

    # Nombre total de logs
    count = nginx_collection.count_documents({})
    print(f"{count} logs")

    # Affichage du décompte par méthode HTTP
    print("Méthodes:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        method_count = nginx_collection.count_documents({"method": method})
        print(f"\tMéthode {method}: {method_count}")

    # Nombre de requêtes de vérification de statut (GET /status)
    status_check_count = nginx_collection.count_documents({"method": "GET",
                                                           "path": "/status"})
    print(f"{status_check_count} vérifications de statut")


if __name__ == "__main__":
    log_stats()
