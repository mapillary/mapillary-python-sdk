# -*- coding: utf-8 -*-

"""
mapillary.utils.format

This module deals with converting
data to and from different file formats
"""


def feature_list_to_geojson(json_data):

    output = {"type": "FeatureCollection", "features": []}

    output["features"] = json_data

    return output


def image_entities_to_geojson(json_data_list: list) -> list:

    """From

    [{'geometry': {'type': 'Point', 'coordinates': [30.003755665554, 30.985948744314]},
    'id': '506566177256016'}, ..., ... ]

    To get,

    {'type': 'FeatureCollection', 'features': [{'type': 'Feature', 'geometry': {'type': 'Point',
    'coordinates': [30.98594605922699, 30.003757307208872]}, 'properties': {}}}
    """

    new_json_data_list = []

    for json_data in json_data_list:
        new_json_data_list.append(image_entity_to_geojson(json_data))

    return new_json_data_list


def image_entity_to_geojson(json_data: dict) -> dict:

    """From

    {'geometry': {'type': 'Point', 'coordinates': [30.003755665554, 30.985948744314]}, 'id':
    '506566177256016'}

    To get,

    {'type': 'FeatureCollection', 'features': [{'type': 'Feature', 'geometry': {'type': 'Point',
    'coordinates': [30.98594605922699, 30.003757307208872]}, 'properties': {}}}
    """

    # The geometry property will always be present
    keys = [key for key in json_data.keys() if key != "geometry"]

    init_format = {
        "type": "FeatureCollection",
        "features": [{"type": "Feature", "properties": {}}],
    }
    init_format["features"][0]["geometry"] = json_data["geometry"]

    for key in keys:
        init_format["features"][0]["properties"][key] = json_data[key]

    return init_format


def merge_geojson(
    geojson_one: dict,
    geojson_one_key: str,
    geojson_two: dict,
    geojson_two_key: str,
    debug=True,
) -> dict:

    geojson_from = geojson_one.copy()
    geojson_into = geojson_two.copy()

    list_one = []
    list_two = []

    for from_features in geojson_from["features"]:

        for into_features in geojson_into["features"]:

            if (
                geojson_two_key not in into_features["properties"]
                or geojson_one_key not in from_features["properties"]
            ):
                # * REFACTOR: This is better if it can be logged
                # * in the future
                continue

            list_one.append(int(from_features["properties"][geojson_one_key]))
            list_two.append(int(into_features["properties"][geojson_two_key]))

            if debug:
                print(
                    int(from_features["properties"][geojson_one_key])
                    == int(into_features["properties"][geojson_two_key]),
                    int(into_features["properties"][geojson_two_key]),
                    int(from_features["properties"][geojson_one_key]),
                )

            if int(from_features["properties"][geojson_one_key]) == int(
                into_features["properties"][geojson_two_key]
            ):

                old_properties = [key for key in from_features["properties"].keys()]

                new_properties = [key for key in into_features["properties"].keys()]

                if debug:
                    print(old_properties)
                    print(new_properties)

                for feature in new_properties:

                    if feature not in old_properties:

                        from_features["properties"][feature] = old_properties[
                            "properties"
                        ][feature]

    if debug:
        print(list(set(list_one) & set(list_two)))

    return geojson_from
