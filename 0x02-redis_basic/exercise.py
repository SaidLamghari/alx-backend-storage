#!/usr/bin/env python3
"""
Module pour la classe Cache interagissant avec Redis
"""
import redis
import uuid
from typing import Union


class Cache:
    def __init__(self):
        """
        Initialise Cache avec une instance de client
        Redis et vide la base de données Redis.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stocke les données d'entrée dans Redis sous une
        clé générée aléatoirement et retourne la clé.

        Args:
            data (Union[str, bytes, int, float]): Données à stocker dans Redis.

        Returns:
            str: Clé générée aléatoirement
            utilisée pour stocker les données dans Redis.
        """
        ky = str(uuid.uuid4())
        self._redis.set(ky, data)
        return ky
