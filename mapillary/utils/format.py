# -*- coding: utf-8 -*-

"""
mapillary.utils.format
This module deals with converting
data to and from different file formats
"""
import json


def feature_list_to_geojson(json_data):
    """Converts from only a given feature list into a fully featured
    GeoJSON

    From,
    {'features': [{'type': 'Feature', 'geometry': {'type': 'Point',
    'coordinates': [30.98594605922699, 30.003757307208872]}, 'properties': {}}]}

    To,
    {'type': 'FeatureCollection', 'features': [{'type': 'Feature', 'geometry': {'type': 'Point',
    'coordinates': [30.98594605922699, 30.003757307208872]}, 'properties': {}}]}
    """

    return {"type": "FeatureCollection", "features": json_data['features']}


def features_list_to_geojson(json_data_list: list) -> list:

    """From
    [{'geometry': {'type': 'Point', 'coordinates': [30.003755665554, 30.985948744314]},
    'id': '506566177256016'}, ..., ... ]
    To get,
    {'type': 'FeatureCollection', 'features': [{'type': 'Feature', 'geometry': {'type': 'Point',
    'coordinates': [30.98594605922699, 30.003757307208872]}, 'properties': {}}]}
    """

    return {
        "type": "FeatureCollection",
        "features": [
            feature_list_to_geojson(json_data) for json_data in json_data_list
        ],
    }


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
    feature["type"] = feature.get("type", json_data["type"])
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


def geojson_to_feature_object(json_data):
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