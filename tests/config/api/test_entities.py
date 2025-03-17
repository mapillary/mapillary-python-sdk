# Copyright (c) Facebook, Inc. and its affiliates. (http://www.facebook.com)
# -*- coding: utf-8 -*-

"""
tests.config.api.test_entities

This module tests the interface functions provided at src/mapillary/interface

:copyright: (c) 2022 Facebook
:license: MIT LICENSE
"""

# Package imports
import datetime
import logging
from multiprocessing.sharedctypes import Value
from mapillary.models.exceptions import InvalidFieldError
import pytest

# Local imports
from mapillary.models.config import Config
from mapillary.models.logger import Logger
from mapillary.config.api.entities import Entities

logger: logging.Logger = Logger.setup_logger(
    name="mapillary.tests.config.api.test_entities"
)


@pytest.mark.parametrize(
    "operation, expected",
    [
        (
            (
                "mly.config.api.entities.search_for_images(bbox=[62.22656249999999, 48.1640625,"
                "38.41055825094609, 45.336701909968134])"
            ),
            (
                "https://graph.mapillary.com/images?bbox=62.22656249999999,48.1640625,"
                "38.41055825094609,45.336701909968134"
            ),
        )
    ],
)
def test_search_for_images__only_bbox(operation, expected):

    # Operation to test
    test_that = f"{operation} == {expected}"

    # Logging the intended operation to be tested
    logger.info(f"[search_for_images] Test that {test_that}")

    # Actual data on left, operation on right
    actual: str = Entities.search_for_images(
        bbox=[62.22656249999999, 48.1640625, 38.41055825094609, 45.336701909968134]
    )

    logger.info(f"[search_for_images] Actual: {actual}, Expected: {expected}")
    # What was expected left, what was actual on the right
    assert actual == expected, f"'{test_that}' failed, got {actual}"


@pytest.mark.parametrize(
    "operation, expected",
    [
        (
            (
                "mly.config.api.entities.search_for_images(bbox=[62.22656249999999, 48.1640625",
                "38.41055825094609, 45.336701909968134], start_captured_at='2020-01-01T16:14:20Z'",
                "end_captured_at='2021-01-01T16:14:20Z')",
            ),
            (
                "https://graph.mapillary.com/images?bbox=62.22656249999999,48.1640625,"
                "38.41055825094609,45.336701909968134&start_captured_at=2020-01-01T16:14:20Z&end_captured_at="
                "2021-01-01T16:14:20Z"
            ),
        )
    ],
)
def test_search_for_images__time_param(operation, expected):

    # Operation to test
    test_that = f"{operation} == {expected}"

    # Logging the intended operation to be tested
    logger.info(f"[search_for_images] Test that {test_that}")

    # Actual data on left, operation on right
    actual: str = Entities.search_for_images(
        bbox=[62.22656249999999, 48.1640625, 38.41055825094609, 45.336701909968134],
        start_captured_at="2020-01-01T16:14:20Z",
        end_captured_at="2021-01-01T16:14:20Z",
    )

    logger.info(f"[search_for_images] Actual: {actual}, Expected: {expected}")
    # What was expected left, what was actual on the right
    assert actual == expected, f"'{test_that}' failed, got {actual}"


@pytest.mark.parametrize(
    "operation, expected",
    [
        (
            (
                "mly.config.api.entities.search_for_images(bbox=[62.22656249999999, 48.1640625,"
                "38.41055825094609, 45.336701909968134],start_captured_at=datetime.datetime"
                "(2020, 1, 1, 16, 14, 20),end_captured_at=datetime.datetime(2021, 1, 1, 16, 14,"
                "20))"
            ),
            (
                "https://graph.mapillary.com/images?bbox=62.22656249999999,48.1640625,"
                "38.41055825094609,45.336701909968134&start_captured_at=2020-01-01T16:14:20Z&"
                "end_captured_at=2021-01-01T16:14:20Z"
            ),
        )
    ],
)
def test_search_for_images__time_param_datetime_object(operation, expected):

    # Operation to test
    test_that = f"{operation} == {expected}"

    # Logging the intended operation to be tested
    logger.info(f"[search_for_images] Test that {test_that}")

    # Actual data on left, operation on right
    actual: str = Entities.search_for_images(
        bbox=[62.22656249999999, 48.1640625, 38.41055825094609, 45.336701909968134],
        start_captured_at=datetime.datetime(2020, 1, 1, 16, 14, 20),
        end_captured_at=datetime.datetime(2021, 1, 1, 16, 14, 20),
    )

    logger.info(f"[search_for_images] Actual: {actual}, Expected: {expected}")
    # What was expected left, what was actual on the right
    assert actual == expected, f"'{test_that}' failed, got {actual}"


@pytest.mark.parametrize(
    "operation, expected",
    [
        (
            (
                "mly.config.api.entities.search_for_images(bbox=[62.22656249999999, 48.1640625,"
                "38.41055825094609, 45.336701909968134], start_captured_at='2020-01-01'",
                "end_captured_at='2021-01-01T16:14:20Z')",
            ),
            ("ValueError: start_captured_at must be in ISO 8601 format"),
        )
    ],
)
def test_search_for_images__use_strict_invalid_start_time_param(operation, expected):

    # Operation to test
    test_that = f"{operation} == {expected}"

    # Logging the intended operation to be tested
    logger.info(f"[search_for_images] Test that {test_that}")

    # Setting strict to True
    Config.use_strict = True

    has_exception_occurred: bool = False

    # Actual data on left, operation on right
    try:
        actual: str = Entities.search_for_images(
            bbox=[62.22656249999999, 48.1640625, 38.41055825094609, 45.336701909968134],
            start_captured_at="2020-01-01",
            end_captured_at="2021-01-01T16:14:20Z",
        )
    except ValueError:
        has_exception_occurred = True

    # What was expected left, what was actual on the right
    assert has_exception_occurred, f"'{test_that}' failed, got {actual}"


@pytest.mark.parametrize(
    "operation, expected",
    [
        (
            (
                "mly.config.api.entities.search_for_images(bbox=[62.22656249999999, 48.1640625,"
                "38.41055825094609, 45.336701909968134], start_captured_at='2020-01-01',"
                "end_captured_at='2021-01-01T16:14:20Z')"
            ),
            (
                "https://graph.mapillary.com/images?bbox=62.22656249999999,48.1640625,"
                "38.41055825094609,45.336701909968134&end_captured_at=2021-01-01T16:14:20Z"
            ),
        )
    ],
)
def test_search_for_images__without_use_strict_invalid_start_time_param(
    operation, expected
):

    # Operation to test
    test_that = f"{operation} == {expected}"

    # Logging the intended operation to be tested
    logger.info(f"[search_for_images] Test that {test_that}")

    # Setting strict to False
    Config.use_strict = False

    # Actual data on left, operation on right
    actual: str = Entities.search_for_images(
        bbox=[62.22656249999999, 48.1640625, 38.41055825094609, 45.336701909968134],
        start_captured_at="2020-01-01",
        end_captured_at="2021-01-01T16:14:20Z",
    )

    logger.info(f"[search_for_images] Actual: {actual}, Expected: {expected}")
    # What was expected left, what was actual on the right
    assert actual == expected, f"'{test_that}' failed, got {actual}"


@pytest.mark.parametrize(
    "operation, expected",
    [
        (
            (
                "mly.config.api.entities.search_for_images(bbox=[62.22656249999999, 48.1640625,"
                "38.41055825094609, 45.336701909968134], limit=100)"
            ),
            (
                "https://graph.mapillary.com/images?bbox=62.22656249999999,48.1640625,"
                "38.41055825094609,45.336701909968134&limit=100"
            ),
        )
    ],
)
def test_search_for_images__limit_param(operation, expected):

    # Operation to test
    test_that = f"{operation} == {expected}"

    # Logging the intended operation to be tested
    logger.info(f"[search_for_images] Test that {test_that}")

    # Actual data on left, operation on right
    actual: str = Entities.search_for_images(
        bbox=[62.22656249999999, 48.1640625, 38.41055825094609, 45.336701909968134],
        limit=100,
    )

    logger.info(f"[search_for_images] Actual: {actual}, Expected: {expected}")
    # What was expected left, what was actual on the right
    assert actual == expected, f"'{test_that}' failed, got {actual}"


@pytest.mark.parametrize(
    "operation, expected",
    [
        (
            (
                "mly.config.api.entities.search_for_images(bbox=[62.22656249999999, 48.1640625,"
                "38.41055825094609, 45.336701909968134], limit=2001)"
            ),
            (
                "https://graph.mapillary.com/images?bbox=62.22656249999999,48.1640625,"
                "38.41055825094609,45.336701909968134&limit=2000"
            ),
        )
    ],
)
def test_search_for_images__exceeding_limit_param(operation, expected):

    # Operation to test
    test_that = f"{operation} == {expected}"

    # Logging the intended operation to be tested
    logger.info(f"[search_for_images] Test that {test_that}")

    # Actual data on left, operation on right
    actual: str = Entities.search_for_images(
        bbox=[62.22656249999999, 48.1640625, 38.41055825094609, 45.336701909968134],
        limit=2001,
    )

    logger.info(f"[search_for_images] Actual: {actual}, Expected: {expected}")
    # What was expected left, what was actual on the right
    assert actual == expected, f"'{test_that}' failed, got {actual}"


@pytest.mark.parametrize(
    "operation, expected",
    [
        (
            (
                "mly.config.api.entities.search_for_images(bbox=[62.22656249999999, 48.1640625,"
                "38.41055825094609, 45.336701909968134], organization_id=0123456789)"
            ),
            (
                "https://graph.mapillary.com/images?bbox=62.22656249999999,48.1640625,"
                "38.41055825094609,45.336701909968134&organization_id=1234567890"
            ),
        )
    ],
)
def test_search_for_images__organization_id_param(operation, expected):

    # Operation to test
    test_that = f"{operation} == {expected}"

    # Logging the intended operation to be tested
    logger.info(f"[search_for_images] Test that {test_that}")

    # Actual data on left, operation on right
    actual: str = Entities.search_for_images(
        bbox=[62.22656249999999, 48.1640625, 38.41055825094609, 45.336701909968134],
        organization_id=1234567890,
    )

    logger.info(f"[search_for_images] Actual: {actual}, Expected: {expected}")
    # What was expected left, what was actual on the right
    assert actual == expected, f"'{test_that}' failed, got {actual}"


@pytest.mark.parametrize(
    "operation, expected",
    [
        (
            (
                "mly.config.api.entities.search_for_images(bbox=[62.22656249999999, 48.1640625,"
                "38.41055825094609, 45.336701909968134], organization_id=0123456789)"
            ),
            (
                "https://graph.mapillary.com/images?bbox=62.22656249999999,48.1640625,"
                "38.41055825094609,45.336701909968134&organization_id=1234567890"
            ),
        )
    ],
)
def test_search_for_images__organization_id_param__as_str(operation, expected):

    # Operation to test
    test_that = f"{operation} == {expected}"

    # Logging the intended operation to be tested
    logger.info(f"[search_for_images] Test that {test_that}")

    # Actual data on left, operation on right
    actual: str = Entities.search_for_images(
        bbox=[62.22656249999999, 48.1640625, 38.41055825094609, 45.336701909968134],
        organization_id="1234567890",
    )

    logger.info(f"[search_for_images] Actual: {actual}, Expected: {expected}")
    # What was expected left, what was actual on the right
    assert actual == expected, f"'{test_that}' failed, got {actual}"


@pytest.mark.parametrize(
    "operation, expected",
    [
        (
            (
                "mly.config.api.entities.search_for_images(bbox=[62.22656249999999, 48.1640625,"
                "38.41055825094609, 45.336701909968134], sequence_id=[1234567890, 9876543210,"
                "1234567890, 9876543210])"
            ),
            (
                "https://graph.mapillary.com/images?bbox=62.22656249999999,48.1640625,"
                "38.41055825094609,45.336701909968134&sequence_id=1234567890,9876543210,"
                "1234567890,9876543210"
            ),
        )
    ],
)
def test_search_for_images__sequence_ids_param(operation, expected):

    # Operation to test
    test_that = f"{operation} == {expected}"

    # Logging the intended operation to be tested
    logger.info(f"[search_for_images] Test that {test_that}")

    # Actual data on left, operation on right
    actual: str = Entities.search_for_images(
        bbox=[62.22656249999999, 48.1640625, 38.41055825094609, 45.336701909968134],
        sequence_id=[1234567890, 9876543210, 1234567890, 9876543210],
    )

    logger.info(f"[search_for_images] Actual: {actual}, Expected: {expected}")
    # What was expected left, what was actual on the right
    assert actual == expected, f"'{test_that}' failed, got {actual}"


@pytest.mark.parametrize(
    "operation, expected",
    [
        (
            (
                "mly.config.api.entities.search_for_images(bbox=[62.22656249999999, 48.1640625,"
                "38.41055825094609, 45.336701909968134], fields=['altitude', 'atomic_scale',"
                "'camera_parameters'])"
            ),
            (
                "https://graph.mapillary.com/images?bbox=62.22656249999999,48.1640625,"
                "38.41055825094609,45.336701909968134&fields=altitude,atomic_scale,"
                "camera_parameters,geometry"
            ),
        )
    ],
)
def test_search_for_images__fields_param__selected(operation, expected):

    # Operation to test
    test_that = f"{operation} == {expected}"

    # Logging the intended operation to be tested
    logger.info(f"[search_for_images] Test that {test_that}")

    # Actual data on left, operation on right
    actual: str = Entities.search_for_images(
        bbox=[62.22656249999999, 48.1640625, 38.41055825094609, 45.336701909968134],
        fields=["altitude", "atomic_scale", "camera_parameters"],
    )

    logger.info(f"[search_for_images] Actual: {actual}, Expected: {expected}")
    # What was expected left, what was actual on the right
    assert actual == expected, f"'{test_that}' failed, got {actual}"


@pytest.mark.parametrize(
    "operation, expected",
    [
        (
            (
                "mly.config.api.entities.search_for_images(bbox=[62.22656249999999, 48.1640625,"
                "38.41055825094609, 45.336701909968134], fields=['all'])"
            ),
            (
                "https://graph.mapillary.com/images?bbox=62.22656249999999,48.1640625,"
                "38.41055825094609,45.336701909968134&fields=altitude,atomic_scale,"
                "camera_parameters,camera_type,captured_at,compass_angle,computed_altitude,"
                "computed_compass_angle,computed_geometry,computed_rotation,creator,exif_orientation,"
                "geometry,height,make,model,thumb_256_url,thumb_1024_url,thumb_2048_url,thumb_original_url,merge_cc,mesh,"
                "quality_score,sequence,sfm,width"
            ),
        )
    ],
)
def test_search_for_images__fields_param__all(operation, expected):

    # Operation to test
    test_that = f"{operation} == {expected}"

    # Logging the intended operation to be tested
    logger.info(f"[search_for_images] Test that {test_that}")

    # Actual data on left, operation on right
    actual: str = Entities.search_for_images(
        bbox=[62.22656249999999, 48.1640625, 38.41055825094609, 45.336701909968134],
        fields=["all"],
    )

    logger.info(f"[search_for_images] Actual: {actual}, Expected: {expected}")
    # What was expected left, what was actual on the right
    assert actual == expected, f"'{test_that}' failed, got {actual}"


@pytest.mark.parametrize(
    "operation, expected",
    [
        (
            (
                "mly.config.api.entities.search_for_images(bbox=[62.22656249999999, 48.1640625,"
                "38.41055825094609, 45.336701909968134], fields=['xxxx', 'yyyyyyyyyy'])"
            ),
            (
                "InvalidFieldError: The invalid field, 'xxxx', was passed to the endpoint"
                "'https://graph.mapillary.com/images?bbox=,:parameters=,:fields='"
            ),
        )
    ],
)
def test_search_for_images__fields_param__all(operation, expected):

    # Operation to test
    test_that = f"{operation} == {expected}"

    # Logging the intended operation to be tested
    logger.info(f"[search_for_images] Test that {test_that}")

    has_exception_occurred: bool = False

    # Actual data on left, operation on right
    try:
        actual: str = Entities.search_for_images(
            bbox=[62.22656249999999, 48.1640625, 38.41055825094609, 45.336701909968134],
            fields=["xxxx", "yyyyyyyyyy"],
        )
    except InvalidFieldError:
        has_exception_occurred = True

    # What was expected left, what was actual on the right
    assert has_exception_occurred, f"'{test_that}' failed, got {actual}"
