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
from utils.format import geojson_to_features_list


def save_as_csv_controller(data: str, path: str) -> None:
    """Save data as CSV to given file path

    :param data: The data to save as CSV
    :type data: str

    :param path: The path to save to
    :type path: str

    :return: None
    :rtype: None
    """

    # Get the features list from the GeoJSON
    features = geojson_to_features_list(json.loads(data))
    
    # Extract the geomtry field from each feature in well-knonwn format (WKT)
    geometries = [shape(feature["geometry"]).wkt for feature in features]
    
    try:
        # Write the CSV file
        with open(os.path.join(path, "geojson.csv"), "w", newline='') as file_path:
            field_names = ['Type', 'Geometry']
            writer = csv.DictWriter(file_path, fieldnames=field_names)
            
            writer.writeheader()
            for geometry in geometries:
                writer.writerow({"Type": geometry.split()[0].capitalize(), "Geometry": geometry})
    except Exception as e:
        print(e)
    return None


def save_as_geojson_controller(data: str, path: str) -> None:
    """Save data as GeoJSON to given file path

    :param data: The data to save as GeoJSON
    :type data: str

    :param path: The path to save to
    :type path: str

    :return: Npne
    :rtype: None
    """
    try:
        with open(os.path.join(path, "geojson.geojson"), "w") as file_path:
            json.dump(json.loads(data), file_path, indent=4)
    except Exception as e:
        print(e)

    return None
