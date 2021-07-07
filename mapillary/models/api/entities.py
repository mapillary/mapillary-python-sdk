# -*- coding: utf-8 -*-

"""
mapillary.models.api.entities

This module contains the Adapter design for the Entities API of Mapillary APIv4
"""

# Package Imports
import ast

# Local imports

# # Utils
from utils.format import image_entity_to_geojson

# # Models
from models.client import Client

# # Config
from config.api.entities import Entities


class EntityAdapter(object):
    def __init__(self):
        self.client = Client()
        pass

    def fetch_image(self, image_id: int, fields: list):
        return image_entity_to_geojson(
            ast.literal_eval(
                self.client.get(
                    Entities.get_image(
                        image_id=image_id,
                        # ! FIX ME: The API is currently broken, see #35
                        fields=fields
                        if fields is not None
                        else Entities.get_image_fields(),
                    ),
                ).content.decode("utf-8")
            )
        )

    def fetch_map_features(self, map_feature_id: int, fields: list):

        # TODO: This function should be tested, not yet fit for use

        return self.client.get(
            Entities.get_map_feature(
                map_feature_id=map_feature_id,
                fields=fields
                if fields is not None
                else Entities.get_map_feature_fields(),
            ),
        ).content.decode("utf-8")

    def fetch_detections(self, id: int, id_type: bool, fields: list):

        # TODO: This function should be tested, not yet fit for use

        # If id_type == True, then we use get_detection_with_image_id
        # else, we use get_detection_with_map_feature_id

        if id_type:
            url = Entities.get_detection_with_image_id(
                image_id=id,
                fields=fields
                if fields is not None
                else Entities.get_detection_with_image_id_fields(),
            )
        else:
            url = Entities.get_detection_with_map_feature_id_fields(
                image_id=id,
                fields=fields
                if fields is not None
                else Entities.get_detection_with_map_feature_id_fields_fields(),
            )

        return self.client.get(url).content.decode("utf-8")

    def __enter__(self):
        print("[EntitiesAdapter] __enter__")

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print("[EntitiesAdapter] __exit__")

    def __repr__(self):
        return "EntitiesAdapter"

    def __str__(self):
        return "EntitiesAdapter"
