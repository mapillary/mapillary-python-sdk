# Copyright (c) Facebook, Inc. and its affiliates. (http://www.facebook.com)
# -*- coding: utf-8 -*-

"""
tests.helper.fetch
~~~~~~~~~~~~~~~~~~

This file contains the set of functions that are called by the client.py
in response to a query.

Contributions welcome!

:copyright: (c) 2021 Facebook
:license: MIT LICENSE
"""

# Package imports
import mercantile, requests
import vt2geojson.tools


def fetch_map_feature_point(access_token: str):
    """For fetching utility poles and street lights within a bounding using the Mercantile/Mapbox
    Vector Tile library

    Reference::
        1. 'https://blog.mapillary.com/update/2021/06/23/getting-started-with-the-new-mapillary-api-v4.html'
    """

    # define an empty geojson as output
    output = {"type": "FeatureCollection", "features": []}

    # a bounding box in [east_lng,_south_lat,west_lng,north_lat] format
    east, south, west, north = [
        -80.13423442840576,
        25.77376933762778,
        -80.1264238357544,
        25.788608487732198,
    ]

    filter_values = ["object--support--utility-pole", "object--street-light"]
    # get the tiles with x and y coors intersecting bbox at zoom 14 only
    tiles = list(mercantile.tiles(east, south, west, north, 14))

    # loop through all tiles to get IDs of Mapillary data
    for tile in tiles:

        # Creating the tile URL
        tile_url = (
            f"https://tiles.mapillary.com/maps/vtp/mly_map_feature_point/2/"
            f"{tile.z}/{tile.x}/{tile.y}?access_token={access_token}"
        )

        response = requests.get(tile_url)

        data = vt2geojson.tools.vt_bytes_to_geojson(
            response.content, tile.x, tile.y, tile.z
        )

        filtered_data = [
            feature
            for feature in data["features"]
            if feature["properties"]["value"] in filter_values
        ]

        for feature in filtered_data:

            if (
                feature["geometry"]["coordinates"][0] > east
                and feature["geometry"]["coordinates"][0] < west
            ) and (
                feature["geometry"]["coordinates"][1] > south
                and feature["geometry"]["coordinates"][1] < north
            ):

                output["features"].append(feature)

    return output
