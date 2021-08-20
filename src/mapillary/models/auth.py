# Copyright (c) Facebook, Inc. and its affiliates. (http://www.facebook.com)
# -*- coding: utf-8 -*-

"""
mapillary.models.auth
~~~~~~~~~~~~~~~~~~~~~

This module contains the authorization logic for the client class of Mapillary, responsible
for keeping track of the session token set

For more information, please check out https://www.mapillary.com/developer/api-documentation/.

:copyright: (c) 2021 Facebook
:license: MIT LICENSE
"""

# Local imports
from mapillary.models.client import Client
from mapillary.models.exceptions import AuthError

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
