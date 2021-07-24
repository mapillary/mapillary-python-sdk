# Copyright (c) Facebook, Inc. and its affiliates. (http://www.facebook.com)
# -*- coding: utf-8 -*-

"""
mapillary.utils.extract
~~~~~~~~~~~~~~~~~~~~~~~

This module deals with extracting multiple fields nested within a GeoJSON packet.

:copyright: (c) 2021 Facebook
:license: MIT LICENSE
"""


def extract_properties(geojson: dict, properties: list) -> dict:
    """Extracts specific properties from a complete GeoJSON

    :param geojson: GeoJSON object
    :type geojson: dict

    :param properties: A list of properties to extract
    :type properties: list

    :return: The extracted fields as a dict
    :rtype: dict

    Usage::
        >>> from utils.extract import extract_properties
        >>> extract_properties(data, ['id']) # id most likely exists

    Import::
        >>> cd ${MAPILLARY_PROJECT_ROOT}
        >>> from tests.utils.test_extract import test_extract_properties
        >>> test_extract_properties(['id'])
        {"Test": "Success"}

    Test::
        >>> pytest -m tests/
    """

    extracted_fields = {}

    for property in properties:
        extracted_fields[property] = []

    for feature in geojson["features"]:
        for property in properties:
            if property in feature["properties"]:
                extracted_fields[property].append(feature["properties"][property])

    return extracted_fields
