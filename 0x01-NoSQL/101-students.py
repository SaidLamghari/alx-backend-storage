#!/usr/bin/env python3
"""101-students.py"""
from pymongo import MongoClient


def top_students(mongo_collection):
    '''
    Retourne la liste des étudiants triés par score moyen,
    calculé à partir des scores dans 'topics'.

    Args:
        mongo_collection (pymongo.collection.Collection):
        Collection MongoDB contenant les documents des étudiants.

    Returns:
        list: Liste des étudiants triés par 'averageScore'
        en ordre décroissant.
              Chaque étudiant est représenté par un dictionnaire
              contenant 'name' et 'averageScore'.
    '''
    # Définition du pipeline d'agrégation MongoDB
    pipeline = [
        {
            "$project": {
                # Inclut le champ 'name' dans les résultats projetés
                "name": 1,
                # Calcule la moyenne des scores dans le tableau 'topics'
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {
            # Trie par 'averageScore' en ordre descendant
            "$sort": {"averageScore": -1}
        }
    ]

    # Exécute le pipeline d'agrégation MongoDB
    # et convertit le curseur en liste de résultats
    return list(mongo_collection.aggregate(pipeline))
