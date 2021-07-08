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

# # Utils
from utils.filter import pipeline
from utils.format import merge_geojson

# # Client
from models.api.vector_tiles import VectorTilesAdapter

# # Exception Handling
from controller.rules.verify import kwarg_check_for_images


def get_image_close_to_controller(
    longitude: float,
    latitude: float,
    kwargs: dict,
) -> dict:

    # Checking if a non valid key
    # has been passed to the function
    # If that is the case, throw an exception
    kwarg_check_for_images(kwargs)

    data = VectorTilesAdapter().fetch_layer(
        layer="image",
        zoom=kwargs["zoom"] if "zoom" in kwargs else 14,
        longitude=longitude,
        latitude=latitude,
    )

    # Filtering for the attributes obtained above
    if data["features"][0]["properties"] != {}:
        return pipeline(
            data=data,
            components=[
                {"filter": "coverage", "tile": kwargs["coverage"]}
                if "coverage" in kwargs
                else {},
                {"filter": "organization_id", "organization_ids": kwargs["org_id"]}
                if "org_id" in kwargs
                else {},
                {
                    "filter": "haversine_dist",
                    "radius": kwargs["radius"],
                    "coords": [longitude, latitude],
                }
                if "radius" in kwargs
                else 1000,
            ],
        )


def get_image_looking_at_controller(
    coordinates_looker: tuple,
    coordinates_at: tuple,
    kwargs: dict,
) -> dict:

    looker = get_image_close_to_controller(
        coordinates_looker[0], coordinates_looker[1], kwargs
    )

    at = get_image_close_to_controller(coordinates_at[0], coordinates_at[1], kwargs)

    return merge_geojson(looker, "id", at, "id")


def get_image_thumbnail_from_key_controller(map_key, size=1024):

    return "https://www.mapillary.com/"


def get_images_in_bbox_controller(bbox, **filters):

    return {"Message": "Hello, World!"}


def get_images_in_shape_controller(geoJSON, **filters):

    return None
