# Copyright (c) Facebook, Inc. and its affiliates. (http://www.facebook.com)
# -*- coding: utf-8 -*-

"""
mapillary.models.exceptions
~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module contains the set of Mapillary Exceptions used internally.

For more information, please check out https://www.mapillary.com/developer/api-documentation/.

:copyright: (c) 2021 Facebook
:license: MIT LICENSE
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
    Primarily used with mapillary.image_thumbnail

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
    Primarily used with mapillary.image_thumbnail

    :var image_id: Image ID/key entered by the user
    """

    def __init__(self, image_id) -> None:
        self._image_id = image_id

    def __str__(self) -> str:
        return f'An exception occured, "{self._image_id}" is not a valid image ID/key'

    def __repr__(self) -> str:
        return f'An exception occured, "{self._image_id}" is not a valid image ID/key'


class InvalidKwargError(MapillaryException):
    """Raised when a function is called with the invalid
    keyword argument(s) that do not belong to the
    requested API end call
    :var func: The function that was called
    :var key: The key that was passed
    :var code: The value along with that key
    :var options: The list of possible keys that can be passed,
    to help the user correct his/her mistake
    """

    def __init__(
        self,
        func: str,
        key: str,
        value: str,
        options: list,
    ):
        """Initializing InvalidKwargError constructor"""
        self.func = func
        self.key = key
        self.value = value
        self.options = options

    def __str__(self):
        return (
            f'InvalidKwargError: The invalid kwarg, ["{self.key}": '
            f'{self.value}] was passed to the function, "{self.func}".\n'
            f"A possible list of keys for this function are, "
            f'{", ".join(self.options)}'
        )

    def __repr__(self):
        return (
            f'InvalidKwargError: The invalid kwarg, ["{self.key}": '
            f'{self.value}] was passed to the function, "{self.func}".\n'
            f"A possible list of keys for this function are, "
            f'{", ".join(self.options)}'
        )


class InvalidOptionError(MapillaryException):
    """Out of bound zoom error
    :var zoom: The zoom value used
    :var options: the possible list of zoom values
    """

    def __init__(
        self,
        param: str,
        value: int,
        options: list,
    ):
        """Initializing InvalidOptionError constructor"""
        self.param = param
        self.value = value
        self.options = options

    def __str__(self):
        return (
            f'InvalidOptionError: Given {self.param} value, "{self.value}" '
            f'while possible {self.param} options, [{", ".join(self.options)}] '
        )

    def __repr__(self):
        return (
            f'InvalidOptionError: Given {self.param} value, "{self.value}" '
            f'while possible {self.param} options, [{", ".join(self.options)}] '
        )


class InvalidFieldError(MapillaryException):
    """Raised when an API endpoint is passed invalid
    field elements
    :var endpoint: The API endpoint that was targeted
    :var field: The invalid field that was passed
    """

    def __init__(
        self,
        endpoint: str,
        field: str,
    ):
        """Initializing InvalidFieldError constructor"""
        self.endpoint = endpoint
        self.field = field

    def __str__(self):
        return (
            f'InvalidFieldError: The invalid field, "{self.field}" was '
            f'passed to the endpoint, "{self.endpoint}"'
        )

    def __repr__(self):
        return (
            f'InvalidFieldError: The invalid field, "{self.field}" was '
            f'passed to the endpoint, "{self.endpoint}"'
        )
