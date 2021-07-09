# -*- coding: utf-8 -*-

"""
mapillary.utils.extract
This module deals with extracting multiple fields
nested within a GeoJSON packet
"""


def extract_properties(geojson, properties):

    extracted_fields = {}

    for property in properties:
        extracted_fields[property] = []

    for feature in geojson["features"]:
        for property in properties:
            if property in feature["properties"]:
                extracted_fields[property].append(feature["properties"][property])

    return extracted_fields