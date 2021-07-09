# -*- coding: utf-8 -*-

"""
mapillary.utils.filter
This module contains the filter utilies high level filtering logic
"""

# Local imports
from utils.time import date_to_unix_epoch
from utils.format import feature_list_to_geojson

# Package imports
from haversine import haversine
import logging


def pipeline(data, components: list):

    # ? This function could use refactoring, but how?

    temp_data = data.copy()

    logger = logging.getLogger("pipeline-logger")

    for component in components:

        if component == {}:
            continue

        if component["filter"] == "params":
            try:
                temp_data = params(
                    data=temp_data,
                    values=component["values"],
                    properties=component["properties"],
                )
            except TypeError as exception:
                logger.warning(
                    f"[pipeline - params] Filter not applied, exception thrown, {exception}"
                )

        if component["filter"] == "min_date":
            try:
                temp_data = min_date(
                    data=temp_data, min_timestamp=component["max_timestamp"]
                )
            except TypeError as exception:
                logger.warning(
                    f"[pipeline - min_date] Filter not applied, exception thrown, {exception}"
                )

        if component["filter"] == "max_date":
            try:
                temp_data = max_date(
                    data=temp_data, max_timestamp=component["max_timestamp"]
                )
            except TypeError as exception:
                logger.warning(
                    f"[pipeline - max_date] Filter not applied, exception thrown, {exception}"
                )

        if component["filter"] == "daterange":
            try:
                temp_data = max_date(
                    min_date(data=temp_data, min_timestamp=component["range"][0]),
                    max_timestamp=component["range"][1],
                )
            except TypeError as exception:
                logger.warning(
                    f"[pipeline - daterange] Filter not applied, exception thrown, {exception}"
                )

        if component["filter"] == "haversine_dist":
            try:
                temp_data = haversine_dist(
                    data=temp_data,
                    radius=component["radius"],
                    coords=component["coords"],
                    unit=component["unit"] if "unit" in component else "m",
                )
            except TypeError as exception:
                logger.warning(
                    f"[pipeline - haversine_dist, TypeError] Filter not applied, exception thrown,"
                    f" {exception}"
                )

        if component["filter"] == "coverage":
            try:
                temp_data = coverage(
                    data=temp_data,
                    tile=component["tile"],
                )
            except TypeError as exception:
                logger.warning(
                    f"[pipeline - coverage, TypeError] Filter not applied, exception thrown,"
                    f" {exception}"
                )

        if component["filter"] == "organization_id":
            try:
                temp_data = organization_id(
                    data=temp_data,
                    organization_ids=component["organization_ids"],
                )
            except TypeError as exception:
                logger.warning(
                    f"[pipeline - haversine_dist, TypeError] Filter not applied, exception thrown,"
                    f" {exception}"
                )

    if type(temp_data) in [list]:
        temp_data = feature_list_to_geojson(temp_data)

    return temp_data


def max_date(data, max_timestamp):
    max_timestamp = date_to_unix_epoch(max_timestamp)
    return [
        feature
        for feature in data["features"]
        if feature["properties"]["captured_at"] <= max_timestamp
    ]


def min_date(data, min_timestamp):
    min_timestamp = date_to_unix_epoch(min_timestamp)
    return [
        feature
        for feature in data["features"]
        if feature["properties"]["captured_at"] >= min_timestamp
    ]


def params(data, values, properties):
    return [
        feature
        for feature in data["features"]
        if feature["properties"][properties] in values
    ]


def haversine_dist(data, radius, coords, unit="m"):

    # Define an empty geojson
    output = {"type": "FeatureCollection", "features": []}

    for feature in data["features"]:
        distance = haversine(coords, feature["geometry"]["coordinates"], unit=unit)

        print(distance)
        if distance < radius:
            output["features"].append(feature)

    return output


def coverage(data, tile):
    """The parameter might be 'all' (both is_pano == true and false), 'pano'
    (is_pano == true only), or 'flat' (is_pano == false only)"""

    bool_for_pano_filtering = (
        True if tile == "pano" else False if tile == "flat" else None
    )

    if bool_for_pano_filtering is not None:
        return [
            feature
            for feature in data["features"]
            if feature["properties"]["is_pano"] is bool_for_pano_filtering
        ]


def organization_id(data, organization_ids: list):
    return [
        feature
        for feature in data["features"]
        if feature["properties"]["organization_id"] in organization_ids
    ]