# Copyright (c) Facebook, Inc. and its affiliates. (http://www.facebook.com)
# -*- coding: utf-8 -*-

"""
tests.utils.test_filter
~~~~~~~~~~~~~~~~~~~~~~~~

For testing the functions under mapillary/utils/filter.py

:copyright: (c) 2021 Facebook
:license: MIT LICENSE
"""

# Package imports
import pytest
import logging  # Logger

# Local imports
from mapillary.utils.filter import pipeline  # Pipeline
from tests.conftest import data  # Data as fixture

logger = logging.getLogger(__name__)


@pytest.mark.parametrize(
    "operation, expected",
    [("pipeline(data=fetched_data, components=[...]", "len(data['features'])")],
)
def test_pipeline_min_captured_at(data: dict, operation, expected):

    # Operation to test
    test_that = f"len({operation}) != {expected}"

    # Logging the intended operation to be tested
    logger.info(f"\n[test_pipeline_min_captured_at] Test that {test_that}")

    # Get data from data fixture
    fetched_data, _, longitude, latitude = data.values()

    # Pass through pipeline. Actual data on left, operation on right
    actual = pipeline(
        data=fetched_data,
        components=[
            {
                "filter": "haversine_dist",
                "radius": 5000,
                "coords": [longitude, latitude],
            },
            {
                "filter": "min_captured_at",
                "min_timestamp": "2020-01-01",
            },
        ],
    )

    # What was expected left, what was actual on the right
    assert (
        len(actual) != len(fetched_data["features"])
        or len(fetched_data["features"]) == 0
    ), f"{test_that} failed, got {actual}"


@pytest.mark.parametrize(
    "operation, expected",
    [("pipeline(data=fetched_data, components=[...]", "len(data['features'])")],
)
def test_pipeline_haversine_dist(data: dict, operation, expected):

    # Operation to test
    test_that = f"len({operation}) != {expected}"

    # Logging the intended operation to be tested
    logger.info(f"\n[test_pipeline_haversine_dist] Test that {test_that}")

    # Get data from data fixture
    fetched_data, _, longitude, latitude = data.values()

    # Pass through pipeline. Actual data on left, operation on right
    actual = pipeline(
        data=fetched_data,
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
        ],
    )

    # What was expected left, what was actual on the right
    assert (
        len(actual) != len(fetched_data["features"])
        or len(fetched_data["features"]) == 0
    ), f"{test_that} failed, got {actual}"
