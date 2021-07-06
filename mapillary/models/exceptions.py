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
    to access Mapillary's API, primarily used in
    mapillary.set_access_token

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
        type: str,
        code: str,
        fbtrace_id: str,
    ):
        """Initializing InvalidTokenError constructor"""
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


class InvalidKwargError(MapillaryException):
    """Raised when a function is called with the invalid
    keyword argument(s) that do not belong to the
    requested API end call

    :var func: The function that was called
    :var key: The key that was passed
    :var code: The value along with that key
    :var optional_keys: The list of possible keys that can be passed,
    to help the user correct his/her mistake
    """

    def __init__(
        self,
        func: str,
        key: str,
        value: str,
        optional_keys: list,
    ):
        """Initializing InvalidKwargError constructor"""
        self.func = func
        self.key = key
        self.value = value
        self.optional_keys = optional_keys

    def __str__(self):
        return (
            f'InvalidKwargError: The invalid kwarg, ["{self.key}": '
            f'{self.value}] was passed to the function, "{self.func}".\n'
            f"A possible list of keys for this function are, "
            f'{", ".join(self.optional_keys)}'
        )

    def __repr__(self):
        return (
            f'InvalidKwargError: The invalid kwarg, ["{self.key}": '
            f'{self.value}] was passed to the function, "{self.func}".\n'
            f"A possible list of keys for this function are, "
            f'{", ".join(self.optional_keys)}'
        )


class InvalidDateError(MapillaryException):
    """When an invalid date is provided

    :var date: The function that was called
    """

    def __init__(
        self,
        date: str,
    ):
        """Initializing InvalidDateError constructor"""
        self.date = date

    def __str__(self):
        return f'InvalidDateError: Invalid date, "{self.date}"'

    def __repr__(self):
        return f'InvalidDateError: The invalid kwarg, "{self.date}"'


class ContradictingError(MapillaryException):
    """When two or more opposing keys in kwargs
    has been provided

    :var contradicts: The kwarg that contradicts
    :var contradicted: the kwarg contradicted
    """

    def __init__(
        self,
        contradicts: str,
        contradicted: str,
        message: str,
    ):
        """Initializing ContradictingError constructor"""
        self.contradicts = contradicts
        self.contradicted = contradicted
        self.message = message

    def __str__(self):
        return (
            f'ContradictingError: Kwarg, "{self.contradicted}" '
            f'contradicted due to kwarg, "{self.contradicts}" '
            f'with error message, "{self.message}"'
        )

    def __repr__(self):
        return (
            f'ContradictingError: Kwarg, "{self.contradicted}" '
            f'contradicted due to kwarg, "{self.contradicts}" '
            f'with error message, "{self.message}"'
        )


class OutOfBoundZoomError(MapillaryException):
    """Out of bound zoom error

    :var zoom: The zoom value used
    :var options: the possible list of zoom values
    """

    def __init__(
        self,
        zoom: int,
        options: list,
    ):
        """Initializing OutOfBoundZoomError constructor"""
        self.zoom = zoom
        self.options = options

    def __str__(self):
        return (
            f'OutOfBoundZoomError: Given zoom value, "{self.zoom}" '
            f'while possible zoom options, [{", ".join(self.options)}] '
        )

    def __repr__(self):
        return (
            f'OutOfBoundZoomError: Given zoom value, "{self.zoom}" '
            f'while possible zoom options, [{", ".join(self.options)}] '
        )
