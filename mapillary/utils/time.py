# -*- coding: utf-8 -*-

"""
mapillary.utils.time

This module contains the time utilies for the UNIX epoch
milliseconds, the time and the date range, and the date
filtering logic
"""

# Package imports
import datetime
import re

# Local imports
from models.exceptions import InvalidDateError


def date_to_unix_epoch(date: str):
    """A utility function that converts the given date
    into its UNIX epoch timestamp equivalent. Accepts the following formats,

    1. YYYY-MM-DDTHH:MM:SS
    2. YYYY-MM-DDTHH:MM
    3. YYYY-MM-DDTHH
    4. YYYY-MM-DD
    5. YYYY-MM
    6. YYYY
    7. * (returns current timestamp)

    :param date: The date to get the UNIX timestamp epoch of
    :type date: str

    Usage::
        >>> from utils.time_utils import date_to_unix_epoch
        >>> date_to_unix_epoch('2020-10-23')
        "1603393200"
    """

    # ! REFACTOR/TODO: This function can be heavily refactored

    if date == "*":

        # Returns current timestamp
        return int(datetime.datetime.now().timestamp())

    # YYYY-MM-DDTHH:MM:SS
    match = re.compile(r"[0-9]+-[0-9]+-[0-9]+T[0-9]+:[0-9]+:[0-9]+").match(date)

    if match is not None:

        # Splitting YYYY-MM-DDTHH:MM:SS into [YYYY-MM-DD, HH:MM:SS]
        split_result = match.group().split("T")

        # Splitting YYYY-MM-DD into [YYYY, MM, DD]
        year_month_day = split_result[0].split("-")

        # Beaking HH:MM:SS into [HH, MM, SS]
        hour_minute_second = split_result[1].split(":")

        if (
            int(year_month_day[0]) > datetime.datetime.now().year
            or int(year_month_day[1]) > 12
            or int(year_month_day[2]) > 31
            or int(hour_minute_second[0]) > 23
            or int(hour_minute_second[1]) > 59
            or int(hour_minute_second[2]) > 59
        ):
            raise InvalidDateError(date)

        return int(
            datetime.datetime(
                int(year_month_day[0]),
                int(year_month_day[1]),
                int(year_month_day[2]),
                int(hour_minute_second[0]),
                int(hour_minute_second[1]),
                int(hour_minute_second[2]),
            ).timestamp()
        )

    # YYYY-MM-DDTHH:MM
    match = re.compile(r"[0-9]+-[0-9]+-[0-9]+T[0-9]+:[0-9]+").match(date)

    if match is not None:
        # Splitting YYYY-MM-DDTHH:MM into [YYYY-MM-DD, HH:MM]
        split_result = match.group().split("T")

        # Splitting YYYY-MM-DD into [YYYY, MM, DD]
        year_month_day = split_result[0].split("-")

        # Beaking HH:MM into [HH, MM]
        hour_minute_second = split_result[1].split(":")

        if (
            int(year_month_day[0]) > datetime.datetime.now().year
            or int(year_month_day[1]) > 12
            or int(year_month_day[2]) > 31
            or int(hour_minute_second[0]) > 23
            or int(hour_minute_second[1]) > 59
        ):
            raise InvalidDateError(date)

        return int(
            datetime.datetime(
                int(year_month_day[0]),
                int(year_month_day[1]),
                int(year_month_day[2]),
                int(hour_minute_second[0]),
                int(hour_minute_second[1]),
                00,
            ).timestamp()
        )

    # YYYY-MM-DDTHH
    match = re.compile(r"[0-9]+-[0-9]+-[0-9]+T[0-9]+").match(date)

    if match is not None:

        # Splitting YYYY-MM-DDTHH into [YYYY-MM-DD, HH]
        split_result = match.group().split("T")

        # Splitting YYYY-MM-DD into [YYYY, MM, DD]
        year_month_day = split_result[0].split("-")

        # Splitting HH into [HH]
        hour_minute_second = split_result[1].split(":")

        if (
            int(year_month_day[0]) > datetime.datetime.now().year
            or int(year_month_day[1]) > 12
            or int(year_month_day[2]) > 31
            or int(hour_minute_second[0]) > 23
        ):
            raise InvalidDateError(date)

        return int(
            datetime.datetime(
                int(year_month_day[0]),
                int(year_month_day[1]),
                int(year_month_day[2]),
                int(hour_minute_second[0]),
                00,
                00,
            ).timestamp()
        )

    # YYYY-MM-DD
    match = re.compile(r"[0-9]+-[0-9]+-[0-9]+").match(date)

    if match is not None:

        # Splitting YYYY-MM-DD into [YYYY, MM, DD]
        year_month_day = match.group().split("-")

        if (
            int(year_month_day[0]) > datetime.datetime.now().year
            or int(year_month_day[1]) > 12
            or int(year_month_day[2]) > 31
        ):
            raise InvalidDateError(date)

        return int(
            datetime.datetime(
                int(year_month_day[0]),
                int(year_month_day[1]),
                int(year_month_day[2]),
                00,
                00,
                00,
            ).timestamp()
        )

    # YYYY-MM
    match = re.compile(r"[0-9]+-[0-9]+").match(date)

    if match is not None:

        # Splitting YYYY-MM into [YYYY, MM]
        year_month_day = match.group().split("-")

        if (
            int(year_month_day[0]) > datetime.datetime.now().year
            or int(year_month_day[1]) > 12
        ):
            raise InvalidDateError(date)

        return int(
            datetime.datetime(
                int(year_month_day[0]),
                int(year_month_day[1]),
                00,
                00,
                00,
                00,
            ).timestamp()
        )

    # YYYY
    match = re.compile(r"[0-9]+").match(date)

    if match is not None:

        if int(date) > datetime.datetime.now().year:
            raise InvalidDateError(date)

        return int(
            datetime.datetime(
                int(date),
                00,
                00,
                00,
                00,
                00,
            ).timestamp()
        )
