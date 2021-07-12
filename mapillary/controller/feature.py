"""
mapillary.controllers.feature
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the feature extraction business logic functionalities of the Mapillary
Python SDK.

For more information, please check out https://www.mapillary.com/developer/api-documentation/

:copyright: (c) 2021 Facebook
:license: MIT LICENSE
"""

# Local imports

# # Exception Handling
from controller.rules.verify import shape_bbox_check

def get_map_features_in_shape_controller(geojson: dict, kwargs: dict) -> dict:
    """For extracting all map features within a shape

    :param geojson: The initial data
    :type geojson: dict

    :param kwargs: Kwargs to filter with
    :type kwargs: dict

    :return: GeoJSON
    :rtpe: dict
    """

    # TODO: Requirement# 10

    shape_bbox_check(kwargs=kwargs)

    return {"Message": "Hello, World!"}


def get_feature_map_key_controller(key: str, fields: list) -> dict:
    """Extracting features from the map features endpoint with specified key

    :param key: The image key
    :type key: str

    :param fields: List of possible fields
    :type fields: list

    :return: GeoJSON
    :rtype: dict
    """

    # TODO: Requirement# 11A

    # ? The checking of the fields can be done within the /config/api/, right?    

    return {"Message": "Hello, World!"}


def get_feature_image_key_controller(key: str, fields: list) -> dict:
    """Extracting features from the image endpoint with specified key

    :param key: The image key
    :type key: str

    :param fields: List of possible fields
    :type fields: list

    :return: GeoJSON
    :rtype: dict
    """

    # TODO: Requirement# 11B

    # ? The checking of the fields for this endpoint are already
    # ? done within the Entity class
    # ? We should leave the checking of the fields to the /config/api/, right?

    return {"Message": "Hello, World!"}


def get_map_features_in_bbox_controller(bbox: list, layer: str, kwargs: dict) -> dict:
    """For extracing all map features within a bounding box

    :param bbox: Bounding box coordinates as argument
    :type bbox: list

    :param layer: 'Points' or 'Traffic' signs
    :type layer: str

    :param kwargs.value: Value list as argument (only one value or multiple values or “all”)
    :type kwargs.value: list or str

    :param kwargs.date: Date to filter by
    :type kwargs.date: str

    :return: GeoJSON
    :rtype: dict
    """

    # TODO: Requirement# 8
    # ? Maybe split this into 2 functions, one for
    # ? traffic signs and one for points

    return {"Message": "Hello, World!"}
