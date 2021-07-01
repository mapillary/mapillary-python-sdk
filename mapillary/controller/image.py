"""
mapillary.mapillary
~~~~~~~~~~~~~~~~~~~

This module implements the basic functionalities
of the Mapillary Python SDK, a pythonic
implementation of the Mapillary API v4. For
more information, please check out
https://www.mapillary.com/developer/api-documentation/

:copyright: (c) 2021 ...
:license: See LICENSE for more details
"""

# Package imports
import mercantile
import requests
from vt2geojson.tools import vt_bytes_to_geojson
from haversine import haversine
from datetime import datetime  # Datetime

# Local imports

# # Utils
from utils.filter import filter_max_date, filter_min_date, filter_params

# # Config
from config.api.vector_tiles import VectorTiles

# # Credentials
from models.credentials import Credentials

# # Exception Handling
from models.exceptions import ContradictingError, InvalidKwargError, OutOfBoundZoomError


def get_image_close_to_controller(longitude, latitude, kwargs):

    # Checking if a non valid key
    # has been passed to the function
    # If that is the case, throw an exception
    print(kwargs)

    if kwargs is not None:
        for key in kwargs.keys():
            if key not in [
                "min_date",
                "max_date",
                "daterange",
                "radius",
                "coverage",
                "org_id",
                "fields",
            ]:
                raise InvalidKwargError(
                    "get_image_close_to",
                    key,
                    kwargs[key],
                    [
                        "min_date",
                        "max_date",
                        "daterange",
                        "radius",
                        "coverage",
                        "org_id",
                        "fields",
                    ],
                )

    # Check if two contradicting keys have
    # not been given
    if ("min_date" in kwargs or "max_date" in kwargs) and ("daterange" in kwargs):
        raise ContradictingError(
            "daterange",
            "min_date/max_date",
            "Using either or both of min_date and max_date, or use daterange, "
            "but not both at the same time",
        )

    # Checking if an invalid zoom value has
    # not been given
    if ("zoom" in kwargs) and (kwargs["zoom"] < 14 or kwargs["zoom"] > 17):
        raise OutOfBoundZoomError(kwargs["zoom"], [14, 15, 16, 17])

    # Define an empty geojson as output
    output = {"type": "FeatureCollection", "features": []}

    # input coordinates
    input_coords = [longitude, latitude]
    zoom = kwargs["zoom"] if "zoom" in kwargs else 14
    filter_radius = kwargs["radius"] if "radius" in kwargs else 100

    tile = mercantile.tile(input_coords[0], input_coords[1], zoom)

    tile_url = VectorTiles.get_map_feature_point(
        z=zoom,
        x=tile[0],
        y=tile[1],
        options=kwargs["fields"] if "fields" in kwargs else [],
    )

    response = requests.get(
        tile_url,
        headers={
            "Authorization": f"OAuth \
        {Credentials.token}"
        },
    )

    data = vt_bytes_to_geojson(response.content, tile.x, tile.y, tile.z)

    if "min_date" in kwargs:
        data = filter_min_date(data, kwargs["min_date"])

    if "max_date" in kwargs:
        data = filter_max_date(data, kwargs["max_date"])

    if "daterange" in kwargs:
        data = filter_max_date(
            filter_min_date(data, kwargs["min_date"]), kwargs["max_date"]
        )

    filtered_data = filter_params(
        data, ["object--support--utility-pole", "object--street-light"], "value"
    )

    for feature in filtered_data:
        distance = haversine(input_coords, feature["geometry"]["coordinates"], unit="m")

    if distance < filter_radius:
        output["features"].append(feature)

    return output, data


def get_image_looking_at_controller(
    coordinates_looker,
    coordinates_at,
    fields=["all"],
    radius=200,
    coverage="pano",
    date=datetime.today().strftime("%Y-%m-%d"),
    org_id=-1,
):

    return None


def get_image_thumbnail_from_key_controller(map_key, size=1024):

    return "https://www.mapillary.com/"


def get_images_in_bbox_controller(bbox, **filters):

    return {"Message": "Hello, World!"}


def get_all_images_in_a_shape_controller(geoJSON, **filters):

    return None
