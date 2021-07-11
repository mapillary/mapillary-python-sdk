"""
mapillary.controller.image
~~~~~~~~~~~~~~~~~~~~~~~~~~
This module implements the business logic
functionalities of the Mapillary Python SDK. For
more information, please check out
https://www.mapillary.com/developer/api-documentation/
:copyright: (c) 2021 ...
:license: See LICENSE for more details
"""

# Local imports
from config.api.entities import Entities

# Client
from models.client import Client

# Exceptions imports
from models.exceptions import InvalidImageResolution, InvalidImageKey

# Library imports
import json
from requests import HTTPError


def get_imgae_thumbnail(image_id, resolution):

    # check if the entered resolution is one of the supported image sizes
    if resolution not in [256, 1024, 2048]:
        raise InvalidImageResolution(resolution)

    try:
        res = Client().get(Entities.get_image(image_id, [f"thumb_{resolution}_url"]))
    except HTTPError:
        # If given ID is an invalid image ID, let the user know
        raise InvalidImageKey(image_id)

    thumbnail = json.loads(res.content.decode("utf-8"))[f"thumb_{resolution}_url"]

    return thumbnail
