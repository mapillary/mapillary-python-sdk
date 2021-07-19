# -*- coding: utf-8 -*-

"""
mapillary.utils.filter
This module contains the filter utilies for high level filtering logic
"""

# Local imports
from utils.time import date_to_unix_timestamp
from utils.format import feature_list_to_geojson

# Package imports
import haversine
import logging

logger = logging.getLogger("pipeline-logger")


def pipeline_component(func, data, exception_message, args):
    """A pipeline component which is respnonsible for sending functional arguments over
    to the selected target function - throwing a warning in case of an exception

    Usage::
        >>> # internally used in mapillary.utils.pipeline
    """

    try:
        return func(data, *args)
    except TypeError as exception:
        logger.warning(f"{exception_message}, {exception}")


def pipeline(data: list, components: list):
    """A pipeline component that helps with making filtering easier. It provides
    access to different filtering mechanism by simplying letting users
    pass in what filter they want to apply, and the arguments for that filter

    Usage::
        >>> # assume variables 'data', 'kwargs'
        >>> pipeline(
            data=data,
            components=[
                {"filter": "image_type", "tile": kwargs["image_type"]}
                if "image_type" in kwargs
                else {},
                {"filter": "organization_id", "organization_ids": kwargs["org_id"]}
                if "org_id" in kwargs
                else {},
                {
                    "filter": "haversine_dist",
                    "radius": kwargs["radius"],
                    "coords": [longitude, latitude],
                }
                if "radius" in kwargs
                else 1000,
            ],
        )

    Import::
        >>> cd ${MAPILLARY_PROJECT_ROOT}
        >>> from tests.utils.test_filter import test_pipeline
        >>> test_pipeline(zoom=14, longitude=31, latitude=30)
        53
        0
        676

    Test::
        >>> pytest -m tests/
    """

    # Python treats dict objects as passed reference, thus
    # in order to not modify the previous state, we make a local copy
    __data = data.copy()

    # A mapping of different filters possible
    function_mappings = {
        "filter_values": filter_values,
        "max_date": max_date,
        "min_date": min_date,
        "haversine_dist": haversine_dist,
        "image_type": image_type,
        "organization_id": organization_id,
        "features_in_bounding_box": features_in_bounding_box,
        "existed_after": existed_after,
        "existed_before": existed_before,
        # Simply add the mapping of a new function,
        # nothing else will really need to changed
    }

    # Going through each of the components
    for component in components:

        # If component is simply empty, continue to next
        # iteration
        if component == {}:
            continue

        # Send to pipeline component, return data to `__data`
        __data = pipeline_component(
            # Map function respectively using the function_mappings dictionary
            func=function_mappings[f'{component["filter"]}'],
            # Send over the data
            data=__data,
            # Specify the message on the exception thrown
            exception_message=f'[pipeline - {component["filter"]}] Filter not applied, exception thrown',
            # Except the filter name, select the rest as args
            args=tuple(list(component.values())[1:]),
        )

    # Return the data
    return __data


def max_date(data, max_timestamp):
    """Selects only the feature items that are less
    than the max_timestamp

    Usage::
        >>> max_date({'type': 'FeatureCollection', 'features': [{'type': 'Feature', 'geometry':
        {'type': 'Point', 'coordinates': [30.98594605922699, 30.003757307208872]}, 'properties':
        { ... }, ...}]}, '2020-05-23')
    """

    return {
        "features": [
            feature
            for feature in data["features"]
            if feature["properties"]["captured_at"]
            <= date_to_unix_timestamp(max_timestamp)
        ]
    }


def min_date(data, min_timestamp):
    """Selects only the feature items that are less
    than the min_timestamp

    Usage::
        >>> max_date({'type': 'FeatureCollection', 'features': [{'type': 'Feature', 'geometry':
        {'type': 'Point', 'coordinates': [30.98594605922699, 30.003757307208872]}, 'properties':
        { ... }, ...}]}, '2020-05-23')
    """

    return {
        "features": [
            feature
            for feature in data["features"]
            if feature["properties"]["captured_at"]
            >= date_to_unix_timestamp(min_timestamp)
        ]
    }


def features_in_bounding_box(data: dict, bbox: dict) -> list:
    """Filter for extracting features only in a bounding box

    :param data: the features list to be checked
    :type data: list

    :param bbox: Bounding box coordinates
    example: {
        'east': 'BOUNDARY_FROM_EAST',
        'south': 'BOUNDARY_FROM_SOUTH',
        'west': 'BOUNDARY_FROM_WEST',
        'north': 'BOUNDARY_FROM_NORTH'
    }
    :type bbox: <class 'dict'>

    :return: Features that only exist within the bounding box selected for the given features list
    provided in the BBox functon
    :rtype: list
    """

    # define an empty geojson as output
    output = []

    # For each feature in the filtered_data
    for feature in data:

        # If feature exists in bounding box
        if (
            feature["geometry"]["coordinates"][0] < bbox["east"]
            and feature["geometry"]["coordinates"][0] > bbox["west"]
        ) and (
            feature["geometry"]["coordinates"][1] > bbox["south"]
            and feature["geometry"]["coordinates"][1] < bbox["north"]
        ):

            # Append feature to the output
            output.append(feature)

    return output


def filter_values(data: list, values: list, property: str = "value") -> list:
    """Filter the features based on the existence of a specified value
    in one of the property.

    ### TODO: Need documentation that lists the 'values', specifically, it refers to 'value'
    ### TODO: under 'Detection', and 'Map feature'

    :param data: The data to be filtered
    :type data: dict

    :param values: A list of values to filter by
    :type values: list

    :param property: The specific parameter to look into
    :type property: str

    :return: A feature list
    :rtype: dict
    """

    return [feature for feature in data if feature["properties"][property] in values]


def existed_after(data: list, existed_after: str) -> list:
    return [
        feature
        for feature in data
        if feature["properties"]["first_seen_at"] > date_to_unix_timestamp(existed_after)
    ]


def existed_before(data: list, existed_before: str) -> list:
    print(date_to_unix_timestamp(existed_before))
    return [
        feature
        for feature in data
        if feature["properties"]["first_seen_at"] <= date_to_unix_timestamp(existed_before)
    ]


def haversine_dist(data: dict, radius: float, coords: list, unit: str = "m") -> dict:
    """Returns features that are only in the radius specified
    using the Haversine distance, from the haversince package

    :param data: The data to be filtered
    :type data: dict

    :param radius: Radius for coordinates to fall into
    :type radius: float

    :param coords: The input coordinates (long, lat)
    :type coords: list

    :param unit: Either 'ft', 'km', 'm', 'mi', 'nmi', see here https://pypi.org/project/haversine/
    :type unit: str

    :return: A feature list
    :rtype: dict
    """

    # Define an empty geojson
    output = {"type": "FeatureCollection", "features": []}

    # Go through the features
    for feature in data["features"]:

        # If the calculated haversince distance is less than the radius ...
        if (
            haversine.haversine(coords, feature["geometry"]["coordinates"], unit=unit)
            < radius
        ):

            # ... append to the output
            output["features"].append(feature)

    # Return the output
    return output


def image_type(data: dict, type: str) -> dict:
    """The parameter might be 'all' (both is_pano == true and false), 'pano'
    (is_pano == true only), or 'flat' (is_pano == false only)

    :param data: The data to be filtered
    :type data: dict

    :param type: Either 'pano' (True), 'flat' (False), or 'all' (None)
    :type type: str

    :return: A feature list
    :rtype: dict
    """

    # Checking what kind of parameter is passed
    bool_for_pano_filtering = (
        # Return true if type == 'pano'
        True
        if type == "pano"
        # Else false if type == 'falt'
        else False
        if type == "float"
        # Else None if type is implicity 'all'
        else None
    )

    # Since 'all' doesn't change anything, we checking if
    # variable is not None
    if bool_for_pano_filtering:

        # Return the select features
        return {
            "features": [
                # Feature only if
                feature
                # through the feature in the data
                for feature in data["features"]
                # Select only properties that are appropriate (True/False)
                if feature["properties"]["is_pano"] is bool_for_pano_filtering
            ]
        }


def organization_id(data: dict, organization_ids: list) -> dict:
    """Select only features that contain the specific organization_id

    :param data: The data to be filtered
    :type data: dict

    :param organization_ids: The oragnization id(s) to filter through
    :type organization_ids: list

    :return: A feature list
    :rtype: dict
    """

    return {
        "features": [
            # Feature only if
            feature
            # through the feature in the data
            for feature in data["features"]
            # if the found org_id is in the list of organization_ids
            if feature["properties"]["organization_id"] in organization_ids
        ]
    }
