"""
mapillary.controllers.image
~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the image filtering and analysis business logic functionalities of the
Mapillary Python SDK.

For more information, please check out https://www.mapillary.com/developer/api-documentation/

:copyright: (c) 2021 Facebook
:license: MIT LICENSE
"""

# Local imports

# # Entities
from config.api.entities import Entities

# # Exception Handling
from models.exceptions import InvalidImageResolution, InvalidImageKey
from controller.rules.verify import image_check, thumbnail_size_check, shape_bbox_check

# # Client
from models.client import Client

# # Adapters
from models.api.vector_tiles import VectorTilesAdapter

# # Utilities
from utils.filter import pipeline

# Library imports
import json
from requests import HTTPError

def get_image_close_to_controller(
    longitude: float,
    latitude: float,
    kwargs: dict,
) -> dict:
    """Extracting the GeoJSON for the image data near the [longitude, latitude] coordinates

    :param longitude: The longitude
    :type longitude: float

    :param latitude: The latitude
    :type latitude: float

    :param kwargs.min_date: The minimum date to filter till
    :type kwargs.min_date: str

    :param kwargs.max_date: The maximum date to filter upto
    :type kwargs.max_date: str

    :param kwargs.daterange: A list of a range to filter by
    :type kwargs.daterange: list

    :param kwargs.radius: The radius that the geometry points will lie in
    :type kwargs.radius: float

    :param kwargs.image_type: Either 'pano', 'flat' or 'all'
    :type kwargs.image_type: str

    :param kwargs.org_id: The organization to retrieve the data for. Use 856718694933026 for
    testing
    :type kwargs.org_id: str

    :param kwargs.fields: Fields to pass to the endpoint
    :type kwargs.fields: list[str]

    :return: GeoJSON
    :rtype: dict
    """

    # Checking if a non valid key has been passed to the function If that is the case, throw an
    # exception
    image_check(kwargs=kwargs)

    data = VectorTilesAdapter().fetch_layer(
        layer="image",
        zoom=kwargs["zoom"] if "zoom" in kwargs else 14,
        longitude=longitude,
        latitude=latitude,
    )

    # Filtering for the attributes obtained above
    if data['features'] != {} and data["features"][0]["properties"] != {}:
        return pipeline(
            data=data,
            components=[
                {"filter": "image_type", "tile": kwargs["image_type"]}
                if "image_type" in kwargs
                else {},

                {"filter": "organization_id", "organization_ids": kwargs["org_id"]}
                if "org_id" in kwargs
                else {},

                {
                    "filter": "haversine_dist",
                    "radius": kwargs["radius"] if 'radius' in kwargs else 1000,
                    "coords": [longitude, latitude],
                }
            ],
        )

def get_image_looking_at_controller(
    coordinates_looker: tuple,
    coordinates_at: tuple,
    kwargs: dict,
) -> dict:
    """Extracting the GeoJSON for the image data from a 'looker' and 'at' coordinate view

    :param coordinates_looker: The tuple of coordinates of the position of the looking from
    coordinates, in the format (long, lat)
    :type longitude: tuple

    :param coordinates_at: The tuple of coordinates of the position of the looking at
    coordinates, in the format (long, lat)
    :type latitude: tuple

    :param kwargs.min_date: The minimum date to filter till
    :type kwargs.min_date: str

    :param kwargs.max_date: The maximum date to filter upto
    :type kwargs.max_date: str

    :param kwargs.daterange: A list of a range to filter by
    :type kwargs.daterange: list

    :param kwargs.radius: The radius that the geometry points will lie in
    :type kwargs.radius: float

    :param kwargs.image_type: Either 'pano', 'flat' or 'all'
    :type kwargs.image_type: str

    :param kwargs.org_id: The organization to retrieve the data for
    :type kwargs.org_id: str

    :param kwargs.fields: Fields to pass to the endpoint
    :type kwargs.fields: list[str]

    :return: GeoJSON
    :rtype: dict
    """

    # TODO: Requirement# 3

    # Checking if a non valid key
    # has been passed to  the function
    # If that is the case, throw an exception
    image_check(kwargs=kwargs)
    
    return {"Message": "Hello, World!"}

def get_image_thumbnail_controller(image_id, resolution: int) -> str:
    """This controller holds the business logic for retrieving
    an image thumbnail with a specific resolution (256, 1024, or 2048)
    using an image ID/key

    :param image_id: Image key as the argument

    :param resolution: Option for the thumbnail size, with available resolutions:
    256, 1024, and 2048

    :return: A URL for the thumbnail
    :rtype: str
    """

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

def get_images_in_bbox_controller(bbox: list, kwargs: dict) -> dict:
    """For getting a complete list of images that lie within a bounding box, that can be filered via the kwargs argument

    :param bbox: A bounding box representation ([east, south, west, north] as coordinates)
    :type bbox: list

    :param kwargs.max_date: The max date that can be filtered upto
    :type kwargs.max_date: str

    :param kwargs.min_date: The min date that can be filtered from
    :type kwargs.min_date: str

    :param kwargs.is_pano: Either 'pano', 'flat' or 'all'
    :type kwargs.is_pano: str

    '''
    :raise InvalidKwargError: Raised when a function is called with the invalid keyword argument(s)
    that do not belong to the requested API end call
    '''

    :return: GeoJSON
    :rtype: dict
    """

    # TODO: Requirement# 7

    shape_bbox_check(kwargs)

    return {"Message": "Hello, World!"}


def get_images_in_shape_controller(data: dict, is_geojson: bool = True,
    kwargs: dict = None) -> dict:
    """For extracting images that lie within a shape, either GeoJSON or a Bounding Box, and merges
    the results of the found GeoJSON(s) into a single object - by merging all the features into
    one list in a feature collection.

    A bounding box is in the list order of ([east, south, west, north])

    :param data: GeoJSON | Bounding Box (Bbox)
    :type data: dict | list

    :param is_geojson: True if GeoJSON object will be passed, else False if Bbox, defaults to True
    :type is_geojson: bool

    :param kwargs.max_date: The max date that can be filtered upto
    :type kwargs.max_date: str

    :param kwargs.min_date: The min date that can be filtered from
    :type kwargs.min_date: str

    :param kwargs.is_pano: Either 'pano', 'flat' or 'all'
    :type kwargs.is_pano: str

    '''
    :raise InvalidKwargError: Raised when a function is called with the invalid keyword argument(s)
    that do not belong to the requested API end call
    '''

    :return: GeoJSON
    :rtype: dict
    """

    # TODO: Requirement# 9    

    shape_bbox_check(kwargs)

    return {"Message": "Hello, World!"}
