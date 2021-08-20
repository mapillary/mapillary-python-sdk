# Copyright (c) Facebook, Inc. and its affiliates. (http://www.facebook.com)
# -*- coding: utf-8 -*-

"""
mapillary.models.geojson
~~~~~~~~~~~~~~~~~~~~~~~~

This module contains the class implementation for the geojson

For more information about the API, please check out
https://www.mapillary.com/developer/api-documentation/.

:copyright: (c) 2021 Facebook
:license: MIT LICENSE
"""

# Package
import json

# Local

# # Exceptions
from mapillary.models.exceptions import InvalidOptionError


class Properties:
    """Representation for the properties in a GeoJSON

    :param properties: The properties as the input
    :type properties: dict

    '''
    :raise InvalidOptionError: Raised when the geojson passed is the invalid type - not a dict
    '''

    :return: A class representation of the model
    :rtype: <class 'mapillary.models.geojson.Properties'>
    """

    def __init__(self, *properties, **kwargs) -> None:
        """Initializing Properties constructor"""

        # Validate that the geojson passed is indeed a dictionary
        if not isinstance(properties, dict):

            # Raise InvalidOptionError
            InvalidOptionError(
                # The parameter that caused the exception
                param="Properties.__init__.properties",
                # The invalid value passed
                value=properties,
                # The keys that should be passed instead
                options=["dict"],
            )

        for item in properties:
            for key in item:
                setattr(self, key, item[key])
        for key in kwargs:
            setattr(self, key, kwargs[key])

    def to_dict(self):
        """Return the dictionary representation of the Properties"""

        attr_representation = [
            key for key in dir(self) if not key.startswith("__") and key != "to_dict"
        ]

        return {key: getattr(self, key) for key in attr_representation}

    def __str__(self):
        """Return the informal string representation of the Properties"""

        attr_representation = [
            key for key in dir(self) if not key.startswith("__") and key != "to_dict"
        ]

        attr_key_value_pair = {key: getattr(self, key) for key in attr_representation}

        return f"{attr_key_value_pair}"

    def __repr__(self):
        """Return the formal string representation of the Properties"""

        attr_representation = [
            key for key in dir(self) if not key.startswith("__") and key != "to_dict"
        ]

        attr_key_value_pair = {key: getattr(self, key) for key in attr_representation}

        return f"{attr_key_value_pair}"


class Geometry:
    """Representation for the geometry in a GeoJSON

    :param geometry: The geometry as the input
    :type geometry: dict

    '''
    :raise InvalidOptionError: Raised when the geometry passed is the invalid type - not a dict
    '''

    :return: A class representation of the model
    :rtype: <class 'mapillary.models.geojson.Geometry'>
    """

    def __init__(self, geometry) -> None:
        """Initializing Geometry constructor"""

        # Validate that the geojson passed is indeed a dictionary
        if not isinstance(geometry, dict):

            # Raise InvalidOptionError
            InvalidOptionError(
                # The parameter that caused the exception
                param="Geometry.__init__.geometry",
                # The invalid value passed
                value=geometry,
                # The keys that should be passed instead
                options=["dict"],
            )

        # Setting the type of the selected geometry
        self.type: str = geometry["type"]

        # Setting the coordinates of the geometry
        self.coordinates: list = geometry["coordinates"]

    def to_dict(self):
        """Return dictionary representation of the geometry"""

        return {"type": self.type, "coordinates": self.coordinates}

    def __str__(self):
        """Return the informal string representation of the Geometry"""

        return f"{{'type': {self.type}, 'coordinates': {self.coordinates}}}"

    def __repr__(self):
        """Return the formal string representation of the Geometry"""

        return f"{{'type': {self.type}, 'coordinates': {self.coordinates}}}"


class Feature:
    """Representation for a feature in a feature list

    :param geojson: The GeoJSON as the input
    :type geojson: dict

    '''
    :raise InvalidOptionError: Raised when the geojson passed is the invalid type - not a dict
    '''

    :return: A class representation of the model
    :rtype: <class 'mapillary.models.geojson.Feature'>
    """

    def __init__(self, feature: dict) -> None:
        """Initializing Feature constructor"""

        # Validate that the geojson passed is indeed a dictionary
        if not isinstance(feature, dict):

            # If not, raise `InvalidOptionError`
            InvalidOptionError(
                # The parameter that caused the exception
                param="Feature.__init__.feature",
                # The invalid value passed
                value=feature,
                # The type of value that should be passed instead
                options=["dict"],
            )

        # Setting the type of the selected FeatureList
        self.type = "Feature"

        # Setting the `geometry` property
        self.geometry = Geometry(feature["geometry"])

        # Setting the `properties` property
        self.properties = Properties(feature["properties"])

    def to_dict(self) -> dict:
        """Return the dictionary representation of the Feature"""

        return {
            "type": self.type,
            "geometry": self.geometry.to_dict(),
            "properties": self.properties.to_dict(),
        }

    def __str__(self) -> str:
        """Return the informal string representation of the Feature"""

        return (
            f"{{"
            f"'type': '{self.type}', "
            f"'geometry': {self.geometry}, "
            f"'properties': {self.properties}"
            f"}}"
        )

    def __repr__(self) -> str:
        """Return the formal string representation of the Feature"""

        return (
            f"{{"
            f"'type': {self.type}, "
            f"'geometry': {self.geometry}, "
            f"'properties': {self.properties}"
            f"}}"
        )


class GeoJSON:
    """Representation for a geojson

    :param geojson: The GeoJSON as the input
    :type geojson: dict

    '''
    :raise InvalidOptionError: Raised when the geojson passed is the invalid type - not a dict
    '''

    :return: A class representation of the model
    :rtype: <class 'mapillary.models.geojson.GeoJSON'>

    Usage::
        >>> import mapillary as mly
        >>> from models.geojson import GeoJSON
        >>> mly.set_access_token('MLY|XXX')
        >>> data = mly.get_image_close_to(longitude=31, latitude=31)
        >>> geojson = GeoJSON(geojson=data)
        >>> type(geojson)
        ... <class 'mapillary.models.geojson.GeoJSON'>
        >>> type(geojson.type)
        ... <class 'str'>
        >>> type(geojson.features)
        ... <class 'list'>
        >>> type(geojson.features[0])
        ... <class 'mapillary.models.geojson.Feature'>
        >>> type(geojson.features[0].type)
        ... <class 'str'>
        >>> type(geojson.features[0].geometry)
        ... <class 'mapillary.models.geojson.Geometry'>
        >>> type(geojson.features[0].geometry.type)
        ... <class 'str'>
        >>> type(geojson.features[0].geometry.coordinates)
        ... <class 'list'>
        >>> type(geojson.features[0].properties)
        ... <class 'mapillary.models.geojson.Properties'>
        >>> type(geojson.features[0].properties.captured_at)
        ... <class 'int'>
        >>> type(geojson.features[0].properties.is_pano)
        ... <class 'str'>
    """

    def __init__(self, geojson: dict) -> None:
        """Initializing GeoJSON constructor"""

        # Validate that the geojson passed is indeed a dictionary
        if isinstance(geojson, dict):

            # The GeoJSON should only contain the keys of `type`, `features`, if not empty,
            # raise exception
            if [key for key in geojson.keys() if key not in ["type", "features"]] != []:

                # Raise InvalidOptionError
                InvalidOptionError(
                    # The parameter that caused the exception
                    param="GeoJSON.__init__.geojson",
                    # The invalid value passed
                    value=geojson,
                    # The keys that should be passed instead
                    options=["type", "features"],
                )

        # If the GeoJSON is not of type dictionary
        else:

            # Raise InvalidOptionError
            InvalidOptionError(
                # The parameter that caused the exception
                param="GeoJSON.__init__.geojson",
                # The invalid value passed
                value=geojson,
                # The keys that should be passed instead
                options=["type", "features"],
            )

        # Validate that the geojson passed is indeed a dictionary
        if not isinstance(geojson["features"], list):

            # If not, raise InvalidOptionError
            InvalidOptionError(
                # The parameter that caused the exception
                param="FeatureList.__init__.geojson['features']",
                # The invalid value passed
                value=geojson["features"],
                # The type of the value that should be passed
                options=["list"],
            )

        # Setting the type parameter
        self.type: str = geojson["type"]

        # Setting the list of features
        self.features: list = (
            [Feature(feature=feature) for feature in geojson["features"]]
            if (geojson["features"] != []) or (geojson["features"] is not None)
            else []
        )

    def append_features(self, features: list) -> None:

        for feature in features:
            self.append_feature(feature)

    def append_feature(self, feature_inputs: dict) -> None:

        feature = Feature(feature=feature_inputs)

        if feature not in self.features:
            self.features.append(feature)

    def encode(self):

        return json.dumps(self.__dict__)

    def to_dict(self):
        """Return the dict format representation of the GeoJSON"""

        return {
            "type": self.type,
            "features": [feature.to_dict() for feature in self.features]
            if self.features != []
            else [],
        }

    def __str__(self):
        """Return the informal string representation of the GeoJSON"""

        return f"{{'type': '{self.type}', 'features': {self.features}}}"

    def __repr__(self):
        """Return the formal string representation of the GeoJSON"""

        return f"{{'type': '{self.type}', 'features': {self.features}}}"
