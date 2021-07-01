# -*- coding: utf-8 -*-

"""
mapillary.utils.filter

This module contains the filter utilies high level filtering logic
"""

from utils.time import date_to_unix_epoch


def filter_max_date(data, max_date):
    max_date = date_to_unix_epoch(max_date)
    return [
        feature
        for feature in data["features"]
        if feature["properties"]["captured_at"] <= max_date
    ]


def filter_min_date(data, min_date):
    min_date = date_to_unix_epoch(min_date)
    return [
        feature
        for feature in data["features"]
        if feature["properties"]["captured_at"] >= min_date
    ]


def filter_params(data, filter_values, properties):
    return [
        feature
        for feature in data["features"]
        if feature["properties"][properties] in filter_values
    ]
