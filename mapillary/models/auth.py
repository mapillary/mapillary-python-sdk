# -*- coding: utf-8 -*-

"""
mapillary.models.auth

This module contains the authorization logic for
the client class of Mapillary, responsible
for keeping track of the session token set
"""

# Local imports
from models.client import Client
from models.exceptions import AuthError

from functools import wraps


def auth():
    def auth_decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            if Client.get_token() == "":
                raise AuthError("Function called without setting the access token")
            return f(*args, **kwargs)

        return wrapper

    return auth_decorator
