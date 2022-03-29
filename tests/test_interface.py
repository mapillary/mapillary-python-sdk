# Copyright (c) Facebook, Inc. and its affiliates. (http://www.facebook.com)
# -*- coding: utf-8 -*-

"""
tests.interface

This module loads variables needed to run the test

:copyright: (c) 2021 Facebook
:license: MIT LICENSE
"""

# Package imports
import json
import pytest
import logging
import datetime
import mercantile


# Local imports
import mapillary as mly
from tests.conftest import data

from dateutil.relativedelta import relativedelta

logger = logging.getLogger(__name__)


@pytest.mark.parametrize("operation, expected", [])
def test_traffic_signs_in_bbox(data: dict, operation, expected):

    # Operation to test
    test_that = f"{operation} != {expected}"

    # Logging the intended operation to be tested
    logger.info(f"\n[traffic_signs_in_bbox] Test that {test_that}")

    # Getting the parameters
    time_now = datetime.datetime.today()

    # Define relevant bounding tiles
    monaco_z_tile = mercantile.Tile(x=2132, y=1439, z=12)
    west, south, east, north = mercantile.bounds(
        monaco_z_tile
    )  # get bbox coordinates of the vector tile

    # Make sure coordinates are inside the vector
    west += 0.01
    south += 0.01
    east -= 0.01
    north -= 0.01

    # Actual data on left, operation on right
    actual = mly.interface.traffic_signs_in_bbox(
        bbox={"west": west, "south": south, "east": east, "north": north},
        filter_values=[],
        existed_at=str(time_now - relativedelta(years=1)).split(".")[0],
        existed_before=str(time_now).split(".")[0],
    )

    # Dump file for better visualization
    json_res = json.loads(actual)
    json.dump(
        json_res,
        open(
            f"/monaco_{monaco_z_tile.z}_{monaco_z_tile.x}_{monaco_z_tile.y}.json", "w+"
        ),
        indent=4,
    )
    json.dump(json_res, open(""))
