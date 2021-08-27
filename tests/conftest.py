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

    # The default token is the "Testing" token specially created for testing services
    # Ref:: 'PyTest Workflow for Mapillary API v4 Python SDK'
    token = "MLY|3976749565769581|3022bf582da20b0ce0bb44373289ebb2"

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
