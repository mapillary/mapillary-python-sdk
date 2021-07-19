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

from models.exceptions import ContradictingError, InvalidKwargError, InvalidOptionError


def kwarg_check(kwargs: dict, options: list, callback: str) -> bool:
    if kwargs is not None:
        for key in kwargs.keys():
            if key not in options:
                raise InvalidKwargError(
                    func=callback,
                    key=key,
                    value=kwargs[key],
                    options=options,
                )

    # If 'min_date' or 'max_date' is in the keys
    if ("min_date" in kwargs or "max_date" in kwargs) and ("daterange" in kwargs):

        # Check if two contradicting keys have not been given
        raise ContradictingError(
            contradicts="daterange",
            contradicted="min_date/max_date",
            message="Using either or both of min_date and max_date, or use daterange, "
            "but not both at the same time",
        )

    # If 'zoom' is in kwargs
    if ("zoom" in kwargs) and (kwargs["zoom"] < 14 or kwargs["zoom"] > 17):

        # Raising exception for invalid zoom value
        raise InvalidOptionError(
            param="zoom", value=kwargs["zoom"], options=[14, 15, 16, 17]
        )

    # if 'image_type' is in kwargs
    if ('image_type' in kwargs) and (kwargs['image_type'] not in ['pano', 'flat', 'all']):

        # Raising exception for invalid image_type value
        raise InvalidOptionError(
            param='image_type',
            value=kwargs["image_type"],
            options=['pano', 'flat', 'all']
            )

    return True


def image_check(kwargs) -> bool:

    return kwarg_check(
        kwargs=kwargs,
        options=[
            "min_date",
            "max_date",
            "daterange",
            "radius",
            "image_type",
            "org_id",
            "fields",
        ],
        callback="image_check",
    )


def thumbnail_size_check(thumbnail_size: int) -> bool:
    if thumbnail_size in [256, 1024, 2048]:
        return True

    # Raising exception for thumbnail_size value
    raise InvalidOptionError(
        param="thumbnail_size", value=thumbnail_size, options=[256, 1024, 2048]
    )


def image_bbox_check(kwargs: dict) -> bool:

    return kwarg_check(kwargs=kwargs, options=[
                "max_date",
                "min_date",
                "image_type",
                "compass_angle",
                "org_id",
                "sequence_id",
                "zoom",
            ], callback='image_bbox_check')

def sequence_bbox_check(kwargs: dict) -> bool:

    return kwarg_check(kwargs=kwargs, options=[
                "max_date",
                "min_date",
                "image_type",
                "org_id",
                "zoom",
            ], callback='sequence_bbox_check')



def points_traffic_signs_check(kwargs: dict) -> dict:

    if kwarg_check(
        kwargs=kwargs,
        options=["existed_after", "existed_before"],
        callback="points_traffic_signs_check",
    ):
        return {
            "existed_after": kwargs.get("existed_after", None),
            "existed_before": kwargs.get("existed_before", None),
        }
