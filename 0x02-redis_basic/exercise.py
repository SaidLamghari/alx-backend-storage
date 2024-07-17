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

    def get(self, key: str, fn: Callable = None) -> Union[str, bytes,
                                                          int, float, None]:
        """
        Récupère les données depuis Redis pour la clé donnée et
        optionnellement applique une fonction de conversion.

        Args:
            key (str): Clé à récupérer depuis Redis.
            fn (Callable, optionnel): Fonction callable pour
            convertir les données récupérées.

        Returns:
            Union[str, bytes, int, float, None]: Données
            récupérées, éventuellement converties par fn.
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """
        Récupère les données depuis Redis pour la clé donnée et
        décode les bytes en chaîne de caractères UTF-8.

        Args:
            key (str): Clé à récupérer depuis Redis.

        Returns:
            Union[str, None]: Chaîne de caractères décodée en UTF-8
            récupérée depuis Redis, ou None si la clé n'existe pas.
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """
        Récupère les données depuis Redis pour
        la clé donnée et convertit en entier.

        Args:
            key (str): Clé à récupérer depuis Redis.

        Returns:
            Union[int, None]: Valeur entière récupérée depuis
            Redis, ou None si la clé n'existe pas.
        """
        return self.get(key, fn=int)
