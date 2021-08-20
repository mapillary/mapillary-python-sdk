# Copyright (c) Facebook, Inc. and its affiliates. (http://www.facebook.com)
# -*- coding: utf-8 -*-

"""
mapillary.controller.rules.verify
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the verification of the filters or keys passed to each of the controllers
under `./controllers` that implemeent the business logic functionalities of the Mapillary
Python SDK.

For more information, please check out https://www.mapillary.com/developer/api-documentation/

:copyright: (c) 2021 Facebook
:license: MIT LICENSE
"""
# Local Imports
from mapillary.models.exceptions import InvalidKwargError, InvalidOptionError
from mapillary.config.api.entities import Entities
from mapillary.models.client import Client

# Package Imports
import requests
import re


def kwarg_check(kwargs: dict, options: list, callback: str) -> bool:
    """Checks for keyword arguments amongst the kwarg argument to fall into the options list

    :param kwargs: A dictionary that contains the keyword key-value pair arguments
    :type kwargs: dict

    :param options: A list of possible arguments in kwargs
    :type options: list

    :param callback: The function that called 'kwarg_check' in the case of an exception
    :type callback: str

    '''
    :raise InvalidOptionError: Invalid option exception
    '''

    :return: A boolean, whether the kwargs are appropriate or not
    :rtype: bool
    """
    if kwargs is not None:
        for key in kwargs.keys():
            if key not in options:
                raise InvalidKwargError(
                    func=callback,
                    key=key,
                    value=kwargs[key],
                    options=options,
                )

    # If 'zoom' is in kwargs
    if ("zoom" in kwargs) and (kwargs["zoom"] < 14 or kwargs["zoom"] > 17):

        # Raising exception for invalid zoom value
        raise InvalidOptionError(
            param="zoom", value=kwargs["zoom"], options=[14, 15, 16, 17]
        )

    # if 'image_type' is in kwargs
    if ("image_type" in kwargs) and (
        kwargs["image_type"] not in ["pano", "flat", "all"]
    ):

        # Raising exception for invalid image_type value
        raise InvalidOptionError(
            param="image_type",
            value=kwargs["image_type"],
            options=["pano", "flat", "all"],
        )

    # If all tests pass, return True
    return True


def image_check(kwargs) -> bool:
    """For image entities, check if the arguments provided fall in the right category

    :param kwargs: A dictionary that contains the keyword key-value pair arguments
    :type kwargs: dict
    """

    # Kwarg argument check
    return kwarg_check(
        kwargs=kwargs,
        options=[
            "min_captured_at",
            "max_captured_at",
            "radius",
            "image_type",
            "organization_id",
            "fields",
        ],
        callback="image_check",
    )


def resolution_check(resolution: int) -> bool:
    """Checking for the proper thumbnail size of the argument

    :param resolution: The image size to fetch for
    :type resolution: int

    '''
    :raises InvalidOptionError: Invalid thumbnail size passed raises exception
    '''

    :return: A check if the size is correct
    :rtype: bool
    """

    if resolution not in [256, 1024, 2048]:
        # Raising exception for resolution value
        raise InvalidOptionError(
            param="resolution", value=resolution, options=[256, 1024, 2048]
        )


def image_bbox_check(kwargs: dict) -> dict:
    """Check if the right arguments have been provided for the image bounding box

    :param kwargs: The dictionary parameters
    :type kwargs: dict

    :return: A final dictionary with the kwargs
    :rtype: dict
    """

    if kwarg_check(
        kwargs=kwargs,
        options=[
            "max_captured_at",
            "min_captured_at",
            "image_type",
            "compass_angle",
            "organization_id",
            "sequence_id",
            "zoom",
        ],
        callback="image_bbox_check",
    ):
        return {
            "max_captured_at": kwargs.get("max_captured_at", None),
            "min_captured_at": kwargs.get("min_captured_at", None),
            "image_type": kwargs.get("image_type", None),
            "compass_angle": kwargs.get("compass_angle", None),
            "sequence_id": kwargs.get("sequence_id", None),
            "organization_id": kwargs.get("organization_id", None),
        }


def sequence_bbox_check(kwargs: dict) -> dict:
    """Checking of the sequence bounding box

    :param kwargs: The final dictionary with the correct keys
    :type kwargs: dict

    :return: A dictionary with all the options available specifically
    :rtype: dict
    """

    if kwarg_check(
        kwargs=kwargs,
        options=[
            "max_captured_at",
            "min_captured_at",
            "image_type",
            "organization_id",
            "zoom",
        ],
        callback="sequence_bbox_check",
    ):
        return {
            "max_captured_at": kwargs.get("max_captured_at", None),
            "min_captured_at": kwargs.get("min_captured_at", None),
            "image_type": kwargs.get("image_type", None),
            "organization_id": kwargs.get("organization_id", None),
        }


def points_traffic_signs_check(kwargs: dict) -> dict:
    """Checks for traffic sign arguments

    :param kwargs: The parameters to be passed for filtering
    :type kwargs: dict

    :return: A dictionary with all the options available specifically
    :rtype: dict
    """

    if kwarg_check(
        kwargs=kwargs,
        options=["existed_at", "existed_before"],
        callback="points_traffic_signs_check",
    ):
        return {
            "existed_at": kwargs.get("existed_at", None),
            "existed_before": kwargs.get("existed_before", None),
        }


def valid_id(id: int, image=True):
    """Checks if a given id is valid as it is assumed. For example, is a given id expectedly an
    image_id or not? Is the id expectedly a map_feature_id or not?

    :param id: The ID passed
    :type id: int

    :param image: Is the passed id an image_id?
    :type image: bool

    '''
    :raises InvalidOptionError: Raised when invalid arguments are passed
    '''

    :return: None
    :rtype: None
    """

    # IF image == False, and error_check == True, this becomes True
    # IF image == True, and error_check == False, this becomes True
    if image ^ is_image_id(id=id, fields=[]):

        # The EntityAdapter() sends a request to the server, checking
        # if the id is indeed an image_id, TRUE is so, else FALSE

        # Raises an exception of InvalidOptionError
        raise InvalidOptionError(
            param="id",
            value=f"ID: {id}, image: {image}",
            options=[
                "ID is image_id AND image is True",
                "ID is map_feature_id AND image is False",
            ],
        )


def is_image_id(id: int, fields: list = []) -> bool:
    """Checks if the id is an image_id

    :param id: The id to be checked
    :type id: int

    :param fields: The fields to be checked
    :type fields: list

    :return: True if the id is an image_id, else False
    """
    try:
        res = requests.get(
            Entities.get_image(
                image_id=id,
                fields=fields if fields != [] else Entities.get_image_fields(),
            ),
            headers={"Authorization": f"OAuth {Client.get_token()}"},
        )
        return res.status_code == 200

    except requests.HTTPError:
        return False


def check_file_name_validity(file_name: str) -> bool:
    """Checks if the file name is valid.
    Valid file names are:
        - without extensions
        - without special characters
        - A-Z, a-z, 0-9, _, -

    :param file_name: The file name to be checked
    :type file_name: str

    :return: True if the file name is valid, else False
    """
    string_check = re.compile("[@.!#$%^&*()<>?/\|}{~:]")  # noqa: W605
    if (
        # File name characters are not all ASCII
        not all(ord(c) < 128 for c in file_name)
        # File name characters contain special characters or extensions
        or string_check.search(file_name)
    ):
        print(
            f"File name: {file_name} is not valid. Please use only letters, numbers, dashes,"
            f" and underscores. \nDefaulting to: mapillary_CURRENT_UNIX_TIMESTAMP_"
        )
        return False
    return True
