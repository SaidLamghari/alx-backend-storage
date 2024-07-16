#!/usr/bin/env python3

'''
Module.
'''

from pymongo import MongoClient


def print_request(nginx_collection):
    '''Affiche les statistiques des logs de
    requêtes Nginx en utilisant l'agrégation MongoDB.
    
    Args:
        nginx_collection (pymongo.collection.Collection):
        Collection MongoDB contenant les logs Nginx.
    '''
    
    # Pipeline pour obtenir le nombre total de logs
    pipeline_ttl_logs = [
        {"$group": {"_id": None, "total_logs": {"$sum": 1}}},
        {"$project": {"_id": 0, "total_logs": 1}}
    ]
    
    # Exécuter le pipeline pour obtenir le nombre total de logs
    total_logs = list(nginx_collection.aggregate(pipeline_ttl_logs))
    
    # Afficher le nombre total de logs s'il existe
    if total_logs:
        print('{} logs'.format(total_logs[0]['total_logs']))
    
    # Afficher les statistiques pour chaque méthode HTTP
    print('Méthodes:')
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    for method in methods:
        pipeline_mthod = [
            {"$match": {"method": method}},
            {"$group": {"_id": None, "count": {"$sum": 1}}},
            {"$project": {"_id": 0, "method": method, "count": "$count"}}
        ]
        method_count = list(nginx_collection.aggregate(pipeline_mthod))
        
        if method_count:
            print('\tméthode {}: {}'.format(method, method_count[0]['count']))
    
    # Pipeline pour obtenir le nombre de vérifications de statut (GET /status)
    pipe_stas_chcks = [
        {"$match": {"method": "GET", "path": "/status"}},
        {"$group": {"_id": None, "status_check_count": {"$sum": 1}}},
        {"$project": {"_id": 0, "status_check_count": "$status_check_count"}}
    ]
    
    # Exécuter le pipeline pour obtenir le nombre de vérifications de statut
    stas_chcks = list(nginx_collection.aggregate(pipe_stas_chcks))
    
    # Afficher le nombre de vérifications de statut s'il existe
    if stas_chcks:
        print('{} vérifications de statut'.format(stas_chcks[0]['status_check_count']))


if __name__ == '__main__':
    # Connexion au client MongoDB
    client = MongoClient('mongodb://127.0.0.1:27017')
    
    # Appel de la fonction pour afficher les statistiques des logs Nginx
    print_request(client.logs.nginx)
