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

import json

def get_imgae_thumbnail(image_id, resolution):
    url = Entities.get_image(image_id, [resolution])
    res = json.loads(Client().get(url).content.decode('utf-8'))
    # print(res)
    return res[resolution]

