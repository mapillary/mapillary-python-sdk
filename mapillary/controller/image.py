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

# Package imports
from vt2geojson.tools import vt_bytes_to_geojson
from datetime import datetime  # Datetime
import mercantile
import requests
import ast

# Local imports

# # Utils
from utils.format import image_entity_to_geojson, merge_geojson
from utils.extract import extract_properties
from utils.filter import pipeline

# # Config
from config.api.vector_tiles import VectorTiles
from config.api.entities import Entities

# # Credentials
from models.credentials import Credentials

# # Exception Handling
from controller.rules.verify import kwarg_check_for_image_close_to


def get_image_close_to_controller(longitude, latitude, kwargs):

    # Checking if a non valid key
    # has been passed to the function
    # If that is the case, throw an exception
    kwarg_check_for_image_close_to(kwargs)

    # input coordinates
    input_coords = [longitude, latitude]
    zoom = kwargs["zoom"] if "zoom" in kwargs else 14
    # radius = kwargs["radius"] if "radius" in kwargs else 200
    results = []

    tile = mercantile.tile(input_coords[0], input_coords[1], zoom)

    # The endpoint 'https://tiles.mapillary.com/maps/vtp/'
    # 'mly_map_feature_point/2/{z}/{x}/{y}?access_token=XXX'
    # for id, value, first_seen_at, last_seen_at
    data = vt_bytes_to_geojson(
        requests.get(
            VectorTiles.get_map_feature_point(
                z=zoom,
                x=tile[0],
                y=tile[1],
            ),
            headers={"Authorization": f"OAuth {Credentials.token}"},
        ).content,
        tile.x,
        tile.y,
        tile.z,
    )

    # Filtering for the attributes obtained above
    if data["features"][0]["properties"] != {}:
        data = pipeline(
            data=data,
            components=[
                {"filter": "min_date", "min_timestamp": kwargs["min_date"]}
                if "min_date" in kwargs
                else {},
                {"filter": "max_date", "max_timestamp": kwargs["max_date"]}
                if "max_date" in kwargs
                else {},
                {"filter": "daterange", "radius": kwargs["daterange"]}
                if "daterange" in kwargs
                else {},
                {
                    "filter": "params",
                    "values": ["object--support--utility-pole", "object--street-light"],
                    "properties": "value",
                },
                # { 'filter': 'haversine_dist', 'radius': radius, 'coords':
                #   input_coords} # Confusing results
            ],
        )

    # * REFACTOR: The below logic should be adapted with
    # * Omar's Client implementation in the future

    # For the endpoint 'https://graph.mapillary.com/:image_id'
    # for fields, such as geometry and 'all' as mentioned in the requirement
    for image_id in extract_properties(data, ["id"])["id"]:
        results.append(
            image_entity_to_geojson(
                ast.literal_eval(
                    requests.get(
                        Entities.get_image(
                            image_id=image_id,
                            # ! FIX ME: The API is currently broken, see #35
                            fields=kwargs["fields"]
                            if "fields" in kwargs
                            else Entities.get_image_fields(),
                        ),
                        headers={"Authorization": f"OAuth {Credentials.token}"},
                    ).content.decode("utf-8")
                )
            )
        )

    # Merging results from the previous API calls with the latest
    # output results
    for result in results:
        data = merge_geojson(
            geojson_one=data,
            geojson_one_key="id",
            geojson_two=result,
            geojson_two_key="id",
            debug=False,
        )

    # For the endpoint 'https://tiles.mapillary.com/maps/vtp/mly1_public/'
    # '2{z}/{x}/{y}?access_token=XXX'
    # For the organization_id to filter via organization key, and is_pano
    # attribute for pano, flat or both
    new_data = vt_bytes_to_geojson(
        requests.get(
            VectorTiles.get_image_layer(
                z=zoom,
                x=tile[0],
                y=tile[1],
            ),
            headers={"Authorization": f"OAuth {Credentials.token}"},
        ).content,
        tile.x,
        tile.y,
        tile.z,
    )

    # # Filtering for the attributes obtained above
    # if new_data["features"][0]["properties"] != {}:
    #     new_data = pipeline(
    #         data=new_data,
    #         components=[
    #             {"filter": "min_date", "min_timestamp": kwargs["min_date"]}
    #             if "min_date" in kwargs
    #             else {},
    #             {"filter": "max_date", "max_timestamp": kwargs["max_date"]}
    #             if "max_date" in kwargs
    #             else {},
    #             {"filter": "daterange", "radius": kwargs["daterange"]}
    #             if "daterange" in kwargs
    #             else {},
    #             {
    #                 "filter": "params",
    #                 "values": ["object--support--utility-pole", "object--street-light"],
    #                 "properties": "value",
    #             },
    #             # { 'filter': 'haversine_dist', 'radius': radius, 'coords':
    #             #   input_coords} # Confusing results
    #         ],
    #     )

    data = merge_geojson(
        geojson_one=data,
        geojson_one_key="id",
        geojson_two=new_data,
        geojson_two_key="image_id",
        debug=False,
    )

    return data


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
