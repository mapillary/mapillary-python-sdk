# Copyright (c) Facebook, Inc. and its affiliates. (http://www.facebook.com)
# -*- coding: utf-8 -*-

"""
mapillary.controllers.save
~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the saving business logic functionalities of the Mapillary Python SDK.

For more information, please check out https://www.mapillary.com/developer/api-documentation/

:copyright: (c) 2021 Facebook
:license: MIT LICENSE
"""

# Package Imports
import os
import json
import csv
from shapely import geometry
from shapely.geometry import shape

# Local Imports
from utils.format import flatten_geojson


def save_as_csv_controller(data: str, path: str, file_name: str) -> None:
    """Save data as CSV to given file path

    :param data: The data to save as CSV
    :type data: str

    :param path: The path to save to
    :type path: str

    :param file_name: The file name to save as
    :type file_name: str

    :return: None
    :rtype: None
    """

    # Get the features list from the GeoJSON
    if isinstance(data, str):
        data = json.loads(data)
    features = flatten_geojson(data)
    print(max([len(feature.keys()) for feature in features]))

    try:
        # Write the CSV file
        file_name = file_name if file_name is not None else "geojson.csv"
        with open(os.path.join(path, file_name), "w", newline="") as file_path:
            field_names = (
                ["ID", "WKT"]
                + [
                    key
                    for key in features[0].keys()
                    if key != "id" and key != "geometry"
                ]
                + ["organization_id"]
            )

            writer = csv.DictWriter(file_path, fieldnames=field_names)

            writer.writeheader()
            for feature in features:
                writer.writerow(
                    {
                        "ID": feature["id"],
                        "WKT": shape(feature["geometry"]).wkt,
                        **{
                            key: feature[key]
                            for key in feature.keys()
                            if key != "id" and key != "geometry"
                        },
                        "organization_id": feature["organization_id"]
                        if "organization_id" in feature
                        else "NULL",
                    }
                )
    except Exception as e:
        print(f"An error occured: {e}")
    return None


def save_as_geojson_controller(data: str, path: str, file_name: str) -> None:
    """Save data as GeoJSON to given file path

    :param data: The data to save as GeoJSON
    :type data: str

    :param path: The path to save to
    :type path: str

    :param file_name: The file name to save as
    :type file_name: str

    :return: Npne
    :rtype: None
    """
    try:
        file_name = file_name if file_name is not None else "geojson.geojson"
        with open(os.path.join(path, file_name), "w") as file_path:
            json.dump(json.loads(data), file_path, indent=4)
    except Exception as e:
        print(e)

    return None
