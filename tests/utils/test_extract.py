# Copyright (c) Facebook, Inc. and its affiliates. (http://www.facebook.com)
# -*- coding: utf-8 -*-

"""
tests.utils.test_extract
~~~~~~~~~~~~~~~~~~~~~~~~

For testing the functions under mapillary/utils/extract.py

:copyright: (c) 2021 Facebook
:license: MIT LICENSE
"""

import requests
import mercantile
from vt2geojson.tools import vt_bytes_to_geojson
from mapillary.utils.extract import extract_properties

def test_extract_properties(properties: list) -> dict:

    tile = mercantile.tile(lng=31, lat=30, zoom=14)

    data = vt_bytes_to_geojson(
        b_content=requests.get(
            f"https://tiles.mapillary.com/maps/vtp/mly1_public/2/14/{tile[0]}/{tile[1]}/?access_token=MLY|4352045404840373|b35c62c790e9b52c8476cfd08eb58704"
        ).content,
        x=tile.x,
        y=tile.y,
        z=tile.z,
        layer="image",
    )

    extracted = extract_properties(data, properties)

    assert('id' in extracted)

    assert(len(extracted['id']) != 0)

    return {"Test": "Success"}

if __name__ == '__main__':
    test_extract_properties(['id'])