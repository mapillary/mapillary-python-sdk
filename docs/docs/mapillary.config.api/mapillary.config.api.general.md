---
sidebar position: 3
---


### mapillary.config.api.general

This module contains the class implementation of the
general metadata functionalities for the API v4 of Mapillary.

For more information, please check out [https://www.mapillary.com/developer/api-documentation/](https://www.mapillary.com/developer/api-documentation/).


* Copyright: (c) 2021 Facebook


* License: MIT LICENSE


### class mapillary.config.api.general.General()
Bases: `object`

A general list of metadata API endpoints for API v4


#### static get_computed_image_type_tiles(x: float, y: float, z: float)
Computed image_type tiles


#### static get_image_type_tiles(x: float, y: float, z: float)
image_type tiles


#### static get_map_features_points_tiles(x: float, y: float, z: float)
Map features (points) tiles


#### static get_map_features_traffic_signs_tiles(x: float, y: float, z: float)
Map features (traffic signs) tiles


#### static get_tile_metadata()
Root endpoint for metadata


#### static get_vector_tiles()
Root endpoint for vector tiles
