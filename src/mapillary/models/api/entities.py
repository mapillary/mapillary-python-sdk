# Copyright (c) Facebook, Inc. and its affiliates. (http://www.facebook.com)
# -*- coding: utf-8 -*-

"""
mapillary.models.api.entities
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module contains the Adapter design for the Entities API of Mapillary APIv4.

For more information, please check out https://www.mapillary.com/developer/api-documentation/.

:copyright: (c) 2021 Facebook
:license: MIT LICENSE
"""

# Package Imports
import json
import ast

# Local imports

# # Utilities
from mapillary.utils.format import detection_features_to_geojson

# # Models
from mapillary.models.client import Client

# # Exception Handling
from mapillary.models.exceptions import InvalidImageKey

# # Config
from mapillary.config.api.entities import Entities

# Library imports
from requests import HTTPError


class EntityAdapter(object):
    """Adapter model for dealing with the Entity API, through the DRY principle. The EntityAdapter
    class can be instantiated in the controller modules, providing an abstraction layer that uses
    the Client class, endpoints provided by the APIv4 under `/config/api/entities.py`.

    It performs parsing, handling of layers, properties, and fields to make it easier to
    write higher level logic for extracing information, and lets developers to focus only
    on writing the high level business logic without having to repeat the process of parsing
    and using libraries such as `mercantile`, `ast`, and others to only then care about the
    inputs and the outputs

    Usage::
        >>> EntityAdapter().fetch_layer(image_id=image_id, fields=[
                    'altitude', 'atomic_scale', 'geometry', 'width'
                ])
        >>> EntityAdapter().fetch_map_features(map_feature_id=map_feature_id, fields=[
                    'first_seen_at', 'last_seen_at', 'geometry'
                ])
    """

    def __init__(self):
        """Initializing EntityAdapter constructor"""

        # client object to deal with session and requests
        self.client = Client()

    def fetch_image(self, image_id: int, fields: list = []) -> dict:
        """Fetches images depending on the image_id and the fields provided

        :param image_id: The image_id to extract for
        :type image_id: int

        :param fields: The fields to extract properties for, defaults to []
        :type fields: list

        :return: The fetched GeoJSON
        :rtype: dict
        """

        # Getting the results through the client, and return after decoding
        try:
            return (
                # Converts the dict to a GeoJSON format
                # image_entity_to_geojson(
                # ast converts the str dict to a dict object
                ast.literal_eval(
                    # The results returned here are the str dicts
                    self.client.get(
                        # Calling the endpoint with the parameters ...
                        Entities.get_image(
                            # ... image_id, for the needed image ...
                            image_id=image_id,
                            # ... the fields passed in in ...
                            fields=fields
                            # ... only if the fields are not empty ...
                            if fields != []
                            # ... if they are, get all the fields as a list instead
                            else Entities.get_image_fields(),
                        ),
                        # After retrieval of response, only get the content, decode to utf-8
                    ).content.decode("utf-8")
                )
            )
        except HTTPError:
            # If given ID is an invalid image ID, let the user know
            raise InvalidImageKey(image_id)

    def fetch_map_feature(self, map_feature_id: int, fields: list = []):
        """Fetches map feaures depending on the map_feature_id and the fields provided

        :param map_feature_id: The map_feature_id to extract for
        :type map_feature_id: int

        :param fields: The fields to extract properties for, defaults to []
        :type fields: list

        :return: The fetched GeoJSON
        :rtype: dict
        """

        # Getting the results through the client, and return after decoding
        return ast.literal_eval(
            self.client.get(
                # Calling the endpoint with the parameters ...
                Entities.get_map_feature(
                    # ... image_id, for the needed image ...
                    map_feature_id=map_feature_id,
                    # ... the fields passed in in ...
                    fields=fields
                    # ... only if the fields are not empty ...
                    if fields != []
                    # ... if they are, get all the fields as a list instead
                    else Entities.get_map_feature_fields(),
                ),
                # After retrieval of response, only get the content, decode to utf-8
            ).content.decode("utf-8")
        )

    def fetch_detections(self, id: int, id_type: bool = True, fields: list = []):
        """Fetches detections depending on the id, detections for either map_features or
        images and the fields provided

        :param id: The id to extract for
        :type id: int

        :param id_type: Either True(id is for image), or False(id is for map_feature),
        defaults to True
        :type id_type: bool

        :param fields: The fields to extract properties for, defaults to []
        :type fields: list

        :return: The fetched GeoJSON
        :rtype: dict
        """

        # If id_type is True(id is for image)
        if id_type:

            # Store the URL as ...
            url = Entities.get_detection_with_image_id(
                # .. extracted by setting image_id as id ...
                image_id=id,
                # ... passing in the fields given ...
                fields=fields
                # ... only if the fields are not provided empty ...
                if fields != []
                # ... but if they are, set the fields as all possible fields ...
                else Entities.get_detection_with_image_id_fields(),
            )

        # If id_type is False(id is for map_feature)
        else:

            # Store the URL as ...
            url = Entities.get_detection_with_map_feature_id(
                # ... extracted by setting map_feature_id as id ...
                map_feature_id=id,
                # ... passing in the fields given ...
                fields=fields
                # ... only if the fields are not provided empty ...
                if fields != []
                # ... but if they are, set the fields as all possible fields ...
                else Entities.get_detection_with_map_feature_id_fields(),
            )

        # Retrieve the relevant data with `url`, get content, decode to utf-8, return
        return detection_features_to_geojson(
            json.loads(self.client.get(url).content.decode("utf-8"))["data"]
        )

    def is_image_id(self, id: int, fields: list = []) -> dict:
        """Determines whether the given id is an image_id or a map_feature_id

        :param id: The ID given to test
        :type id: int

        :param fields: The fields to extract properties for, defaults to []
        :type fields: list

        :return: True if id is image, else False
        :rtype: bool

        """

        try:
            # If image data is fetched without an exception being thrown ...
            self.fetch_image(image_id=id, fields=fields)

            # ... return True
            return True

        # An exception to catch the InvalidImageKey exception
        except Exception:

            # If exception, return False
            return False
