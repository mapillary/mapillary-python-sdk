# -*- coding: utf-8 -*-

"""
mapillary.models.exceptions

This module contains the set of Mapillary's exceptions
"""


class MapillaryException(Exception):
    """Base class for exceptions in this module"""

    pass


class InvalidTokenError(MapillaryException):
    """Raised when an invalid token is given
    to access Mapillary's API, primarily used in mapillary.set_access_token

    :var message: The error message returned
    :var type: The type of error that occurred
    :var code: The error code returned,
    most like 190, "Access token has expired",
    see
    https://developers.facebook.com/docs/graph-api/using-graph-api/error-handling/
    for more information
    :fbtrace_id: A unique ID to track the issue/exception
    """

    def __init__(self, message, type, code, fbtrace_id):
        """ """
        self.message = message
        self.type = type
        self.code = code
        self.fbtrace_id = fbtrace_id

    def __str__(self):
        return f"{self.message}"

    def __repr__(self):
        return (
            "InvalidTokenError: An exception occured."
            + f'Message: "{self.message}", Type: "{self.type}",'
            + f'Code: "{self.code}",'
            + f'fbtrace_id: "{self.fbtrace_id}"'
        )


class AuthError(MapillaryException):
    """Raised when a function is called without
    having the access token set in
    set_access_token to access Mapillary's API,
    primarily used in mapillary.set_access_token
    :var message: The error message returned
    :var type: The type of error that occurred
    :var code: The error code returned,
    most like 190, "Access token has expired",
    see
    https://developers.facebook.com/docs/graph-api/using-graph-api/error-handling/
    for more information
    :fbtrace_id: A unique ID to track the issue/exception
    """

    def __init__(
        self,
        message: str,
    ):
        """Initializing AuthError constructor"""
        self.message = message

    def __str__(self):
        return f'AuthError: An exception occured, "{self.message}"'

    def __repr__(self):
        return "AuthError: An exception occured." + f'Message: "{self.message}"'


class InvalidImageResolution(MapillaryException):
    """Raised when trying to retrieve an image thumbnail with an invalid resolution/size.
    Primarly used with mapillary.image_thumbnail

    :var resolution: Image size entered by the user
    """

    def __init__(self, resolution) -> None:
        self._resolution = resolution

    def __str__(self) -> str:
        return f"""An exception occured, "{self._resolution}" is not a supported image size

Hint: Supported image sizes are: 256, 1024, and 2048
        """

    def __repr__(self) -> str:
        return (
            f'An exception occured, "{self._resolution}" is not a supported image size'
        )


class InvalidImageKey(MapillaryException):
    """Raised when trying to retrieve an image thumbnail with an invalid image ID/key.
    Primarly used with mapillary.image_thumbnail

    :var image_id: Image ID/key entered by the user
    """

    def __init__(self, image_id) -> None:
        self._image_id = image_id

    def __str__(self) -> str:
        return f'An exception occured, "{self._image_id}" is not a valid image ID/key'

    def __repr__(self) -> str:
        return f'An exception occured, "{self._image_id}" is not a valid image ID/key'
