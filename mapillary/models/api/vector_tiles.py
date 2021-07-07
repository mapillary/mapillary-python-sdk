# -*- coding: utf-8 -*-

"""
mapillary.models.api.vector_tiles

This module contains the Adapter design for the Vector Tiles API of Mapillary APIv4, Vector tiles
provide an easy way to visualize vast amounts of data. Mapillary APIs are heavily based on vector
tiles to provide the developers with flexibility to programmatically interact with the data they
contain in custom ways. Vector tiles support filtering and querying rendered features. Mapillary
vector tiles follow the Mapbox tile specification.
"""

# Package imports
from vt2geojson.tools import vt_bytes_to_geojson
import mercantile

# Local imports
from models.exceptions import OutOfBoundZoomError, InvalidKwargError
from models.client import Client

# # Config
from config.api.vector_tiles import VectorTiles


class VectorTilesAdapter(object):
    def __init__(self):
        self.client = Client()
        self.__min_zoom = 0
        self.__max_zoom = 14

    def fetch_layer(self, layer: str, zoom: int, longitude: float, latitude: float):

        self.__zoom_range_check(layer=layer, zoom=zoom)

        return self.__preprocess_layer(
            layer=layer, longitude=longitude, latitude=latitude, zoom=zoom
        )

    def fetch_computed_layer(
        self, layer: str, zoom: int, longitude: float, latitude: float
    ):

        self.__zoom_range_check(layer=layer, zoom=zoom)

        return self.__preprocess_computed_layer(
            layer=layer, longitude=longitude, latitude=latitude, zoom=zoom
        )

    def fetch_features(
        self, feature_type: str, zoom: int, longitude: float, latitude: float
    ):

        self.__zoom_range_check(layer="map", zoom=zoom)

        return self.__preprocess_features(
            feature_type=feature_type, longitude=longitude, latitude=latitude, zoom=zoom
        )

    def __zoom_range_check(self, layer: str, zoom: int):

        if zoom < self.__min_zoom or zoom > self.__max_zoom:

            raise OutOfBoundZoomError(
                zoom, [_ for _ in range(self.__min_zoom, self.__max_zoom + 1)]
            )

        if layer == "overview":

            if zoom not in [_ for _ in range(self.__min_zoom, 5 + 1)]:
                raise OutOfBoundZoomError(
                    zoom, [_ for _ in range(self.__min_zoom, 5 + 1)]
                )

        elif layer == "sequence":

            if zoom not in [_ for _ in range(6, 14 + 1)]:
                raise OutOfBoundZoomError(zoom, [_ for _ in range(6, 14 + 1)])

        elif layer == "image" or layer == "map":

            if zoom != 14:
                raise OutOfBoundZoomError(zoom, [14])

        else:
            raise InvalidKwargError(
                func="__zoom_range_check",
                key="layer",
                value=layer,
                optional_keys=["overview", "sequence", "image"],
            )

    def __preprocess_layer(
        self, layer: str, longitude: float, latitude: float, zoom: int
    ):
        tile = mercantile.tile(longitude, latitude, zoom)

        if layer == "overview":
            url = VectorTiles.get_overview_layer(x=tile[0], y=tile[1], z=zoom)

        elif layer == "sequence":
            url = VectorTiles.get_sequence_layer(x=tile[0], y=tile[1], z=zoom)

        elif layer == "image":
            url = VectorTiles.get_image_layer(x=tile[0], y=tile[1], z=zoom)

        return vt_bytes_to_geojson(
            b_content=self.client.get(url), x=tile.x, y=tile.y, z=tile.z, layer=layer
        )

    def __preprocess_computed_layer(
        self, layer: str, longitude: float, latitude: float, zoom: int
    ):
        tile = mercantile.tile(longitude, latitude, zoom)

        if layer == "overview":
            url = VectorTiles.get_computed_overview_layer(x=tile[0], y=tile[1], z=zoom)

        elif layer == "sequence":
            url = VectorTiles.get_computed_sequence_layer(x=tile[0], y=tile[1], z=zoom)

        elif layer == "image":
            url = VectorTiles.get_computed_image_layer(x=tile[0], y=tile[1], z=zoom)

        return vt_bytes_to_geojson(
            b_content=self.client.get(url), x=tile.x, y=tile.y, z=tile.z, layer=layer
        )

    def __preprocess_features(self, feature_type, longitude, latitude, zoom):
        if feature_type != "point" and feature_type != "tiles":
            return

        tile = mercantile.tile(longitude, latitude, zoom)

        if feature_type == "point":
            url = VectorTiles.get_map_feature_point(x=tile[0], y=tile[1], z=zoom)

        elif feature_type == "tiles":
            url = VectorTiles.get_map_feature_tiles(x=tile[0], y=tile[1], z=zoom)

        return vt_bytes_to_geojson(
            b_content=self.client.get(url),
            x=tile.x,
            y=tile.y,
            z=tile.z,
        )

    def __enter__(self):
        print("[VectorTilesAdapter] __enter__")

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print("[VectorTilesAdapter] __exit__")

    def __repr__(self):
        return "VectorTilesAdapter"

    def __str__(self):
        return "VectorTilesAdapter"
