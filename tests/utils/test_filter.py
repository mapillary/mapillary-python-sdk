# Copyright (c) Facebook, Inc. and its affiliates. (http://www.facebook.com)
# -*- coding: utf-8 -*-

"""
tests.utils.test_filter
~~~~~~~~~~~~~~~~~~~~~~~~

For testing the functions under mapillary/utils/filter.py

:copyright: (c) 2021 Facebook
:license: MIT LICENSE
"""


import requests
import mercantile
from vt2geojson.tools import vt_bytes_to_geojson
from mapillary.utils.filter import pipeline


def test_pipeline(zoom, longitude, latitude):

    tile = mercantile.tile(lng=longitude, lat=latitude, zoom=zoom)

    data = vt_bytes_to_geojson(
        b_content=requests.get(
            f"https://tiles.mapillary.com/maps/vtp/mly1_public/2/14/{tile[0]}/{tile[1]}/?access_token=MLY|4352045404840373|b35c62c790e9b52c8476cfd08eb58704"
        ).content,
        x=tile.x,
        y=tile.y,
        z=tile.z,
        layer="image",
    )

    result = pipeline(
        data=data,
        components=[
            {
                "filter": "haversine_dist",
                "radius": 5000,
                "coords": [longitude, latitude],
            },
            {
                "filter": "haversine_dist",
                "radius": 1000,
                "coords": [longitude, latitude],
            },
            {
                "filter": "min_date",
                "min_timestamp": '2020-01-01',
            },
        ],
    )

    print(len(result['features']))    
    assert(len(result['features']) != len(data['features']))

    result = pipeline(
        data=data,
        components=[
            {
                "filter": "haversine_dist",
                "radius": 5000,
                "coords": [longitude, latitude],
            },
            {
                "filter": "haversine_dist",
                "radius": 800,
                "coords": [longitude, latitude],
            },
        ],
    )

    print(len(result['features']))
    assert(len(result['features']) != len(data['features']))

    result = pipeline(
        data=data,
        components=[
            {
                "filter": "haversine_dist",
                "radius": 5000,
                "coords": [longitude, latitude],
            },
        ],
    )

    print(len(result['features']))
    assert(len(result['features']) == len(data['features']))

if __name__ == '__main__':
    test_pipeline(zoom=14, longitude=31, latitude=30)