# Copyright (c) Facebook, Inc. and its affiliates. (http://www.facebook.com)
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

# Local imports

# # Adapter Imports
from models.api.entities import EntityAdapter

# # Rules
from controller.rules.verify import valid_id

def get_image_detections_controller(image_id: int, filters: dict) -> dict:
    """Get image detections with given (image) key

    :param image_id: The image id
    :type image_id: str

    # TODO: To list out possible kwarg arguments
    :param filters: Possible key word arguments
    :type filters: dict

    :return: GeoJSON
    :rtype: dict
    """

    # Checks if the Id given is indeed a valid image_id
    valid_id(id=image_id, image=True)

    # Return results from the Adapter
    return EntityAdapter().fetch_detections(
        id=image_id,
        id_type=True,
        fields=filters["fields"] if "fields" in filters else [],
    )

def get_map_feature_detections_controller(map_feature_id: str, filters: dict) -> dict:
    """Get image detections with given (map feature) key

    :param map_feature_id: The map feature id
    :type map_feature_id: str

    # TODO: To list out possible kwarg arguments
    :param filters: Possible key word arguments
    :type filters: dict

    :return: GeoJSON
    :rtype: dict
    """

    # Checks if the Id given is indeed a valid image_id
    valid_id(id=map_feature_id, image=False)
    
    # Return results from the Adapter
    return EntityAdapter().fetch_detections(
        id=map_feature_id,
        id_type=False,
        fields=filters["fields"] if "fields" in filters else [],
    )
