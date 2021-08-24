# Copyright (c) Facebook, Inc. and its affiliates. (http://www.facebook.com)
# -*- coding: utf-8 -*-

"""
tests.conftest.py

This module loads variables needed to run the test

:copyright: (c) 2021 Facebook
:license: MIT LICENSE
"""

# Package imports
import pytest
import requests
import mercantile
from vt2geojson.tools import vt_bytes_to_geojson

@pytest.fixture(autouse=True)
def mly_access_token():
    """Specify the access token here"""

    token = "MLY|YYY"

    if "MLY|YYY" in token or "MLY|XXX" in token:
        raise ValueError("[tests.conftest]: MLY Access Token is not specified")

    return token


@pytest.fixture(autouse=True)
def data(mly_access_token):

    zoom, longitude, latitude = 14, 31, 30

    tile = mercantile.tile(lng=longitude, lat=latitude, zoom=zoom)

    data = vt_bytes_to_geojson(
        b_content=requests.get(
            f"https://tiles.mapillary.com/maps/vtp/mly1_public/2/14/{tile[0]}/{tile[1]}/"
            f"?access_token={mly_access_token}"
        ).content,
        x=tile.x,
        y=tile.y,
        z=tile.z,
        layer="image",
    )

    return {"data": data, "tile": tile, "longitude": longitude, "latitude": latitude}
