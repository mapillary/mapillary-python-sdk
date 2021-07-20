# -*- coding: utf-8 -*-

"""
mapillary.controllers.save
~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the saving business logic functionalities of the Mapillary Python SDK.

For more information, please check out https://www.mapillary.com/developer/api-documentation/

:copyright: (c) 2021 Facebook
:license: MIT LICENSE
"""


def save_as_csv_controller(data: dict, path: str) -> bool:
    """Save data as CSV to given file path

    :param data: The data to save as CSV
    :type data: dict

    :param path: The path to save to
    :type path: str

    :return: Confirmation of whether the object was saved properly
    :rtype: bool
    """

    # TODO: Requirement# 12A

    return {"Message": "Hello, World!"}


def save_as_geojson_controller(data: str, path: str) -> bool:
    """Save data as GeoJSON to given file path

    :param data: The data to save as GeoJSON
    :type data: dict

    :param path: The path to save to
    :type path: str

    :return: Confirmation of whether the object was saved properly
    :rtype: bool
    """

    # TODO: Requirement# 12B

    return {"Message": "Hello, World!"}
