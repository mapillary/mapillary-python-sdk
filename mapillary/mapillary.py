# Copyright (c) Facebook, Inc. and its affiliates. (http://www.facebook.com)
# -*- coding: utf-8 -*-

"""
mapillary.mapillary
~~~~~~~~~~~~~~~~~~~

This module implements the basic functionalities of the Mapillary Python SDK, a pythonic
implementation of the Mapillary API v4. For more information, please check out
https://www.mapillary.com/developer/api-documentation/

:copyright: (c) 2021 Facebook
:license: MIT LICENSE
"""

# Local
from models.client import Client
from models.auth import auth

# Controllers
import controller.image as image
import controller.feature as feature
import controller.detection as detection


def set_access_token(token: str):
    """A function allowing the user to set an access
    token for the session, which they can create at
    https://www.mapillary.com/dashboard/developers.
    Takes token as an argument and sets a global
    variable used by other functions making API requests.
    For more information what the details of authentication,
    please check out the blog post at Mapillary.
    https://blog.mapillary.com/update/2021/06/23/getting-started-with-the-new-mapillary-api-v4.html

    :param token: The token itself that would
    be set and accessed globally. Must be obtained
    :type token: str

    :return: None
    :rtype: None

    Usage::
        >>> import mapillary as mly
        >>> mly.set_access_token('CLIENT_TOKEN_HERE')
    """

    Client.set_token(token)

    return {"Success": "Token set"}


@auth()
def get_image_close_to(latitude=-122.1504711, longitude=37.485073, **kwargs):
    """Function that takes a longitude, latitude as argument and outputs the near images. This
    makes an API call with the token set in set_access_token and returns a JSON object.

    :param longitude: The longitude
    :type longitude: float or double

    :param latitude: The latitude
    :type latitude: float or double

    :param kwargs.fields: A list of options, either as ['all'], or a list of fields.
    See https://www.mapillary.com/developer/api-documentation/, under 'Fields' for more insight.
    :type kwargs.fields: list

    :param kwargs.radius: The radius of the images obtained from a center center
    :type kwargs.radius: float or int or double

    :param kwargs.image_type: The tile image_type to be obtained, either as 'flat', 'pano'
    (panoramic), or 'both'. See https://www.mapillary.com/developer/api-documentation/ under
    'image_type Tiles' for more information
    :type kwargs.image_type: str

    :param kwargs.min_date: The min date. Format from 'YYYY', to 'YYYY-MM-DDTHH:MM:SS'
    :type kwargs.min_date: str

    :param kwargs.max_date: The max date. Format from 'YYYY', to 'YYYY-MM-DDTHH:MM:SS'
    :type kwargs.max_date: str

    :param kwargs.org_id: The organization id, ID of the organization this image (or sets of
    images) belong to. It can be absent. Thus, default is -1 (None)
    :type kwargs.org_id: int

    :return: GeoJSON
    :rtype: dict

    Usage::
        >>> import mapillary as mly
        >>> mly.set_access_token('CLIENT_TOKEN_HERE')
        >>> mly.get_image_close_to(longitude=31, latitude=30)
        {'type': 'FeatureCollection', 'features': [{'type': 'Feature',
        'geometry': {'type': 'Point', 'coordinates': [30.9912246465683,
        29.99794091267283]}, 'properties': {'captured_at': 1621008070596,
        'compass_angle': 322.56726074219, 'id': 499412381300321, 'is_pano':
        False, 'sequence_id': '94afmyyhq85xd9bi8p44ve'}} ...
    """

    return image.get_image_close_to_controller(
        latitude=latitude,
        longitude=longitude,
        kwargs=kwargs,
    )


@auth()
def get_image_looking_at(
    looker: dict,
    at: dict,
    **filters: dict,
) -> dict:
    """Function that takes two sets of latitude and longitude, where the 2nd set is the
    "looking at" location from 1st set's perspective argument and outputs the near images. This
    makes an API call with the token set in set_access_token and returns a JSON object.

    :param looker: The coordinate sets from where a certain point is being looked at in the format,
        >>> looker = {
        >>>     'lng': <longitudinal parameter>
        >>>     'lat': <latitude parameters>
        >>> }
    :type looker: dict

    :param at: The coordinate sets to where a certain point is being looked at in the format
        >>> at = {
        >>>     'lng': <longitudinal parameter>
        >>>     'lat': <latitude parameters>
        >>> }
    :type at: dict

    :param filters.min_date: The minimum date to filter till
    :type filters.min_date: str

    :param filters.max_date: The maximum date to filter upto
    :type filters.max_date: str

    :param filters.radius: The radius that the geometry points will lie in
    :type filters.radius: float

    :param filters.image_type: Either 'pano', 'flat' or 'all'
    :type filters.image_type: str

    :param filters.organization_id: The organization to retrieve the data for
    :type filters.organization_id: str

    :return: The GeoJSON response containing relevant features
    :rtype: dict

    Usage::
        >>> import mapillary as mly
        >>> mly.set_access_token('CLIENT_TOKEN_HERE')
        >>> data = mly.get_image_looking_at(
                    looker={
                        'lng': 12.954940544167,
                        'lat': 48.0537894275,
                    },
                    at={
                        'lng': 12.955075073889,
                        'lat': 48.053805939722,
                    },
                    radius = 5000,
                )
        >>> data
        ... {'type': 'FeatureCollection', 'features': [{'type': 'Feature', 'geometry': {'type':
        'Point', 'coordinates': [12.954479455947876, 48.05091893670834]}, 'properties':
        {'captured_at': 1612606959408, 'compass_angle': 21.201110839844, 'id': 1199705400459580,
        'is_pano': False, 'sequence_id': 'qrrqtke4a6vtygyc7w8rzc'}}, ... }

    Testing::
        >>> import mapillary as mly
        >>> mly.set_access_token('CLIENT_TOKEN_HERE')
        >>> data_1 = mly.get_image_looking_at(
                    looker={
                        'lng': 12.954940544167,
                        'lat': 48.0537894275,
                    },
                    at={
                        'lng': 12.955075073889,
                        'lat': 48.053805939722,
                    },
                    radius = 2000,
                )
        >>> data_1 = json.loads(data_1)
        >>> data_2 = mly.get_image_looking_at(
                    looker={
                        'lng': 12.954940544167,
                        'lat': 48.0537894275,
                    },
                    at={
                        'lng': 12.955075073889,
                        'lat': 48.053805939722,
                    },
                    radius = 5000,
                )
        >>> data_2 = json.loads(data_2)
        >>> len(data_1['features']) == len(data_2['features'])
        ... True
        >>> # The total features did not change on increasing the radius
        >>> data_3 = mly.get_image_close_to(
                    longitude=12.954940544167,
                    latitude=48.0537894275,
                    radius = 5,
                )
        >>> len(data_3['features'])
        ... 32
        >>> data_4 = mly.get_image_looking_at(
                    looker={
                        'lng': 12.954940544167,
                        'lat': 48.0537894275,
                    },
                    at={
                        'lng': 12.955075073889,
                        'lat': 48.053805939722,
                    },
                    radius = 5,
                )
        >>> len(data_4['features'])
        ... 11
        >>> # Only selected features are actually looking at the location
    """

    return image.get_image_looking_at_controller(
        looker=looker,
        at=at,
        filters=filters,
    )


@auth()
def get_detections_with_image_id(image_id: int, **filters):
    """Extracting all the detections within an image using an image key

    :param image_id: The image key as the argument
    :type image_id: int

    :return: The GeoJSON in response
    :rtype: dict

    Usage::
        >>> import mapillary as mly
        >>> mly.set_access_token('CLIENT_TOKEN_HERE')
        >>> mly.get_detections_with_image_id(image_id=1933525276802129)
        ... '{"data":[{"created_at":"2021-05-20T17:49:01+0000","geometry":
        ... "GjUKBm1weS1vchIVEgIAABgDIg0JhiekKBoqAABKKQAPGgR0eXBlIgkKB3BvbHlnb24ogCB4AQ==","image"
        ... :{"geometry":{"type":"Point","coordinates":[-97.743279722222,30.270651388889]},"id":
        ... "1933525276802129"},"value":"regulatory--no-parking--g2","id":"1942105415944115"},
        ... {"created_at":"2021-05-20T18:40:21+0000","geometry":
        ... "GjYKBm1weS1vchIWEgIAABgDIg4J7DjqHxpWAADiAVUADxoEdHlwZSIJCgdwb2x5Z29uKIAgeAE=",
        ... "image":{"geometry":{"type":"Point","coordinates":[-97.743279722222,30.270651388889]},
        ... "id":"1933525276802129"},"value":"information--parking--g1","id":"1942144785940178"},
        ... , ...}
    """

    return detection.get_image_detections_controller(
        image_id=image_id,
        filters=filters,
    )


@auth()
def get_detections_with_map_feature_id(map_feature_id: int, **filters) -> dict:
    """Extracting all detections made for a map feature key

    :param map_feature_id: A map feature key as the argument
    :type map_feature_id: int

    :return: The GeoJSON in response
    :rtype: dict

    Usage::
        >>> import mapillary as mly
        >>> mly.set_access_token('CLIENT_TOKEN_HERE')
        >>> mly.get_detections_with_map_feature_id(map_feature_id=1933525276802129)
        ...     File "/home/saif/MLH/mapillary-python-sdk/mapillary/controller/rules/verify.py",
        ...         line 227, in valid_id
        ...             raise InvalidOptionError(
        ... models.exceptions.InvalidOptionError: InvalidOptionError: Given id value,
        ...     "Id: 1933525276802129, image: False" while possible id options, [Id is image_id
        ...     AND image is True, key is map_feature_id ANDimage is False]
    """

    return detection.get_map_feature_detections_controller(
        map_feature_id=map_feature_id,
        filters=filters,
    )


@auth()
def image_thumbnail(image_id, resolution=1024) -> str:
    """Gets the thumbnails of images from the API

    :param image_id: Image key as the argument

    :param resolution: Option for the thumbnail size, with available resolutions:
    256, 1024, and 2048

    :return: A URL for the thumbnail
    :rtype: str

    Usage::
        >>> import mapillary as mly
        >>> mly.set_access_token('MLY|XXX')
        >>> mly.image_thumbnail(
        ...     image_id='IMAGE_ID_HERE', resolution='DESIRED_RESOLUTION'
        ... )
    """
    return image.get_image_thumbnail_controller(image_id, resolution=resolution)


@auth()
def images_in_bbox(bbox: dict, **filters) -> str:
    """Gets a complete list of images with custom filter within a BBox

    :param bbox: Bounding box coordinates
    example: {
        'west': 'BOUNDARY_FROM_WEST',
        'south': 'BOUNDARY_FROM_SOUTH',
        'east': 'BOUNDARY_FROM_EAST',
        'north': 'BOUNDARY_FROM_NORTH'
    }
    :type bbox: dict

    :param **filters: Different filters that may be applied to the output.
    example filters:
    - max_date
    - min_date
    - image_type: pano, flat, or all
    - compass_angle
    - sequence_id
    - organization_id
    :type **filters: dict

    :return: Output is a GeoJSON string that represents all the within a bbox after passing given
    filters.
    :rtype: <class 'str'>

    Usage::
        >>> import mapillary as mly
        >>> mly.set_access_token('MLY|XXX')
        >>> mly.images_in_bbox(
        ...     bbox={
        ...         'west': 'BOUNDARY_FROM_WEST',
        ...         'south': 'BOUNDARY_FROM_SOUTH',
        ...         'east': 'BOUNDARY_FROM_EAST',
        ...         'north': 'BOUNDARY_FROM_NORTH'
        ...     },
        ...     max_date='YYYY-MM-DD HH:MM:SS',
        ...     min_date='YYYY-MM-DD HH:MM:SS',
        ...     image_type='pano',
        ...     compass_angle=(0, 360),
        ...     sequence_id='SEQUENCE_ID',
        ...     organization_id='ORG_ID'
        ... )
    """

    return image.get_images_in_bbox_controller(
        bbox=bbox, layer="image", zoom=14, filters=filters
    )


@auth()
def sequences_in_bbox(bbox: dict, **filters) -> str:
    """Gets a complete list of all sequences of images that satisfy given filters
    within a BBox.

    :param bbox: Bounding box coordinates
    example: {
        'west': 'BOUNDARY_FROM_WEST',
        'south': 'BOUNDARY_FROM_SOUTH',
        'east': 'BOUNDARY_FROM_EAST',
        'north': 'BOUNDARY_FROM_NORTH'
    }
    :type bbox: dict

    :param **filters: Different filters that may be applied to the output.
    example filters:
    - max_date
    - min_date
    - image_type: pano, flat, or all
    - org_id
    :type **filters: dict

    :return: Output is a GeoJSON string that contains all the filtered sequences within a bbox.
    Sequences would NOT be cut at BBox boundary, would select all sequences which are partially
    or entirely in BBox
    :rtype: <class 'str'>

    Usage::
        >>> import mapillary as mly
        >>> mly.set_access_token('MLY|XXX')
        >>> mly.sequences_in_bbox(
        ...     bbox={
        ...         'west': 'BOUNDARY_FROM_WEST',
        ...         'south': 'BOUNDARY_FROM_SOUTH',
        ...         'east': 'BOUNDARY_FROM_EAST',
        ...         'north': 'BOUNDARY_FROM_NORTH'
        ...     },
        ...     max_date='YYYY-MM-DD HH:MM:SS',
        ...     min_date='YYYY-MM-DD HH:MM:SS',
        ...     image_type='pano',
        ...     org_id='ORG_ID'
        ... )
    """

    return image.get_images_in_bbox_controller(
        bbox=bbox, layer="sequence", zoom=14, filters=filters
    )


@auth()
def map_feature_points_in_bbox(
    bbox: dict, filter_values: list = None, **filters: dict
) -> str:
    """Extracts map feature points within a bounding box (bbox)

    :param bbox: bbox coordinates as the argument
    example: {
        'west': 'BOUNDARY_FROM_WEST',
        'south': 'BOUNDARY_FROM_SOUTH',
        'east': 'BOUNDARY_FROM_EAST',
        'north': 'BOUNDARY_FROM_NORTH'
    }
    :type bbox: dict

    :param filter_values: a list of filter values supported by the API.
    example: ['object--support--utility-pole', 'object--street-light']
    :type filter_values: list

    :param **filters: kwarg filters to be applied on the resulted GeoJSON
    Chronological filters:
    - existed_at: checks if a feature existed after a certain date depending on the time it
    was first seen at.
    - existed_before: filters out the features that existed after a given date
    :type **filters: dict

    :return: GeoJSON Object
    :rtype: <class 'dict'>

    Usage::
        >>> import mapillary as mly
        >>> mly.set_access_token('MLY|XXX')
        >>> mly.map_feature_points_in_bbox(
        ...     bbox={
        ...         'west': 'BOUNDARY_FROM_WEST',
        ...         'south': 'BOUNDARY_FROM_SOUTH',
        ...         'east': 'BOUNDARY_FROM_EAST',
        ...         'north': 'BOUNDARY_FROM_NORTH'
        ...     },
        ...     filter_values=['object--support--utility-pole', 'object--street-light'],
        ...     existed_at='YYYY-MM-DD HH:MM:SS',
        ...     existed_before='YYYY-MM-DD HH:MM:SS'
        ... )
    """

    return feature.get_map_features_in_bbox_controller(
        bbox=bbox, filters=filters, filter_values=filter_values, layer="points"
    )


@auth()
def traffic_signs_in_bbox(
    bbox: dict, filter_values: list = None, **filters: dict
) -> str:
    """Extracts traffic signs within a bounding box (bbox)

    :param bbox: bbox coordinates as the argument
    example: {
        'west': 'BOUNDARY_FROM_WEST',
        'south': 'BOUNDARY_FROM_SOUTH',
        'east': 'BOUNDARY_FROM_EAST',
        'north': 'BOUNDARY_FROM_NORTH'
    }
    :type bbox: dict

    :param filter_values: a list of filter values supported by the API,
    example: ['regulatory--advisory-maximum-speed-limit--g1', 'regulatory--atvs-permitted--g1']
    :type filter_values: list

    :param **filters: kwarg filters to be applied on the resulted GeoJSON
    Chronological filters:
    - existed_at: checks if a feature existed after a certain date depending on the time it
    was first seen at.
    - existed_before: filters out the features that existed after a given date
    :type **filters: dict

    :return: GeoJSON Object
    :rtype: <class 'dict'>

    Usage::
        >>> import mapillary as mly
        >>> mly.set_access_token('MLY|XXX')
        >>> mly.traffic_signs_in_bbox(
        ...    bbox={
        ...         'west': 'BOUNDARY_FROM_WEST',
        ...         'south': 'BOUNDARY_FROM_SOUTH',
        ...         'east': 'BOUNDARY_FROM_EAST',
        ...         'north': 'BOUNDARY_FROM_NORTH'
        ...    },
        ...    filter_values=[
        ...        'regulatory--advisory-maximum-speed-limit--g1',
        ...        'regulatory--atvs-permitted--g1'
        ...    ],
        ...    existed_at='YYYY-MM-DD HH:MM:SS',
        ...    existed_before='YYYY-MM-DD HH:MM:SS'
        ... )
    """

    return feature.get_map_features_in_bbox_controller(
        bbox=bbox, filters=filters, filter_values=filter_values, layer="traffic_signs"
    )


@auth()
def images_in_geojson(geojson: dict, **filters: dict):
    """Extracts all images within a shape

    :param geojson: A geojson as the shape acting as the query extent
    :type geojson: dict

    :param **filters: Different filters that may be applied to the output, defaults to {}
    :type filters: dict (kwargs)

    :param filters.max_date: The max date. Format from 'YYYY', to 'YYYY-MM-DDTHH:MM:SS'
    :type filters.max_date: str

    :param filters.min_date: The min date. Format from 'YYYY', to 'YYYY-MM-DDTHH:MM:SS'
    :type filters.min_date: str

    :param filters.image_type: The tile image_type to be obtained, either as 'flat', 'pano'
    (panoramic), or 'all'. See https://www.mapillary.com/developer/api-documentation/ under
    'image_type Tiles' for more information
    :type filters.image_type: str

    :param filters.compass_angle: The compass angle of the image
    :type filters.compass_angle: int

    :param filters.sequence_id: ID of the sequence this image belongs to
    :type filters.sequence_id: str

    :param filters.organization_id: ID of the organization this image belongs to. It can be absent
    :type filters.organization_id: str

    :return: Output is a GeoJSON string that represents all the within a bbox after passing given
    filters.
    :rtype: dict

    :return: A feature collection as a GeoJSON
    :rtype: dict

    Usage::
        >>> import mapillary as mly
        >>> from models.geojson import GeoJSON
        >>> import json
        >>> mly.set_access_token('MLY|YYY')
        >>> data = mly.images_in_geojson(json.load(open('fetch_map_feature_point.json', mode='r')))
        >>> open('testing_geojson.json', mode='w').write(data.encode())
    """

    return image.images_in_geojson_controller(geojson=geojson, filters=filters)


@auth()
def images_in_shape(shape, **filters: dict):
    """Extracts all images within a shape

    :param shape: A shape that describes features, formatted as a geojson
    :type shape: dict

    :param **filters: Different filters that may be applied to the output, defaults to {}
    :type filters: dict (kwargs)

    :param filters.max_date: The max date. Format from 'YYYY', to 'YYYY-MM-DDTHH:MM:SS'
    :type filters.max_date: str

    :param filters.min_date: The min date. Format from 'YYYY', to 'YYYY-MM-DDTHH:MM:SS'
    :type filters.min_date: str

    :param filters.image_type: The tile image_type to be obtained, either as 'flat', 'pano'
    (panoramic), or 'all'. See https://www.mapillary.com/developer/api-documentation/ under
    'image_type Tiles' for more information
    :type filters.image_type: str

    :param filters.compass_angle: The compass angle of the image
    :type filters.compass_angle: int

    :param filters.sequence_id: ID of the sequence this image belongs to
    :type filters.sequence_id: str

    :param filters.organization_id: ID of the organization this image belongs to. It can be absent
    :type filters.organization_id: str

    :return: Output is a GeoJSON string that represents all the within a bbox after passing given
    filters.
    :rtype: dict

    :return: A feature collection as a GeoJSON
    :rtype: dict

    Usage::
        # TODO: Write code here to display how the function works
    """

    return image.images_in_shape_controller(shape=shape, filters=filters)


@auth()
def get_map_features_in_shape(geoJSON, **filters):
    """Extracts all images within a shape

    :param geoJSON: Bbox coordinates as the argument
    :type geoJSON: list

    :param **filters: Contains filter arguments
    for date, pano/flat. Such is 'date', 'is_pano',
    'is_flat', 'is_both'
    :type **filters: dict

    :return: # ? Not sure, need to ask Chris
    :rtype: # ? Not sure, need to ask Chris

    Usage::
        # TODO: Write code here to display how
        # TODO: the function works
    """

    # TODO: This functions needs implementation

    return None


@auth()
def feature_from_key(key: int, fields: list = []) -> str:
    """Gets a map feature for the given key argument

    :param key: The map feature ID to which will be used to get the feature
    :type key: int

    :param fields: The fields to include. The field 'geometry' will always be included
    so you do not need to specify it, or if you leave it off, it will still be returned.

    Fields::
            1. first_seen_at - timestamp, timestamp of the least recent
            detection contributing to this feature
            2. last_seen_at - timestamp, timestamp of the most recent
            detection contributing to this feature
            3. object_value - string, what kind of map feature it is
            4. object_type - string, either a traffic_sign or point
            5. geometry - GeoJSON Point geometry
            6. images - list of IDs, which images this map feature was derived
            from
    refer to https://www.mapillary.com/developer/api-documentation/#map-feature for more details
    :type fields: list

    :return: A GeoJSON string that represents the queried feature
    :rtype: <class 'str'>

    Usage::
        >>> import mapillary as mly
        >>> mly.set_access_token('MLY|XXX')
        >>> mly.feature_from_key(
        ...     key=VALID_MAP_FEATURE_KEY,
        ...     fields=['object_value']
        ... )
    """
    return feature.get_feature_from_key_controller(key=int(key), fields=fields)


@auth()
def image_from_key(key: int, fields: list = []) -> str:
    """Gets an image for the given key argument

    :param key: The image unique key which will be used for image retrieval
    :type key: int

    :param fields: The fields to include. The field 'geometry' will always be included
    so you do not need to specify it, or if you leave it off, it will still be returned.

    Fields::
            1. altitude - float, original altitude from Exif
            2. atomic_scale - FIXME, FIXME
            3. camera_parameters - FIXME, FIXME
            4. camera_type - enum, type of camera used for taking the phone.
            VALUES: FIXME
            5. captured_at - timestamp, capture time
            6. compass_angle - float, original compass angle of the image
            7. computed_altitude - float, altitude after running image
            processing
            8. computed_compass_angle - float, compass angle after running
            image processing
            9. computed_geometry - GeoJSON Point, location after running image
            processing
            10. computed_rotation - enum, corrected orientation of the image
            11. exif_orientation - enum, original orientation of the image.
            VALUES: FIXME
            12. geometry - GeoJSON Point geometry
            13. height - int, height of the original image uploaded
            14. thumb_256_url - string, URL to the 256px wide thumbnail
            15. thumb_1024_url - string, URL to the 1024px wide thumbnail
            16. thumb_2048_url - string, URL to the 2048px wide thumbnail
            17. merge_cc
            18. mesh - { id: string, url: string } - URL to the mesh
            19. quality_score - float, how good the image is (experimental)
            20. sequence - string, ID of the sequence
            21. sfm_cluster - { id: string, url: string } - URL to the point
            cloud
            22. width - int, width of the original image uploaded
    refer to https://www.mapillary.com/developer/api-documentation/#image for more details
    :type fields: list

    :return: A GeoJSON string that represents the queried image
    :rtype: <class 'str'>

    Usage::
        >>> import mapillary as mly
        >>> mly.set_access_token('MLY|XXX')
        >>> mly.image_from_key(
        ...     key=VALID_IMAGE_KEY,
        ...     fields=['captured_at']
        ... )
    """
    return image.get_image_from_key_controller(key=int(key), fields=fields)


@auth()
def save_to_csv(
    csv_data,
    file_path,
):
    """This function saves the csv data locally with the extension .csv

    :param csv_data: The CSV data to be stored
    :type csv_data: CSV Object

    :param file_path: The path to save the data to
    :type file_path: str

    :return: None
    :rtype: None

    Usage::
        # TODO: Write code here to display how
        # TODO: the function works
    """

    # TODO: This functions needs implementation

    return None


@auth()
def save_as_geojson(
    geojson_data,
    file_path,
):
    """This function saves the geojson data locally with the extension .geojson

    :param geojson_data: The GeoJSON data to be stored
    :type geojson_data: GeoJSON Object

    :param file_path: The path to save the data to
    :type file_path: str

    :return: None
    :rtype: None

    Usage::
        # TODO: Write code here to display how
        # TODO: the function works
    """

    # TODO: This functions needs implementation

    return None
