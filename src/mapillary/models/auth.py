# Copyright (c) Facebook, Inc. and its affiliates. (http://www.facebook.com)
# -*- coding: utf-8 -*-

"""
mapillary.models.auth
~~~~~~~~~~~~~~~~~~~~~

This module contains the authorization logic for the client class of Mapillary, responsible
for keeping track of the session token set

For more information, please check out https://www.mapillary.com/developer/api-documentation/.

- Copyright: (c) 2021 Facebook
- License: MIT LICENSE
"""

from functools import wraps

# Local imports
from mapillary.models.client import Client
from mapillary.models.exceptions import AuthError


def auth():
    """Wrap interface functions with logic for Client"""

    def auth_decorator(f):
        """Decorator function"""

        @wraps(f)
        def wrapper(*args, **kwargs):
            """
            :param args: Function arguments
            :param kwargs: Key word arguments
            :return: Return the specified function with args, kwargs
            """

            if Client.get_token() == "":
                # If empty, raise exception
                raise AuthError("Function called without setting the access token")

            # Return function called with arguments
            return f(*args, **kwargs)

        # Return wrapper
        return wrapper

    # Return decorator
    return auth_decorator
