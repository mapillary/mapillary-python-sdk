---
sidebar_position: 5
---

# mapillary.models.api package
 
 ## Submodules
 
 ## mapillary.models.api.entities module
 
 ### mapillary.models.api.entities
 
 This module contains the Adapter design for the Entities API of Mapillary API v4.
 
 For more information, please check out [https://www.mapillary.com/developer/api-documentation/](https://www.mapillary.com/developer/api-documentation/).
 
 
 * Copyright: (c) 2021 Facebook
 
 
 * License: MIT LICENSE
 
 
 ### class mapillary.models.api.entities.EntityAdapter()
 Bases: `object`
 
 Adapter model for dealing with the Entity API, through the DRY principle. The EntityAdapter
 class can be instantiated in the controller modules, providing an abstraction layer that uses
 the Client class, endpoints provided by the API v4 under /config/api/entities.py.
 
 It performs parsing, handling of layers, properties, and fields to make it easier to
 write higher level logic for extracing information, and lets developers to focus only
 on writing the high level business logic without having to repeat the process of parsing
 and using libraries such as mercantile, ast, and others to only then care about the
 inputs and the outputs
 
 Usage:
 
 ```
 >>> import mapillary
 >>> from mapillary.models.api.entities import EntityAdapter
 >>> EntityAdapter().fetch_image(image_id='IMAGE_ID', fields=[
 ...     'altitude', 'atomic_scale', 'geometry', 'width'
 ... ])
 >>> EntityAdapter().fetch_map_feature(map_feature_id='MAP_FEATURE_ID', fields=[
 ...         'first_seen_at', 'last_seen_at', 'geometry'
 ...     ])
 ```
 
 
 #### fetch_detections(identity: int, id_type: bool = True, fields: Optional[list] = None)
 Fetches detections depending on the id, detections for either map_features or
 images and the fields provided
 
 
 * **Parameters**
 
     
     * **identity** (*int*) – The id to extract for
 
 
     * **id_type** (*bool*) – Either True(id is for image), or False(id is for map_feature),
     defaults to True
 
 
     * **fields** (*list*) – The fields to extract properties for, defaults to []
 
 
 
 * **Returns**
 
     The fetched GeoJSON
 
 
 
 * **Return type**
 
     dict
 
 
 
 #### fetch_image(image_id: Union[int, str], fields: Optional[list] = None)
 Fetches images depending on the image_id and the fields provided
 
 
 * **Parameters**
 
     
     * **image_id** (*int*) – The image_id to extract for
 
 
     * **fields** (*list*) – The fields to extract properties for, defaults to []
 
 
 
 * **Returns**
 
     The fetched GeoJSON
 
 
 
 * **Return type**
 
     dict
 
 
 
 #### fetch_map_feature(map_feature_id: Union[int, str], fields: Optional[list] = None)
 Fetches map features depending on the map_feature_id and the fields provided
 
 
 * **Parameters**
 
     
     * **map_feature_id** (*int*) – The map_feature_id to extract for
 
 
     * **fields** (*list*) – The fields to extract properties for, defaults to []
 
 
 
 * **Returns**
 
     The fetched GeoJSON
 
 
 
 * **Return type**
 
     dict
 
 
 
 #### is_image_id(identity: int, fields: Optional[list] = None)
 Determines whether the given id is an image_id or a map_feature_id
 
 
 * **Parameters**
 
     
     * **identity** (*int*) – The ID given to test
 
 
     * **fields** (*list*) – The fields to extract properties for, defaults to []
 
 
 
 * **Returns**
 
     True if id is image, else False
 
 
 
 * **Return type**
 
     bool
 
 
 ## mapillary.models.api.vector_tiles module
 
 ### mapillary.models.api.vector_tiles
 
 This module contains the adapter design for the Vector Tiles API of Mapillary API v4, Vector tiles
 provide an easy way to visualize vast amounts of data. Vector tiles support filtering and querying
 rendered features. Mapillary vector tiles follow the Mapbox tile specification.
 
 For more information, please check out [https://www.mapillary.com/developer/api-documentation/](https://www.mapillary.com/developer/api-documentation/).
 
 
 * Copyright: (c) 2021 Facebook
 
 
 * License: MIT LICENSE
 
 
 ### class mapillary.models.api.vector_tiles.VectorTilesAdapter()
 Bases: `object`
 
 Adapter model for dealing with the VectorTiles API, through the DRY principle. The
 VectorTilesAdapter class can be instantiated in the controller modules, providing an
 abstraction layer that uses the Client class, endpoints provided by the API v4 under
 /config/api/vector_tiles.py.
 
 It performs parsing, handling of layers, properties, and fields to make it easier to
 write higher level logic for extracing information, and lets developers to focus only
 on writing the high level business logic without having to repeat the process of parsing
 and using libraries such as mercantile, ‘vt2geojson’ and others, caring only about
 inputs/outputs
 
 Usage:
 
 ```
 >>> import mapillary
 >>> from mapillary.models.api.vector_tiles import VectorTilesAdapter
 >>> latitude, longitude = 30, 31
 >>> VectorTilesAdapter().fetch_layer(layer="image", zoom=14, longitude=longitude,
 ...     latitude=latitude,
 ... )
 >>> VectorTilesAdapter().fetch_layer(layer="sequence", zoom=10, longitude=longitude,
 ...     latitude=latitude,
 ... )
 >>> VectorTilesAdapter().fetch_layer(layer="overview", zoom=3, longitude=longitude,
 ...     latitude=latitude,
 ... )
 ```
 
 
 #### fetch_computed_layer(layer: str, zoom: int, longitude: float, latitude: float)
 Same as fetch_layer, but gets in return computed tiles only.
 Depends on the layer, zoom level, longitude and the latitude specifications
 
 
 * **Parameters**
 
     
     * **layer** (*str*) – Either ‘overview’, ‘sequence’, ‘image’
 
 
     * **zoom** (*int*) – The zoom level, [0, 14], inclusive
 
 
     * **longitude** (*float*) – The longitude of the coordinates
 
 
     * **latitude** (*float*) – The latitude of the coordinates
 
 
 
 * **Returns**
 
     A GeoJSON for that specific layer and the specified zoom level
 
 
 
 * **Return type**
 
     dict
 
 
 
 #### fetch_features(feature_type: str, zoom: int, longitude: float, latitude: float)
 Fetches specified features from the coordinates with the appropriate zoom level
 
 
 * **Parameters**
 
     
     * **feature_type** (*str*) – Either point, or tiles
 
 
     * **zoom** (*int*) – The zoom level
 
 
     * **longitude** (*float*) – The longitude of the coordinates
 
 
     * **latitude** (*float*) – The latitude of the coordinates
 
 
 
 * **Returns**
 
     A GeoJSON for that specific layer and the specified zoom level
 
 
 
 * **Return type**
 
     dict
 
 
 
 #### fetch_layer(layer: str, longitude: float, latitude: float, zoom: int = 14)
 Fetches an image tile layer depending on the coordinates, and the layer selected
 along with the zoom level
 
 
 * **Parameters**
 
     
     * **layer** (*str*) – Either ‘overview’, ‘sequence’, ‘image’
 
 
     * **longitude** (*float*) – The longitude of the coordinates
 
 
     * **latitude** (*float*) – The latitude of the coordinates
 
 
     * **zoom** (*int*) – The zoom level, [0, 14], inclusive
 
 
 
 * **Returns**
 
     A GeoJSON for that specific layer and the specified zoom level
 
 
 
 * **Return type**
 
     dict
 
 
 
 #### fetch_layers(coordinates: list[list], layer: str = 'image', zoom: int = 14, is_computed: bool = False)
 Fetches multiple vector tiles based on a list of multiple coordinates in a listed format
 
 
 * **Parameters**
 
     
     * **coordinates** (*"list**[**list**]**"*) – A list of lists of coordinates to get the vector tiles for
 
 
     * **layer** (*str*) – Either “overview”, “sequence”, “image”, “traffic_sign”, or “map_feature”,
     defaults to “image”
 
 
     * **zoom** (*int*) – the zoom level [0, 14], inclusive. Defaults to 14
 
 
     * **is_computed** (*bool*) – Will to be fetched layers be computed? Defaults to False
 
 
 
 * **Returns**
 
     A geojson with merged features from all unique vector tiles
 
 
 
 * **Return type**
 
     dict
 
 
 
 #### fetch_map_features(coordinates: list[list], feature_type: str, zoom: int = 14)
 Fetches map features based on a list Polygon object
 
 
 * **Parameters**
 
     
     * **coordinates** (*"list**[**list**]**"*) – A list of lists of coordinates to get the map features for
 
 
     * **feature_type** (*str*) – Either “point”, “traffic_signs”, defaults to “point”
 
 
     * **zoom** (*int*) – the zoom level [0, 14], inclusive. Defaults to 14
 
 
 
 * **Returns**
 
     A geojson with merged features from all unique vector tiles
 
 
 
 * **Return type**
 
     dict
 
 
 ## Module contents
 
 ### mapillary.models.api.__init__
 
 This package contains the class adaptors of the API logic within the Mapillary Python SDK.
 
 
 * Copyright: (c) 2021 Facebook
 
 
 * License: MIT LICENSE
