#!/usr/bin/env python3
"""
Ce module contient la classe Cache qui interagit avec Redis
pour stocker et récupérer des données.
Auteur SAID LAMGHARI
"""

import redis
import uuid
from typing import Union, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    Décorateur qui compte combien de fois une méthode est appelée.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        # Utilise le nom qualifié de la méthode comme clé
        key = f"{method.__qualname__}"
        # Incrémente le compteur chaque fois
        # que la méthode est appelée
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Décorateur pour stocker l'historique des entrées et sorties d'une
    fonction particulière.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        # Clés pour stocker les entrées et sorties
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"
        # Ajoute les arguments d'entrée à la liste
        self._redis.rpush(input_key, str(args))
        result = method(self, *args, **kwargs)
        # Ajoute le résultat de la fonction
        # à la liste des sorties
        self._redis.rpush(output_key, result)
        return result
    return wrapper


class Cache:
    """
    Classe Cache pour interagir avec Redis pour stocker et récupérer
    des données.
    """

    def __init__(self):
        """
        Initialise le client Redis et vide la base de données.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stocke les données d'entrée dans Redis en utilisant une clé
        générée aléatoirement.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) -> Union[str, bytes,
                                                          int, float, None]:
        """
        Récupère les données de Redis et applique éventuellement une
        fonction de conversion.
        """
        data = self._redis.get(key)
        if data is None:
            return None
        return fn(data) if fn else data

    def get_str(self, key: str) -> str:
        """
        Récupère les données sous forme de chaîne de caractères.
        """
        return self.get(key, lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """
        Récupère les données sous forme d'entier.
        """
        return self.get(key, int)


def replay(method: Callable):
    """
    Affiche l'historique des appels d'une fonction particulière.
    """
    self = method.__self__
    input_key = f"{method.__qualname__}:inputs"
    output_key = f"{method.__qualname__}:outputs"
    inputs = self._redis.lrange(input_key, 0, -1)
    outputs = self._redis.lrange(output_key, 0, -1)

    print(f"{method.__qualname__} a été appelé {len(inputs)} fois:")
    for inp, out in zip(inputs, outputs):
        print(f"{method.__qualname__}(*{inp.decode('utf-8')}) -> "
              f"{out.decode('utf-8')}")
