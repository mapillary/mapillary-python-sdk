# -*- coding: utf-8 -*-

"""
mapillary.models.credentials

This module contains the Credentials class of
Mapillary, responsible for keeping track of the
session token set
"""

import requests
import json

# Exception Imports
from .exceptions import InvalidTokenError


class Credentials:

    token = ""

    @classmethod
    def set_token(cls, new_token):
        cls.__check_token_validity(new_token)
        cls.token = new_token

    @classmethod
    def __check_token_validity(cls, new_token):
        response = requests.get(
            "https://graph.mapillary.com/1933525276802129?fields=id",
            headers={"Authorization": f"OAuth {new_token}"},
        )

        response = json.loads(response.content)

        if "error" in response:
            raise InvalidTokenError(
                response["error"]["message"],
                response["error"]["type"],
                response["error"]["code"],
                response["error"]["fbtrace_id"],
            )
