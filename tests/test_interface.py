# Copyright (c) Facebook, Inc. and its affiliates. (http://www.facebook.com)
# -*- coding: utf-8 -*-

"""
tests.test_interface

This module tests the interface functions provided at src/mapillary/interface

:copyright: (c) 2022 Facebook
:license: MIT LICENSE
"""

# Package imports
import json
import pytest
import logging
import datetime
import mercantile
import pandas as pd


# Local imports
import mapillary as mly
from tests.conftest import testing_envs

from dateutil.relativedelta import relativedelta

logger = logging.getLogger(__name__)


@pytest.mark.parametrize(
    "operation, expected",
    [
        (
            """mly.interface.traffic_signs_in_bbox(bbox={\"west\": west, \"south\": south, \"east\": east, \"north\": north},filter_values=traffic_sign_names,existed_at=str(time_now - relativedelta(years=1)).split(\".\")[0],existed_before=str(time_now).split(\".\")[0]))""",
            "KeyError: 'value'",
        )
    ],
)
def test_traffic_signs_in_bbox(test_initialize: dict, operation, expected):

    # Get the env dict
    testing_envs = test_initialize["testing_envs"]

    # Operation to test
    test_that = f"{operation} != {expected}"

    # Logging the intended operation to be tested
    logger.info(f"\n[traffic_signs_in_bbox] Test that {test_that}")

    # Read relevant traffic signs' names
    traffic_signs_names_path = testing_envs["TRAFFIC_SIGNS_FILTER_VALUES"]
    traffic_sign_names = pd.read_csv(traffic_signs_names_path)["name"].tolist()

    # Getting the parameters
    time_now = datetime.datetime.today()

    # Define relevant bounding tiles
    for tile in test_initialize["testing_tile_data"]:
        logger.info("--------------------------")
        logger.info(f"For (Tile(x={tile[0]}, y={tile[1]}, z={tile[2]})\n")
        z_tile = mercantile.Tile(x=int(tile[0]), y=int(tile[1]), z=int(tile[2]))
        west, south, east, north = mercantile.bounds(
            z_tile
        )  # get bbox coordinates of the vector tile

        # Dump file for better visualization
        json_res = json.loads(
            mly.interface.traffic_signs_in_bbox(
                # Make sure coordinates are inside the vector
                bbox={
                    "west": west + 0.01,
                    "south": south + 0.01,
                    "east": east - 0.01,
                    "north": north - 0.01,
                },
                filter_values=traffic_sign_names,
                existed_at=str(time_now - relativedelta(years=1)).split(".")[0],
                existed_before=str(time_now).split(".")[0],
            )
        )

        with open(
            f"{testing_envs['TRAFFIC_SIGNS_IN_BBOX_DIR']}/{z_tile.z}_{z_tile.x}_{z_tile.y}.json",
            "w",
        ) as traffic_signs_fp:
            json.dump(
                json_res,
                traffic_signs_fp,
                indent=2,
            )
