#!/usr/bin/env python3
"""
Ce module contient une fonction pour récupérer
le contenu HTML d'une URL
et le mettre en cache dans Redis avec une durée d'expiration.
auteur SAID LAMGHARI
"""

import redis
import requests
from typing import Callable


def get_page(url: str) -> str:
    """
    Récupère le contenu HTML d'une URL et le met en cache avec une
    durée d'expiration de 10 secondes.
    """
    r = redis.Redis()
    cache_ky = f"count:{url}"
    html_ky = f"html:{url}"
    # Incrémente le compteur d'accès à l'URL
    r.incr(cache_ky)
    
    # Vérifie si le contenu est déjà en cache
    cached_html = r.get(html_ky)
    if cached_html:
        return cached_html.decode('utf-8')
    
    # Si non en cache, récupère le contenu de l'URL
    rspnse = requests.get(url)
    html_cntnt = rspnse.text
    
    # Stocke le contenu dans Redis avec une expiration de 10 secondes
    r.setex(html_ky, 10, html_cntnt)
    return html_cntnt


def cache_decorator(method: Callable) -> Callable:
    """
    Décorateur pour mettre en cache le résultat d'une fonction dans Redis
    avec une durée d'expiration.
    """
    def wrapper(url: str, *args, **kwargs):
        r = redis.Redis()
        cache_ky = f"count:{url}"
        html_ky = f"html:{url}"
        
        # Incrémente le compteur d'accès à l'URL
        r.incr(cache_ky)
        
        # Vérifie si le contenu est déjà en cache
        cached_html = r.get(html_ky)
        if cached_html:
            return cached_html.decode('utf-8')
        
        # Si non en cache, appelle la fonction originale
        html_cntnt = method(url, *args, **kwargs)
        
        # Stocke le contenu dans Redis avec une expiration de 10 secondes
        r.setex(html_ky, 10, html_cntnt)
        return html_cntnt
    return wrapper


@cache_decorator
def get_page_decorated(url: str) -> str:
    """
    Récupère le contenu HTML d'une URL. Cette fonction est décorée pour
    mettre en cache le résultat.
    """
    rspnse = requests.get(url)
    return rspnse.text
