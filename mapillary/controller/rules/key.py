"""
mapillary.controller.rules.key
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the checking if the given key is valid for the parameter functionalities of
the Mapillary Python SDK.

For more information, please check out https://www.mapillary.com/developer/api-documentation/

:copyright: (c) 2021 Facebook
:license: MIT LICENSE
"""

# Local imports

# # Models
from models.api.entities import EntityAdapter
from models.exceptions import InvalidOptionError

def valid_id(id: int, image=True):
    """Checks if a given id is valid as it is assumed. For example, is a given id expectedly an
    image_id or not? Is the id expectedly a map_feature_id or not?

    :param id: The ID passed
    :type id: int

    :param image: Is the passed id an image_id?
    :type image: bool

    '''
    :raises InvalidOptionError: Raised when invalid arguments are passed
    '''

    :return: None
    :rtype: None
    """

    # Send a request to the specified end point, and check if an error is received
    error_check = 'error' in EntityAdapter().fetch_image(image_id=id, fields=[])

    # IF image == False, and error_check == True, this becomes True
    # IF image == True, and error_check == False, this becomes True    
    if not (image ^ error_check):

        # Raises an exception of InvalidOptionError
        raise InvalidOptionError(
            param='id',
            value=f'Id: {id}, image: {image}',
            options=['Id is image_id AND image is True', 'key is map_feature_id AND'
                'image is False']
            )
