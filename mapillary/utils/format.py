# Copyright (c) Facebook, Inc. and its affiliates. (http://www.facebook.com)
# -*- coding: utf-8 -*-

"""
mapillary.utils.format
~~~~~~~~~~~~~~~~~~~~~~

This module deals with converting data to and from different file formats.

:copyright: (c) 2021 Facebook
:license: MIT LICENSE
"""

# Package imports
import json
from pprint import pprint


def feature_to_geojson(json_data: dict) -> dict:

    """From
    {'geometry': {'type': 'Point', 'coordinates': [30.003755665554, 30.985948744314]}, 'id':
    '506566177256016'}
    To get,
    {'type': 'FeatureCollection', 'features': [{'type': 'Feature', 'geometry': {'type': 'Point',
    'coordinates': [30.98594605922699, 30.003757307208872]}, 'properties': {}}]}
    """

    # The geometry property will always be present
    keys = [key for key in json_data.keys() if key != "geometry"]

    feature = {"type": "Feature", "geometry": {}, "properties": {}}
    # Make sure that all keys exist and retrieve their values if specified
    feature["geometry"] = json_data["geometry"]

    for key in keys:
        feature["properties"][key] = json_data[key]

    return feature


def join_geojson_with_keys(
    geojson_src: dict,
    geojson_src_key: str,
    geojson_dest: dict,
    geojson_dest_key: str,
) -> dict:

    """Combines features from two geojsons on the basis of same given key ids, similar to
    an SQL join functionality

    Usage::
        >>> join_geojson_with_keys(
            geojson_src=geojson_src,
            geojson_src_key='id',
            geojson_dest=geojson_dest,
            geojson_dest_key='id')
    """

    # Go through the feature set in the src geojson
    for from_features in geojson_src["features"]:

        # Go through the feature set in the dest geojson
        for into_features in geojson_dest["features"]:

            # If either of the geojson features do not contain
            # their respective assumed keys, continue
            if (
                geojson_dest_key not in into_features["properties"]
                or geojson_src_key not in from_features["properties"]
            ):
                continue

            # Checking if two IDs match up
            if int(from_features["properties"][geojson_src_key]) == int(
                into_features["properties"][geojson_dest_key]
            ):

                # Firstly, extract the properties that exist in the
                # src_geojson for that feature
                old_properties = [key for key in from_features["properties"].keys()]

                # Secondly, extract the properties that exist in the
                # dest_json for that feature
                new_properties = [key for key in into_features["properties"].keys()]

                # Going through the old properties in the features of src_geojson
                for new_property in new_properties:

                    # Going through the new propeties in the features of dest_geojson
                    if new_property not in old_properties:

                        # Put the new_featu
                        from_features["properties"][new_property] = old_properties[
                            "properties"
                        ][new_property]

    return geojson_src


def geojson_to_features_list(json_data):
    """Converts a decoded output GeoJSON to a list of feature objects
    example:
    From,
    {'type': 'FeatureCollection', 'features': [{'type': 'Feature', 'geometry': {'type': 'Point',
    'coordinates': [30.98594605922699, 30.003757307208872]}, 'properties': {}}]}

    To,
    [{'type': 'Feature', 'geometry': {'type': 'Point',
    'coordinates': [30.98594605922699, 30.003757307208872]}, 'properties': {}}]

    The purpose of this formatting utility is to obtain a list of individual features for
    decoded tiles that can be later extended to the output GeoJSON
    """

    return json_data["features"]


def merged_features_list_to_geojson(features_list: list) -> str:
    """Converts a processed features list (i.e. a features list with all the needed features merged
    from multiple tiles) into a fully-featured GeoJSON

    :param features_list: a list of processed features merged from different tiles within a bbox
    :type features_list: list
    example:
    From,
    [{'type': 'Feature', 'geometry': {'type': 'Point',
    'coordinates': [30.98594605922699, 30.003757307208872]}, 'properties': {}}, ...]

    To,
    {'type': 'FeatureCollection', 'features': [{'type': 'Feature', 'geometry': {'type': 'Point',
    'coordinates': [30.98594605922699, 30.003757307208872]}, 'properties': {}}, ...]}

    :return: GeoJSON string formatted with all the extra commas removed.
    :rtype: str
    """
    return json.dumps({"type": "FeatureCollection", "features": features_list})


def detection_features_to_geojson(feature_list: list) -> dict:
    """Converts a preprocessed list (i.e, features from the detections of either images or
    map_features from multiple segments) into a fully featured GeoJSON

    :param features_list: A list of processed features merged from different segments within a
    detection
    :type features_list: list

    Example::
        >>> # From
        >>> [{'created_at': '2021-05-20T17:49:01+0000', 'geometry':
        ... 'GjUKBm1weS1vchIVEgIAABgDIg0JhiekKBoqAABKKQAPGgR0eXBlIgkKB3BvbHlnb24ogCB4AQ==',
        ... 'image': {'geometry': {'type': 'Point', 'coordinates': [-97.743279722222,
        ... 30.270651388889]}, 'id': '1933525276802129'}, 'value': 'regulatory--no-parking--g2',
        ... 'id': '1942105415944115'}, ... ]
        >>> # To
        >>> {'type': 'FeatureCollection', 'features': [{'type': 'Feature', 'geometry':
        ... {'type': 'Point', 'coordinates': [-97.743279722222, 30.270651388889]}, 'properties': {
        ... 'image_id': '1933525276802129', 'created_at': '2021-05-20T17:49:01+0000',
        ... 'pixel_geometry':
        ... 'GjUKBm1weS1vchIVEgIAABgDIg0JhiekKBoqAABKKQAPGgR0eXBlIgkKB3BvbHlnb24ogCB4AQ=='`,
        ... 'value': 'regulatory--no-parking--g2', 'id': '1942105415944115' } }, ... ]}

    :return: GeoJSON formatted as expected in a detection format
    :rtype: dict
    """

    resulting_geojson = {
        # FeatureCollection type
        "type": "FeatureCollection",
        # List of features
        "features": [
            # Feature generation from feature_list
            {
                # Type is 'Feature'
                "type": "Feature",
                # Let 'geometry' be the `image` key, defaults to {} is `image` not in feature
                "geometry": {
                    "type": "Point",
                    "coordinates": feature["image"]["geometry"]["coordinates"],
                }
                if "image" in feature
                else {},
                # Property list
                "properties": {
                    # Only if "image" was specified in the `fields` of the endpoint, else None
                    "image_id": feature["image"]["id"]
                    if "image" in "feature"
                    else None,
                    # Only if "created_at" was specified in the `fields` of the endpoint, else None
                    "created_at": feature["created_at"]
                    if "created_at" in feature
                    else None,
                    # Only if "geometry" was specified in the `fields` of the endpoint, else None
                    "pixel_geometry": feature["geometry"]
                    if "geometry" in feature
                    else None,
                    # Only if "value" was specified in the `fields` of the endpoint, else None
                    "value": feature["value"] if "value" in feature else None,
                    # "id" is always available in the response
                    "id": feature["id"],
                },
            }
            # Going through the given of features
            for feature in feature_list
        ],
    }

    # The next logic below removes features that defaulted to None

    # Through each feature in the resulting features
    for _feature in resulting_geojson["features"]:

        # Going through each property in the feature
        for _property in _feature["properties"]:

            # If the _property has defauled to None
            if _property is None:

                # Delete the _property from the feature
                del _feature["properties"][_property]

    # Finally return the output
    return resulting_geojson


def flatten_geojson(geojson: dict) -> dict:
    """Flattens a GeoJSON dictionary to a dictionary with only the relevant keys.
    This is useful for writing to a CSV file. The output is a dictionary with the following
    structure:
    {
        "geometry": {
            "type": "Point",
            "coordinates": [x, y]
        },
        "first_seen_at": "UNIX_TIMESTAMP",
        "last_seen_at": "UNIX_TIMESTAMP",
        "value": "regulatory--no-parking--g2",
        "id": "FEATURE_ID",
        "image_id": "IMAGE_ID"
    }
    :param geojson: The GeoJSON to flatten
    :type geojson: dict
    :return: A flattened GeoJSON
    :rtype: dict

    Note:
        1. The `geometry` key is always present in the output
        2. The properties are flattened to the following keys:
            - "first_seen_at"   (optional)
            - "last_seen_at"    (optional)
            - "value"           (optional)
            - "id"              (required)
            - "image_id"        (optional)
            - etc.
        3. If the 'geometry` type is `Point`, two more properties will be added:
            - "longitude"
            - "latitude"
        # TODO: Further testing needed with different geometries, e.g., Polygon, etc.
    """
    for feature in geojson["features"]:
        # Check if the geometry is a Point
        if feature["geometry"]["type"] == "Point":
            # Add longitude and latitude properties to the feature
            feature["properties"]["longitude"] = feature["geometry"]["coordinates"][0]
            feature["properties"]["latitude"] = feature["geometry"]["coordinates"][1]

    # Return the flattened geojson
    return [
        {"geometry": _feature["geometry"], **_feature["properties"]}
        for _feature in geojson["features"]
    ]
