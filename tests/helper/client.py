# Copyright (c) Facebook, Inc. and its affiliates. (http://www.facebook.com)
# -*- coding: utf-8 -*-

"""
tests.helper.client
~~~~~~~~~~~~~~~~~~~

For pulling in data for test purposes from the Mapillary APIv4. Some higher level requirements
use a geojson or a bbox as the query extent for further testing. This file serves to be an
easy way of pulling in data from endpoints through an easy CLI instead of writing Python
code as 1 offs for getting the data and parsing it.

Contributions welcome!

:copyright: (c) 2021 Facebook
:license: MIT LICENSE
"""

# Local imports
import fetch

# Package imports
import inspect
import logging
import json
import sys
import os

colors = {
    "HEADER": "\033[95m",
    "OKBLUE": "\033[94m",
    "OKCYAN": "\033[96m",
    "OKGREEN": "\033[92m",
    "WARNING": "\033[93m",
    "FAIL": "\033[91m",
    "ENDC": "\033[0m",
    "BOLD": "\033[1m",
    "UNDERLINE": "\033[4m",
}


def list_fetched_functions(fetched_functions: list) -> None:
    """Simply lists out the functions described in fetch.py along with their DocString

    :param fetched_functions: List of function names along with their references in a tuple set
    :type fetched_functions: list

    :return: Nothing to return
    :rtype: None
    """

    # Through each tuple in the format (name, reference)
    for index, function in enumerate(fetched_functions):

        # Print out ...
        print(
            # ... an index for the function, then the name of the function in cyan color ...
            f"{index + 1}. {colors['OKCYAN']}{function[0]}{colors['ENDC']} "
            # ... then print the docstring as well
            f"- {function[1].__doc__}"
        )


def save_as_geojson(data: dict) -> None:
    """Saves the resulting geojson dictionary in a file tagged .geojson

    :param data: The data to save
    :type data: dict

    :return: Nothing to return
    :rtype: None
    """

    # TODO: Test if this works perfectly fine in Windows, since it uses the `os` package

    # Save the file at the given path, create it if it does not exist
    with open(
        f'{os.path.abspath(".")}/data/{sys.argv[2]}.geojson', mode="w"
    ) as geojson_file:

        # Save the dictionary as a json in a clean formatted way
        json.dump(data, geojson_file, sort_keys=True, indent=4)


def main():
    """Main logic for the CLI"""

    # Getting the list of functions and their references from fetch.py
    fetched_functions = inspect.getmembers(fetch, inspect.isfunction)

    # If there are insufficient arguments
    if len(sys.argv) < 3:

        # Log an error ...
        logging.error(
            # ... indicating the source of the error ...
            " - client.py\n"
            # ... the reason for the error ...
            f"{colors['FAIL']}Invalid format!{colors['ENDC']}\n"
            # ... giving the user a format for the colors ...
            f"Try: python client.py {colors['BOLD']}'MLY|XXX'{colors['ENDC']} "
            # ... format of the function called
            f"{colors['OKCYAN']}fetch_function_here{colors['ENDC']}\n"
        )

        # Finally, list the functions for the user
        list_fetched_functions(fetched_functions=fetched_functions)

    else:

        # Getting the access token
        access_token = str(sys.argv[1])

        # result output variable
        result: dict = {}

        # Going through each tuple of the format (func_name, func_reference)
        for function in fetched_functions:

            # If the function named is what is asked through the args
            if function[0] == str(sys.argv[2]):

                # Get the resulting output from the reference
                result = function[1](access_token=access_token)

        # If the results ends up empty
        if result == {}:

            # Log an error ...
            logging.error(
                # ... indicating the source of the error ...
                " - client.py\n"
                # ... the reason for the error
                f"{colors['FAIL']}Unrecognized function call!{colors['ENDC']}\n"
            )

            # Finally, list the functions for the user
            list_fetched_functions(fetched_functions=fetched_functions)

        # Saving the data
        save_as_geojson(result)


if __name__ == "__main__":
    main()
