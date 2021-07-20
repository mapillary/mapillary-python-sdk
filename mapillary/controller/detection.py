# -*- coding: utf-8 -*-

"""
mapillary.controllers.detection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the detection based business logic functionalities of the Mapillary
Python SDK.

For more information, please check out https://www.mapillary.com/developer/api-documentation/

:copyright: (c) 2021 Facebook
:license: MIT LICENSE
"""


def get_image_detections_controller(key: str) -> dict:
    """Get image detections with given (image) key

    :param key: The image key
    :type key: str

    :return: GeoJSON
    :rtype: dict
    """

    # TODO: Requirement# 4
    # TODO: Needs to have key checked if it belongs to an image

    return {"Message": "Hello, World!"}


def get_map_feature_detections_controller(key: str) -> dict:
    """Get image detections with given (map feature) key

    :param key: The map feature key
    :type key: str

    :return: GeoJSON
    :rtype: dict
    """

    # TODO: Requirement# 5
    # TODO: Needs to have key checked if it belongs to a map_feature

    return {"Message": "Hello, World!"}
