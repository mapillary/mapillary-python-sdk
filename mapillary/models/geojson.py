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

# Local

# # Exceptions
from models.exceptions import InvalidOptionError


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

    def __init__(self, properties: dict) -> None:
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

        # Setting the properties dictionary
        self.properties: dict = properties

    def __str__(self):
        """Return the informal string representation of the Properties"""

        return f"{self.properties}"

    def __repr__(self):
        """Return the formal string representation of the Properties"""

        return f"{self.properties}"


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

    def __str__(self):
        """Return the informal string representation of the Geometry"""

        return f"{{ 'type': {self.type}, 'coordinates': {self.coordinates} }}"

    def __repr__(self):
        """Return the formal string representation of the Geometry"""

        return f"{{ 'type': {self.type}, 'coordinates': {self.coordinates} }}"


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

    def __str__(self) -> str:
        """Return the informal string representation of the Feature"""

        return (
            f"{{"
            f"  'type': {self.type},"
            f"  'geometry,: {self.geometry},"
            f"  'properties': {self.properties},"
            f"}}"
        )

    def __repr__(self) -> str:
        """Return the formal string representation of the Feature"""

        return (
            f"{{"
            f"  'type': {self.type},"
            f"  'geometry,: {self.geometry},"
            f"  'properties': {self.properties},"
            f"}}"
        )


class FeatureList:
    """Representation for features in a GeoJSON

    :param features: The features as the input
    :type features: list

    '''
    :raise InvalidOptionError: Raised when the feature list passed is the invalid type - not a list
    '''

    :return: A class representation of the model
    :rtype: <class 'mapillary.models.geojson.FeatureList'>
    """

    def __init__(self, features: list) -> None:
        """Initializing FeatureList constructor"""

        # Validate that the geojson passed is indeed a dictionary
        if not isinstance(features, list):

            # If not, raise InvalidOptionError
            InvalidOptionError(
                # The parameter that caused the exception
                param="FeatureList.__init__.features",
                # The invalid value passed
                value=features,
                # The type of the value that should be passed
                options=["list"],
            )

        # Setting the list of features
        self.features: list = [Feature(feature=feature) for feature in features]

    def __str__(self) -> str:
        """Return the informal string representation of the FeatureList"""

        return f"{self.features}"

    def __repr__(self) -> str:
        """Return the formal string representation of the FeatureList"""

        return f"{self.features}"


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
        ... <class 'mapillary.models.geojson.FeatureList'>
        >>> type(geojson.features.features[0])
        ... <class 'mapillary.models.geojson.Feature'>
        >>> type(geojson.features.features[0].type)
        ... <class 'str'>
        >>> type(geojson.features.features[0].geometry)
        ... <class 'mapillary.models.geojson.Geometry'>
        >>> type(geojson.features.features[0].geometry.type)
        ... <class 'str'>
        >>> type(geojson.features.features[0].geometry.coordinates)
        ... <class 'list'>
        >>> type(geojson.features.features[0].properties)
        ... <class 'mapillary.models.geojson.Properties'>
        >>> type(geojson.features.features[0].properties.properties)
        ... <class 'dict'>

    """

    def __init__(self, geojson: dict) -> None:
        """Initializing GeoJSON constructor"""

        # Validate that the geojson passed is indeed a dictionary
        if isinstance(geojson, dict):

            # The GeoJSON should only contain the keys of `type`, `features`, if not empty, raise exception
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

        # Setting the type parameter
        self.type: str = geojson["type"]

        # Setting the list of features
        self.features: FeatureList = FeatureList(features=geojson["features"])

    def __str__(self):
        """Return the informal string representation of the GeoJSON"""

        return f"{{" f"  'type': {self.type}, 'features': {self.features}" f"}}"

    def __repr__(self):
        """Return the formal string representation of the GeoJSON"""

        return f"{{" f"  'type': {self.type}, 'features': {self.features}" f"}}"
