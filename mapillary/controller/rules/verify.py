"""
mapillary.controller.rules.verify
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the business logic
functionalities of the Mapillary Python SDK. For
more information, please check out
https://www.mapillary.com/developer/api-documentation/

:copyright: (c) 2021 ...
:license: See LICENSE for more details
"""

from models.exceptions import ContradictingError, InvalidKwargError, OutOfBoundZoomError


def kwarg_check_for_image_close_to(kwargs):
    if kwargs is not None:
        for key in kwargs.keys():
            if key not in [
                "min_date",
                "max_date",
                "daterange",
                "radius",
                "coverage",
                "org_id",
                "fields",
            ]:
                raise InvalidKwargError(
                    "get_image_close_to",
                    key,
                    kwargs[key],
                    [
                        "min_date",
                        "max_date",
                        "daterange",
                        "radius",
                        "coverage",
                        "org_id",
                        "fields",
                    ],
                )

    # Check if two contradicting keys have
    # not been given
    if ("min_date" in kwargs or "max_date" in kwargs) and ("daterange" in kwargs):
        raise ContradictingError(
            "daterange",
            "min_date/max_date",
            "Using either or both of min_date and max_date, or use daterange, "
            "but not both at the same time",
        )

    # Checking if an invalid zoom value has
    # not been given
    if ("zoom" in kwargs) and (kwargs["zoom"] < 14 or kwargs["zoom"] > 17):
        raise OutOfBoundZoomError(kwargs["zoom"], [14, 15, 16, 17])
