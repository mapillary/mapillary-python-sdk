"""
mapillary.mapillary
~~~~~~~~~~~~~~~~~~~

This module implements the basic functionalities
of the Mapillary Python SDK, a pythonic
implementation of the Mapillary API v4. For
more information, please check out
https://www.mapillary.com/developer/api-documentation/

:copyright: (c) 2021 ...
:license: See LICENSE for more details
"""

# Datetime
from datetime import datetime

# Local
from models.credentials import Credentials
from models.auth import auth

# Local
import controller.image as image


@auth()
def greetings(name):
    """A greetings function temporarily here to test
    if the package installation is working as expected

    :param name: a name given to the function to print
    out a basic statement. Temporary solution made to
    testing if the function is working as expected
    :type name: str

    :return: None
    :rtype: None

    Usage::
        >>> import mapillary as mly
        >>> mly.greetings('New User')
        "Hello, there, New User! Nice to meet you.
        As you can see, work is currently under progress"
    """

    print(
        f"Hello, there, {name}! Nice to meet you. "
        "As you can see, work is currently under progress."
    )

    return None


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

    Credentials.set_token(token)

    return {"Status": "Success"}


@auth()
def get_image_close_to(latitude=-122.1504711, longitude=37.485073, **kwargs):
    """Function that takes a longitude, latitude as
    argument and outputs the near images. This makes
    an API call with the token set in set_access_token
    and returns a JSON object.

    :param longitude: The longitude
    :type longitude: float or double

    :param latitude: The latitude
    :type latitude: float or double

    :param kwargs.fields: A list of options, either as 'all',
    or individually accounted lists of fields. For more
    details about the fields themselves, please take a
    look at https://www.mapillary.com/developer/api-documentation/,
    under 'Fields'.
    Geometry must always be included in the fields, even in indvidual
    :type kwargs.fields: list

    :param kwargs.radius: The radius of the images obtained
    from a center center
    :type kwargs.radius: float or int or double

    :param kwargs.coverge: The tile coverage to be obtained,
    either as 'flat', 'pano' (panoramic), or 'both'.
    For more information, please take a look at
    https://www.mapillary.com/developer/api-documentation/
    under 'Coverage Tiles'
    :type kwargs.coverage: str

    :param kwargs.min_date: The min date starting from, with
    'YYYY-MM-DD', 'YYYY-MM-DDTHH:MM:SS'
    :type kwargs.min_date: datetime

    :param kwargs.max_date: The max date to filter upto, with
    'YYYY-MM-DD', 'YYYY-MM-DDTHH:MM:SS'
    :type kwargs.max_date: datetime

    :param kwargs.daterange: Date list. daterange[0] is min_date,
    daterange[1] is max_date. The format is 'YYYY-MM-DD',
    'YYYY-MM-DDTHH:MM:SS'
    :type kwargs.daterange: list

    :param kwargs.org_id: The organization id, ID of the
    organization this image (or sets of images) belong
    to. It can be absent. Thus, default is -1 (None)
    :type kwargs.org_id: int

    :return: None
    :rtype: None

    Usage::
        # TODO: Write code here to display how the function works
    """

    output = image.get_image_close_to_controller(
        latitude=latitude,
        longitude=longitude,
        kwargs=kwargs,
    )

    return output


@auth()
def get_image_looking_at(
    coordinates_looker,
    coordinates_at,
    fields=["all"],
    radius=200,
    coverage="pano",
    date=datetime.today().strftime("%Y-%m-%d"),
    org_id=-1,
):
    """Function that takes two sets of latitude and
    longitude, where the 2nd set is the "looking at"
    location from 1st set's perspective
    argument and outputs the near images. This
    makes an API call with the token set in
    set_access_token and returns a JSON object.

    :param coordinates_looker: The coordinate sets from
    where a certain point is being looked at, it has
    length 2, index@0 is lat, index@1 is long
    :type coordinates_looker: list

    :param coordinates_at: The coordinate sets to
    where a certain point is being looked at, it has
    length 2, index@0 is lat, index@1 is long
    :type coordinates_at: list

    :param fields: A list of options, either as 'all',
    or individually accounted lists of fields. For more
    details about the fields themselves, please take a
    look at
    https://www.mapillary.com/developer/api-documentation/,
    under 'Fields'. Geometry must always be included in
    the fields, even in indvidual
    :type fields: list

    :param radius: The radius of the images obtained
    from a center center
    :type radius: float or int or double

    :param coverge: The tile coverage to be obtained,
    either as 'flat', 'pano' (panoramic), or 'both'.
    For more information, please take a look at
    https://www.mapillary.com/developer/api-documentation/
    under 'Coverage Tiles'
    :type coverage: str

    :param date: The date to filter to, if needed.
    The date format currently is 'YYYY-MM-DD', or '%Y-%m-%d'
    :type date: datetime

    :param org_id: The organization id, ID of the
    organization this image (or sets of images) belong
    to. It can be absent. Thus, default is -1 (None)
    :type org_id: int

    :return: None
    :rtype: None

    Usage::
        # TODO: Write code here to display how the function works
    """

    # * `coordinates_looker` and `coordinates_at`
    # * can be the same or different

    # ? It may be useful to have the function
    # ? exclude images that are too close to the
    # ? looking at longitude, latitude, as if
    # ? within 3 meters, as the returned photo may
    # ? be too close to be useful. 10+ meters may be
    # ? best

    # TODO: This functions needs implementation

    return None


@auth()
def get_detections_from_key(key):
    """Extracting all the detections within an image using an image key

    :param key: The image key as the argument
    :type key: int

    :return: JSON
    :rtype: <class 'dict'>

    Usage::
        # TODO: Write code here to display how the function works
    """

    # TODO: This functions needs implementation

    return None


@auth()
def get_detections_for_feature_from_key(feature_key):
    """Extracting all detections made for a map feature key

    :param feature_key: A map feature key as the argument
    :type feature_key: str # ? To check if valid

    :return: JSON
    :rtype: <class 'dict'>

    Usage::
        # TODO: Write code here to display how the function works
    """

    # TODO: This functions needs implementation

    return None


@auth()
def get_image_thumbnail_from_key(map_key, size=1024):
    """Gets the thumbnails of images from the API

    :param map_key: Image key as the argument
    :type map_key: str # ? To check if valid

    :param size: Option for the thumbnail size, ranging from 320 to 2048 width
    :type size: int

    :return: A URL for the thumbnail
    :rtype: str

    Usage::
        # TODO: Write code here to display how the function works
    """

    # TODO: Write logic below that implements
    # TODO: an exception handling mechanism for
    # TODO: checking if the size is the range 320 to 2048, inclusive

    # TODO: This functions needs implementation

    return "https://www.mapillary.com/"


@auth()
def get_images_in_bbox(bbox, **filters):
    """Gets a complete list of all images within a BBox

    :param bbox: Bounding box coordinates, length 4
    :type bbox: list

    :param **filters: Contains filter arguments for
    date, pano/flat. Such is 'date', 'is_pano',
    'is_flat', 'is_both'
    :type **filters: dict

    :return: Output is a GeoJSON object. Could do the
    same for sequences and leave as an option to return
    either image (point) or sequences (line). Sequences
    would NOT be cut at BBox boundary, would select all
    sequences which are partially or entirely in BBox
    :rtype: <class 'dict'>

    Usage::
        # TODO: Write code here to display how the function works
    """

    # TODO: This functions needs implementation

    return {"Message": "Hello, World!"}


@auth()
def get_all_map_features_in_bbox(bbox, layer, **filters):
    """Extracts all map features within a bounding box (bbox)

    :param bbox: Bbox coordinates as the argument
    :type bbox: list

    :param layer: 'Points' or 'Traffic Signs'
    :type layer: str

    :param **filters: Contains two possible filter arguments,
        1. Value list as arguments (only one value or multiple values or 'all')
        2. Other - data_first_seen, last_seen, # ? More ... ?
    :type **filters: dict

    :return: GeoJSON Object
    :rtype: JSON
    # ? Maybe we should implement a
    # ? GeoJSON class to keep 'objects'
    # ? consistent

    Usage::
        # TODO: Write code here to display how the function works
    """

    # TODO: This functions needs implementation

    return {"Message": "Hello, World!"}


@auth()
def get_all_images_in_a_shape(geoJSON, **filters):
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
        # TODO: Write code here to display how the function works
    """

    # TODO: This functions needs implementation

    return None


@auth()
def get_all_map_features_in_shape(geoJSON, **filters):
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
def get_feature_from_map_feature_key(map_feature_key, fields):
    """Gets features for the given map_key argument

    :param map_feature_key: The map feature key to
    extract features
    :type map_feature_key: int

    :param fields: The fields to include. Geometry is
    always included in the request
    :type fields: list

    :return: JSON
    :rtype: <class 'dict'>

    Usage::
        # TODO: Write code here to display how
        # TODO: the function works
    """

    # TODO: This functions needs implementation

    return None


@auth()
def get_feature_from_image_feature_key(image_feature_key):
    """Gets features for the given map_key argument

    :param image_feature_key: The image feature key to
    extract features
    :type image_feature_key: int

    :param fields: The fields to include. Geometry is
    always included in the request
    :type fields: list

    :return: JSON
    :rtype: <class 'dict'>

    Usage::
        # TODO: Write code here to display how
        # TODO: the function works
    """

    # TODO: This functions needs implementation

    return None


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
