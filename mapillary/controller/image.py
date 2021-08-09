# Copyright (c) Facebook, Inc. and its affiliates. (http://www.facebook.com)
# -*- coding: utf-8 -*-

"""
mapillary.controllers.image
~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the image filtering and analysis business logic functionalities of the
Mapillary Python SDK.

For more information, please check out https://www.mapillary.com/developer/api-documentation/

:copyright: (c) 2021 Facebook
:license: MIT LICENSE
"""

# Configs
from config.api.entities import Entities
from config.api.vector_tiles import VectorTiles

# Exception Handling
from models.exceptions import InvalidImageKey
from utils.verify import (
    image_check,
    image_bbox_check,
    sequence_bbox_check,
    resolution_check,
)

# Client
from models.client import Client

# # Adapters
from models.api.vector_tiles import VectorTilesAdapter

# # Class Representation
from models.geojson import GeoJSON

# # Utilities
from utils.filter import pipeline
from utils.format import (
    geojson_to_features_list,
    merged_features_list_to_geojson,
    geojson_to_polgyon,
)

# Library imports
import json
import mercantile
from requests import HTTPError
from shapely.geometry import shape
from vt2geojson.tools import vt_bytes_to_geojson


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

    :param kwargs.image_type: Either 'pano', 'flat' or 'all'
    :type kwargs.image_type: str

    :param kwargs.organization_id: The organization to retrieve the data for
    :type kwargs.organization_id: str

    :param kwargs.radius: The radius that the geometry points will lie in
    :type kwargs.radius: float

    :return: GeoJSON
    :rtype: dict
    """

    # Checking if a non valid key has been passed to the function If that is the case, throw an
    # exception
    image_check(kwargs=kwargs)

    unfiltered_data = VectorTilesAdapter().fetch_layer(
        layer="image",
        zoom=kwargs["zoom"] if "zoom" in kwargs else 14,
        longitude=longitude,
        latitude=latitude,
    )

    # Filtering for the attributes obtained above
    if (
        unfiltered_data["features"] != {}
        and unfiltered_data["features"][0]["properties"] != {}
    ):
        return pipeline(
            data=unfiltered_data,
            components=[
                # Filter using kwargs.min_date
                {"filter": "min_date", "min_timestamp": kwargs["min_date"]}
                if "min_date" in kwargs
                else {},
                # Filter using kwargs.max_date
                {"filter": "max_date", "min_timestamp": kwargs["max_date"]}
                if "max_date" in kwargs
                else {},
                # Filter using kwargs.image_type
                {"filter": "image_type", "tile": kwargs["image_type"]}
                if "image_type" in kwargs
                else {},
                # Filter using kwargs.organization_id
                {"filter": "organization_id", "organization_ids": kwargs["org_id"]}
                if "org_id" in kwargs
                else {},
                # Filter using kwargs.radius
                {
                    "filter": "haversine_dist",
                    "radius": kwargs["radius"],
                    "coords": [longitude, latitude],
                }
                if "radius" in kwargs
                else {},
            ],
        )


def get_image_looking_at_controller(
    looker: dict,
    at: dict,
    filters: dict,
) -> dict:
    """Extracting the GeoJSON for the image data from a 'looker' and 'at' coordinate view

    :param looker: The dictionary of coordinates of the position of the looking from
    coordinates, in the format,
        >>> looker = {
        >>>     'lng': <longitudinal parameter>
        >>>     'lat': <latitude parameters>
        >>> }
    :type looker: dict

    :param at: The dict of coordinates of the position of the looking at
    coordinates, in the format,
        >>> at = {
        >>>     'lng': <longitudinal parameter>
        >>>     'lat': <latitude parameters>
        >>> }
    :type at: dict

    :param filters.min_date: The minimum date to filter till
    :type filters.min_date: str

    :param filters.max_date: The maximum date to filter upto
    :type filters.max_date: str

    :param filters.radius: The radius that the geometry points will lie in
    :type filters.radius: float

    :param filters.image_type: Either 'pano', 'flat' or 'all'
    :type filters.image_type: str

    :param filters.organization_id: The organization to retrieve the data for
    :type filters.organization_id: str

    :return: GeoJSON
    :rtype: dict
    """

    # Checking if a non valid key
    # has been passed to  the function
    # If that is the case, throw an exception
    image_check(kwargs=filters)

    looker = json.loads(
        get_image_close_to_controller(
            longitude=looker["lng"], latitude=looker["lat"], kwargs=filters
        )
    )

    # Filter the unfiltered rsults by the given filters
    if looker["features"] != [] and looker["features"][0]["properties"] != {}:
        return merged_features_list_to_geojson(
            pipeline(
                data=looker,
                components=[
                    # Filter by `max_date`
                    {"filter": "max_date", "max_timestamp": filters.get("max_date")}
                    if "max_date" in filters
                    else {},
                    # Filter by `min_date`
                    {"filter": "min_date", "min_timestamp": filters.get("min_date")}
                    if "min_date" in filters
                    else {},
                    # Filter by `image_type`
                    {"filter": "image_type", "type": filters.get("image_type")}
                    if "image_type" in filters and filters["image_type"] != "all"
                    else {},
                    # Filter by `organization_id`
                    {
                        "filter": "organization_id",
                        "organization_ids": filters.get("organization_id"),
                    }
                    if "organization_id" in filters
                    else {},
                    # Filter by `hits_by_look_at`
                    {"filter": "hits_by_look_at", "at": at},
                ],
            )
        )


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
    resolution_check(resolution)

    try:
        res = Client().get(Entities.get_image(image_id, [f"thumb_{resolution}_url"]))
    except HTTPError:
        # If given ID is an invalid image ID, let the user know
        raise InvalidImageKey(image_id)

    return json.loads(res.content.decode("utf-8"))[f"thumb_{resolution}_url"]


def get_images_in_bbox_controller(
    bbox: dict, layer: str, zoom: int, filters: dict
) -> str:
    """For getting a complete list of images that lie within a bounding box,
     that can be filered via the filters argument

    :param bbox: A bounding box representation
    example: {
        'west': 'BOUNDARY_FROM_WEST',
        'south': 'BOUNDARY_FROM_SOUTH',
        'east': 'BOUNDARY_FROM_EAST',
        'north': 'BOUNDARY_FROM_NORTH'
    }
    :type bbox: dict

    :param filters.max_date: The max date that can be filtered upto
    :type filters.max_date: str

    :param filters.min_date: The min date that can be filtered from
    :type filters.min_date: str

    :param filters.image_type: Either 'pano', 'flat' or 'all'
    :type filters.image_type: str

    :param filters.compass_angle:
    :type filters.compass_angle: float

    :param filters.organization_id:
    :type filters.organization_id: int

    :param filters.sequence_id:
    :type filters.sequence_id: str

    '''
    :raise InvalidKwargError: Raised when a function is called with the invalid keyword argument(s)
    that do not belong to the requested API end call
    '''

    :return: GeoJSON
    :rtype: str

    Reference: https://www.mapillary.com/developer/api-documentation/#coverage-tiles
    """

    # Check if the given filters are valid ones
    filters["zoom"] = filters.get("zoom", zoom)
    filters = (
        image_bbox_check(filters) if layer == "image" else sequence_bbox_check(filters)
    )

    # Instantiate the Client
    client = Client()

    # filtered images or sequence data will be appended to this list
    filtered_results = []

    # A list of tiles that are either confined within or intersect with the bbox
    tiles = list(
        mercantile.tiles(
            west=bbox["west"],
            south=bbox["south"],
            east=bbox["east"],
            north=bbox["north"],
            zooms=zoom,
        )
    )

    for tile in tiles:
        url = (
            VectorTiles.get_image_layer(x=tile.x, y=tile.y, z=tile.z)
            if layer == "image"
            else VectorTiles.get_sequence_layer(x=tile.x, y=tile.y, z=tile.z)
        )

        # Get the response from the API
        res = client.get(url)

        # Get the GeoJSON response by decoding the byte tile
        geojson = vt_bytes_to_geojson(
            b_content=res.content, layer=layer, z=tile.z, x=tile.x, y=tile.y
        )

        # Separating feature objects from the decoded data
        unfiltered_results = geojson_to_features_list(geojson)

        # Filter the unfiltered results by the given filters
        filtered_results.extend(
            pipeline(
                data=unfiltered_results,
                components=[
                    {"filter": "features_in_bounding_box", "bbox": bbox}
                    if layer == "image"
                    else {},
                    {"filter": "max_date", "max_timestamp": filters.get("max_date")}
                    if filters["max_date"] is not None
                    else {},
                    {"filter": "min_date", "min_timestamp": filters.get("min_date")}
                    if filters["min_date"] is not None
                    else {},
                    {"filter": "image_type", "type": filters.get("image_type")}
                    if filters["image_type"] is not None
                    or filters["image_type"] != "all"
                    else {},
                    {
                        "filter": "organization_id",
                        "organization_ids": filters.get("organization_id"),
                    }
                    if filters["organization_id"] is not None
                    else {},
                    {"filter": "sequence_id", "ids": filters.get("sequence_id")}
                    if layer == "image" and filters["sequence_id"] is not None
                    else {},
                    {"filter": "compass_angle", "angles": filters.get("compass_angle")}
                    if layer == "image" and filters["compass_angle"] is not None
                    else {},
                ],
            )
        )

    return merged_features_list_to_geojson(filtered_results)


def get_image_from_key_controller(key: int, fields: list) -> str:
    """
    A controller for getting properties of a certain image given the image key and
    the list of fields/properties to be returned
    :param key: The image key
    :type key: int

    :param fields: The list of fields to be returned
    :type fields: list

    :return: The requested image properties in GeoJSON format
    :rtype: str
    """


def images_in_geojson_controller(geojson: dict, filters: dict = None) -> dict:
    """For extracting images that lie within a GeoJSON and merges the results of the found
    GeoJSON(s) into a single object - by merging all the features into one feature list.

    :param geojson: The geojson to act as the query extent
    :type geojson: dict

    :param **filters: Different filters that may be applied to the output, defaults to {}
    :type filters: dict (kwargs)

    :param filters.zoom: The zoom level to obtain vector tiles for, defaults to 14
    :type filters.zoom: int

    :param filters.max_date: The max date. Format from 'YYYY', to 'YYYY-MM-DDTHH:MM:SS'
    :type filters.max_date: str

    :param filters.min_date: The min date. Format from 'YYYY', to 'YYYY-MM-DDTHH:MM:SS'
    :type filters.min_date: str

    :param filters.image_type: The tile image_type to be obtained, either as 'flat', 'pano'
    (panoramic), or 'all'. See https://www.mapillary.com/developer/api-documentation/ under
    'image_type Tiles' for more information
    :type filters.image_type: str

    :param filters.compass_angle: The compass angle of the image
    :type filters.compass_angle: int

    :param filters.sequence_id: ID of the sequence this image belongs to
    :type filters.sequence_id: str

    :param filters.organization_id: ID of the organization this image belongs to. It can be absent
    :type filters.organization_id: str

    '''
    :raise InvalidKwargError: Raised when a function is called with the invalid keyword argument(s)
    that do not belong to the requested API end call
    '''

    :return: A feature collection as a GeoJSON
    :rtype: dict
    """

    # TODO: Requirement# 9.1

    # Filter checking
    image_bbox_check(filters)

    # Get a GeoJSON with features from tiles originating from coordinates
    # at specified zoom level
    layers: GeoJSON = VectorTilesAdapter().fetch_layers(
        # Sending coordinates for all the points within input geojson
        coordinates=[
            feature["geometry"]["coordinates"] for feature in geojson["features"]
        ],
        # Fetching image layers for the geojson
        layer="image",
        # Specifying zoom level, defaults to zoom if zoom not specified
        zoom=filters['zoom'] if 'zoom' in filters else 14,
    )

    # Extracting polygon from geojson, converting to dict
    polygon = geojson_to_polgyon(geojson).to_dict()

    # Getting the boundary paramters from polygon
    boundary = shape(polygon["features"][0]["geometry"])

    # Generating output format
    output = {"type": "FeatureCollection", "features": []}

    # Iterating over features
    for feature in layers.features:

        # Extracting point from geometry feature
        point = shape(feature["geometry"])

        # Checking if point falls within the boundary using shapely.geometry.point.point
        if boundary.contains(point):

            # If true, append to output features
            output["features"].append(feature)

    # Return as GeoJSON output
    return GeoJSON(geojson=output)


def images_in_shape_controller(shape, filters: dict = None) -> dict:
    """For extracting images that lie within a shape, merging the results of the found features
    into a single object - by merging all the features into one list in a feature collection.

    :param shape: ??? # ! Fill in documentation
    :type shape: ??? # ! Fill in documentation

    :param **filters: Different filters that may be applied to the output, defaults to {}
    :type filters: dict (kwargs)

    :param filters.max_date: The max date. Format from 'YYYY', to 'YYYY-MM-DDTHH:MM:SS'
    :type filters.max_date: str

    :param filters.min_date: The min date. Format from 'YYYY', to 'YYYY-MM-DDTHH:MM:SS'
    :type filters.min_date: str

    :param filters.image_type: The tile image_type to be obtained, either as 'flat', 'pano'
    (panoramic), or 'all'. See https://www.mapillary.com/developer/api-documentation/ under
    'image_type Tiles' for more information
    :type filters.image_type: str

    :param filters.compass_angle: The compass angle of the image
    :type filters.compass_angle: int

    :param filters.sequence_id: ID of the sequence this image belongs to
    :type filters.sequence_id: str

    :param filters.organization_id: ID of the organization this image belongs to. It can be absent
    :type filters.organization_id: str

    '''
    :raise InvalidKwargError: Raised when a function is called with the invalid keyword argument(s)
    that do not belong to the requested API end call
    '''

    :return: A feature collection as a GeoJSON
    :rtype: dict
    """

    # TODO: Requirement# 9.2

    image_bbox_check(filters)

    return {"Message": "Hello, World!"}
