"""
mapillary.utils.client

This module contains aims to serve as a generalization for all API
requests within the mapillary python SDK
"""

import requests
import logging
import sys
import os
import pprint
from math import floor


# Root endpoint for vector tiles
TILES_URL = "https://tiles.mapillary.com"

# Root endpoint for metadata
GRAPH_URL = "https://graph.mapillary.com"

# Basic logger setup
logger = logging.getLogger("mapillary.utils.client")

# stdout logger setup
hdlr = logging.StreamHandler(sys.stdout)
logger.addHandler(hdlr)

# Setting log_level to INFO
logger.setLevel(logging.INFO)


class Client(object):
    """
    Client setup for API communication
    """

    def __init__(self, access_token=None) -> None:

        self.url = GRAPH_URL  # Default to metadata endpoint

        # Session object setup to be referenced across future API calls.
        self.session = requests.Session()

        # User Access token will be set once and used throughout all requests within the same session
        self.access_token = access_token

    def __initiate_request(
        self, endpoint=None, method="GET", graph=True, params=None, body=None
    ):
        # TODO: document the method
        if endpoint is None:  # Check if an enpoint is specified.
            logger.error("You need to specify an endpoint!")
            return

        # Dynamically set authorization mechanism based on the target endpoint
        if not graph:
            params["access_token"] = params.get("access_token", self.access_token)
        else:
            self.session.headers.update({"Authorization": f"OAuth {self.access_token}"})

        url = self.url + endpoint
        request = requests.Request(method, url, params=params)
        prepped_req = self.session.prepare_request(
            request
        )  # create a prepared request with the request and the session info merged

        # TODO: Log the request

        # Sending the request
        res = self.session.send(prepped_req)

        # TODO: Log the response
        pprint.pprint(res.content)

        # Handling the response status codes
        if res.status_code == requests.codes.ok:
            try:
                logger.debug(f"Response: {res.json()}")
            except ValueError:
                return res.text

        elif res.status_code >= 400:
            logger.error(f"Srever responded with a {str(res.status_code)} error!")
            try:
                logger.debug(f"Error details: {str(res.json())}")

            except ValueError:
                ...
            res.raise_for_status()

    def get(self, endpoint=None):
        return self.__initiate_request(endpoint=endpoint)



