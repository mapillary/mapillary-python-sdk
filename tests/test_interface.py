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
from mapillary.models.geojson import Coordinates

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


@pytest.mark.parametrize(
    "operation, expected, equality",
    [
        (
            """mly.interface.is_image_being_looked_at(at={'lng': 21.396712884299973, 'lat': 41.99463190510002})""",
            """True""",
            "==",
        )
    ],
)
def test_is_image_being_looked_at_with_no_params(
    test_initialize: dict, operation: str, expected: str, equality: str
):

    # Get the env dict
    testing_envs: dict = test_initialize["testing_envs"]

    # Operation to test
    test_that: str = f"{operation} {equality} {expected}"

    # Logging the intended operation to be tested
    logger.info(f"\n[is_image_being_looked_at] Test that {test_that}")

    # Get the parameters
    at: Coordinates = Coordinates(
        longitude=21.396712884299973, latitude=41.99463190510002
    )

    # Checking for boolean result
    boolean_result: bool = mly.interface.is_image_being_looked_at(at=at) == "True"

    with open(
        f"{testing_envs['DUMP_DIRECTORY']}/{at.longitude}_{at.latitude}.json",
        "w",
    ) as is_image_being_looked_at_fp:
        json.dump(
            boolean_result,
            is_image_being_looked_at_fp,
            indent=2,
        )
