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
from controller.rules.key import valid_id

def get_image_detections_controller(image_id: int, kwargs: dict) -> dict:
    """Get image detections with given (image) key

    :param image_id: The image id
    :type image_id: str

    # TODO: To list out possible kwarg arguments
    :param kwargs: Possible key word arguments
    :type kwargs: dict

    :return: GeoJSON
    :rtype: dict
    """

    # Checks if the Id given is indeed a valid image_id
    valid_id(id=image_id, image=True)

    # Return results from the Adapter
    return EntityAdapter().fetch_detections(
        id=image_id,
        id_type=True,
        fields=kwargs["fields"] if "fields" in kwargs else [],
    )    


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