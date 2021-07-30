# Copyright (c) Facebook, Inc. and its affiliates. (http://www.facebook.com)
# -*- coding: utf-8 -*-

"""
mapillary.controller.rules.verify
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the verification of the filters passed to each of the controllers
under `./controllers` that implemeent the business logic functionalities of the Mapillary
Python SDK.

For more information, please check out https://www.mapillary.com/developer/api-documentation/

:copyright: (c) 2021 Facebook
:license: MIT LICENSE
"""

from models.exceptions import InvalidKwargError, InvalidOptionError


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
            "min_date",
            "max_date",
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
            "max_date",
            "min_date",
            "image_type",
            "compass_angle",
            "organization_id",
            "sequence_id",
            "zoom",
        ],
        callback="image_bbox_check",
    ):
        return {
            "max_date": kwargs.get("max_date", None),
            "min_date": kwargs.get("min_date", None),
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
            "max_date",
            "min_date",
            "image_type",
            "organization_id",
            "zoom",
        ],
        callback="sequence_bbox_check",
    ):
        return {
            "max_date": kwargs.get("max_date", None),
            "min_date": kwargs.get("min_date", None),
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
