# Copyright (c) Facebook, Inc. and its affiliates. (http://www.facebook.com)
# -*- coding: utf-8 -*-

"""
tests.utils.test_extract
~~~~~~~~~~~~~~~~~~~~~~~~

For testing the functions under mapillary/utils/extract.py

:copyright: (c) 2021 Facebook
:license: MIT LICENSE
"""

# Package imports
import pytest
import logging  # Logger

# Local imports
from mapillary.utils.extract import extract_properties  # Function to test
from tests.conftest import data  # Data as fixture

logger = logging.getLogger(__name__)


@pytest.mark.parametrize(
    "operation, expected", [("extract_properties(data['data'], ['id'])", 0)]
)
def test_extract_properties(data: dict, operation, expected):

    # Operation to test
    test_that = f"{operation} != {expected}"

    # Logging the intended operation to be tested
    logger.info(f"\n[test_extract_properties] Test that {test_that}")

    # Actual data on left, operation on right
    actual = extract_properties(data["data"], ["id"])

    # What was expected left, what was actual on the right
    assert len(actual["id"]) != [], f"{test_that} failed, got {actual}"
