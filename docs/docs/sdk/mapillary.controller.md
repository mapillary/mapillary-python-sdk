---
sidebar_position: 3
---

# mapillary.controller package
 
 ## Submodules
 
 ## mapillary.controller.detection module
 
 ### mapillary.controllers.detection
 
 This module implements the detection based business logic functionalities of the Mapillary
 Python SDK.
 
 For more information, please check out [https://www.mapillary.com/developer/api-documentation/](https://www.mapillary.com/developer/api-documentation/)
 
 
 * Copyright: (c) 2021 Facebook
 
 
 * License: MIT LICENSE
 
 
 ### mapillary.controller.detection.get_image_detections_controller(image_id: Union[str, int], fields: Optional[list] = None)
 Get image detections with given (image) key
 
 
 * **Parameters**
 
     
     * **image_id** (*str*) – The image id
 
 
     * **fields** (*list*) – The fields possible for the detection endpoint. Please see
     [https://www.mapillary.com/developer/api-documentation](https://www.mapillary.com/developer/api-documentation) for more information
 
 
 
 * **Returns**
 
     GeoJSON
 
 
 
 * **Return type**
 
     dict
 
 
 
 ### mapillary.controller.detection.get_map_feature_detections_controller(map_feature_id: Union[str, int], fields: Optional[list] = None)
 Get image detections with given (map feature) key
 
 
 * **Parameters**
 
     
     * **map_feature_id** (*str*) – The map feature id
 
 
     * **fields** (*list*) – The fields possible for the detection endpoint. Please see
     [https://www.mapillary.com/developer/api-documentation](https://www.mapillary.com/developer/api-documentation) for more information
 
 
 
 * **Returns**
 
     GeoJSON
 
 
 
 * **Return type**
 
     dict
 
 
 ## mapillary.controller.feature module
 
 ### mapillary.controllers.feature
 
 This module implements the feature extraction business logic functionalities of the Mapillary
 Python SDK.
 
 For more information, please check out [https://www.mapillary.com/developer/api-documentation/](https://www.mapillary.com/developer/api-documentation/)
 
 
 * Copyright: (c) 2021 Facebook
 
 
 * License: MIT LICENSE
 
 
 ### mapillary.controller.feature.get_feature_from_key_controller(key: int, fields: list)
 A controller for getting properties of a certain image given the image key and
 the list of fields/properties to be returned
 
 
 * **Parameters**
 
     
     * **key** (*int*) – The image key
 
 
     * **fields** (*list*) – List of possible fields
 
 
 
 * **Returns**
 
     The requested feature properties in GeoJSON format
 
 
 
 * **Return type**
 
     str
 
 
 
 ### mapillary.controller.feature.get_map_features_in_bbox_controller(bbox: dict, filter_values: list, filters: dict, layer: str = 'points')
 For extracting either map feature points or traffic signs within a bounding box
 
 
 * **Parameters**
 
     
     * **bbox** (*dict*) – Bounding box coordinates as argument
 
 
     * **layer** (*str*) – ‘points’ or ‘traffic_signs’
 
 
     * **filter_values** (*list*) – a list of filter values supported by the API.
 
 
     * **filters** (*dict*) – Chronological filters
 
 
 
 * **Returns**
 
     GeoJSON
 
 
 
 * **Return type**
 
     str
 
 
 ## mapillary.controller.image module
 
 ### mapillary.controllers.image
 
 This module implements the image filtering and analysis business logic functionalities of the
 Mapillary Python SDK.
 
 For more information, please check out [https://www.mapillary.com/developer/api-documentation/](https://www.mapillary.com/developer/api-documentation/)
 
 
 * Copyright: (c) 2021 Facebook
 
 
 * License: MIT LICENSE
 
 
 ### mapillary.controller.image.geojson_features_controller(geojson: dict, is_image: bool = True, filters: Optional[dict] = None)
 For extracting images that lie within a GeoJSON and merges the results of the found
 GeoJSON(s) into a single object - by merging all the features into one feature list.
 
 
 * **Parameters**
 
     
     * **geojson** (*dict*) – The geojson to act as the query extent
 
 
     * **is_image** (*bool*) – Is the feature extraction for images? True for images, False for map features
     Defaults to True
 
 
     * **filters** (*dict** (**kwargs**)*) – Different filters that may be applied to the output, defaults to {}
 
 
     * **filters.zoom** (*int*) – The zoom level to obtain vector tiles for, defaults to 14
 
 
     * **filters.max_captured_at** (*str*) – The max date. Format from ‘YYYY’, to ‘YYYY-MM-DDTHH:MM:SS’
 
 
     * **filters.min_captured_at** (*str*) – The min date. Format from ‘YYYY’, to ‘YYYY-MM-DDTHH:MM:SS’
 
 
     * **filters.image_type** (*str*) – The tile image_type to be obtained, either as ‘flat’, ‘pano’
     (panoramic), or ‘all’. See [https://www.mapillary.com/developer/api-documentation/](https://www.mapillary.com/developer/api-documentation/) under
     ‘image_type Tiles’ for more information
 
 
     * **filters.compass_angle** (*int*) – The compass angle of the image
 
 
     * **filters.sequence_id** (*str*) – ID of the sequence this image belongs to
 
 
     * **filters.organization_id** (*str*) – ID of the organization this image belongs to. It can be absent
 
 
     * **filters.layer** (*str*) – The specified image layer, either ‘overview’, ‘sequence’, ‘image’
     if is_image is True, defaults to ‘image’
 
 
     * **filters.feature_type** (*str*) – The specified map features, either ‘point’ or ‘traffic_signs’
     if is_image is False, defaults to ‘point’
 
 
 
 * **Raises**
 
     **InvalidKwargError** – Raised when a function is called with the invalid keyword argument(s)
     that do not belong to the requested API end call
 
 
 
 * **Returns**
 
     A feature collection as a GeoJSON
 
 
 
 * **Return type**
 
     dict
 
 
 
 ### mapillary.controller.image.get_image_close_to_controller(longitude: float, latitude: float, kwargs: dict)
 Extracting the GeoJSON for the image data near the [longitude, latitude] coordinates
 
 
 * **Parameters**
 
     
     * **kwargs** (*dict*) – The kwargs for the filter
 
 
     * **longitude** (*float*) – The longitude
 
 
     * **latitude** (*float*) – The latitude
 
 
     * **kwargs.zoom** (*int*) – The zoom level of the tiles to obtain, defaults to 14
 
 
     * **kwargs.min_captured_at** (*str*) – The minimum date to filter till
 
 
     * **kwargs.max_captured_at** (*str*) – The maximum date to filter upto
 
 
     * **kwargs.image_type** (*str*) – Either ‘pano’, ‘flat’ or ‘all’
 
 
     * **kwargs.organization_id** (*str*) – The organization to retrieve the data for
 
 
     * **kwargs.radius** (*float*) – The radius that the geometry points will lie in
 
 
 
 * **Returns**
 
     GeoJSON
 
 
 
 * **Return type**
 
     dict
 
 
 
 ### mapillary.controller.image.get_image_from_key_controller(key: int, fields: list)
 A controller for getting properties of a certain image given the image key and
 the list of fields/properties to be returned
 
 
 * **Parameters**
 
     
     * **key** (*int*) – The image key
 
 
     * **fields** (*list*) – The list of fields to be returned
 
 
 
 * **Returns**
 
     The requested image properties in GeoJSON format
 
 
 
 * **Return type**
 
     str
 
 
 
 ### mapillary.controller.image.get_image_looking_at_controller(looker: dict, at: dict, filters: dict)
 Extracting the GeoJSON for the image data from a ‘looker’ and ‘at’ coordinate view
 
 
 * **Parameters**
 
     
     * **filters** (*dict*) – Filters to pass the data through
 
 
     * **looker** (*dict*) – The dictionary of coordinates of the position of the looking from
     coordinates. Format:
 
     ```
     >>> {
     >>>     'lng': 'longitude',
     >>>     'lat': 'latitude'
     >>> }
     ```
 
 
 
     * **at** (*dict*) – The dict of coordinates of the position of the looking at
     coordinates. Format:
 
     ```
     >>> {
     >>>     'lng': 'longitude',
     >>>     'lat': 'latitude'
     >>> }
     ```
 
 
 
     * **filters.min_captured_at** (*str*) – The minimum date to filter till
 
 
     * **filters.max_captured_at** (*str*) – The maximum date to filter upto
 
 
     * **filters.radius** (*float*) – The radius that the geometry points will lie in
 
 
     * **filters.image_type** (*str*) – Either ‘pano’, ‘flat’ or ‘all’
 
 
     * **filters.organization_id** (*str*) – The organization to retrieve the data for
 
 
 
 * **Returns**
 
     GeoJSON
 
 
 
 * **Return type**
 
     dict
 
 
 
 ### mapillary.controller.image.get_image_thumbnail_controller(image_id: str, resolution: int)
 This controller holds the business logic for retrieving
 an image thumbnail with a specific resolution (256, 1024, or 2048)
 using an image ID/key
 
 
 * **Parameters**
 
     
     * **image_id** (*str*) – Image key as the argument
 
 
     * **resolution** (*int*) – Option for the thumbnail size, with available resolutions:
     256, 1024, and 2048
 
 
 
 * **Returns**
 
     A URL for the thumbnail
 
 
 
 * **Return type**
 
     str
 
 
 
 ### mapillary.controller.image.get_images_in_bbox_controller(bounding_box: dict, layer: str, zoom: int, filters: dict)
 For getting a complete list of images that lie within a bounding box,
 that can be filtered via the filters argument
 
 
 * **Parameters**
 
     
     * **bounding_box** (*dict*) – A bounding box representation
     Example:
 
     ```
     >>> {
     ...     'west': 'BOUNDARY_FROM_WEST',
     ...     'south': 'BOUNDARY_FROM_SOUTH',
     ...     'east': 'BOUNDARY_FROM_EAST',
     ...     'north': 'BOUNDARY_FROM_NORTH'
     ... }
     ```
 
 
 
     * **zoom** – The zoom level
 
 
     * **zoom** – int
 
 
     * **layer** (*str*) – Either ‘image’, ‘sequence’, ‘overview’
 
 
     * **filters** (*dict*) – Filters to pass the data through
 
 
     * **filters.max_captured_at** (*str*) – The max date that can be filtered upto
 
 
     * **filters.min_captured_at** (*str*) – The min date that can be filtered from
 
 
     * **filters.image_type** (*str*) – Either ‘pano’, ‘flat’ or ‘all’
 
 
     * **filters.compass_angle** (*float*) – 
 
 
     * **filters.organization_id** (*int*) – 
 
 
     * **filters.sequence_id** (*str*) – 
 
 
 
 * **Raises**
 
     **InvalidKwargError** – Raised when a function is called with the invalid keyword argument(s)
     that do not belong to the requested API end call
 
 
 
 * **Returns**
 
     GeoJSON
 
 
 
 * **Return type**
 
     str
 
 
 Reference,
 
 
 * [https://www.mapillary.com/developer/api-documentation/#coverage-tiles](https://www.mapillary.com/developer/api-documentation/#coverage-tiles)
 
 
 ### mapillary.controller.image.shape_features_controller(shape, is_image: bool = True, filters: Optional[dict] = None)
 For extracting images that lie within a shape, merging the results of the found features
 into a single object - by merging all the features into one list in a feature collection.
 
 The shape format is as follows:
 
 ```
 >>> {
 ...     "type": "FeatureCollection",
 ...     "features": [
 ...         {
 ...             "type": "Feature",
 ...             "properties": {},
 ...             "geometry": {
 ...                 "type": "Polygon",
 ...                 "coordinates": [
 ...                     [
 ...                        [
 ...                              7.2564697265625,
 ...                             43.69716905314008
 ...                         ],
 ...                         ...
 ...                     ]
 ...                 ]
 ...             }
 ...         }
 ...     ]
 ... }
 ```
 
 
 * **Parameters**
 
     
     * **shape** (*dict*) – A shape that describes features, formatted as a geojson
 
 
     * **is_image** (*bool*) – Is the feature extraction for images? True for images, False for map features
     Defaults to True
 
 
     * **filters** (*dict** (**kwargs**)*) – Different filters that may be applied to the output, defaults to {}
 
 
     * **filters.max_captured_at** (*str*) – The max date. Format from ‘YYYY’, to ‘YYYY-MM-DDTHH:MM:SS’
 
 
     * **filters.min_captured_at** (*str*) – The min date. Format from ‘YYYY’, to ‘YYYY-MM-DDTHH:MM:SS’
 
 
     * **filters.image_type** (*str*) – The tile image_type to be obtained, either as ‘flat’, ‘pano’
     (panoramic), or ‘all’. See [https://www.mapillary.com/developer/api-documentation/](https://www.mapillary.com/developer/api-documentation/) under
     ‘image_type Tiles’ for more information
 
 
     * **filters.compass_angle** (*int*) – The compass angle of the image
 
 
     * **filters.sequence_id** (*str*) – ID of the sequence this image belongs to
 
 
     * **filters.organization_id** (*str*) – ID of the organization this image belongs to. It can be absent
 
 
     * **filters.layer** (*str*) – The specified image layer, either ‘overview’, ‘sequence’, ‘image’
     if is_image is True, defaults to ‘image’
 
 
     * **filters.feature_type** (*str*) – The specified map features, either ‘point’ or ‘traffic_signs’
     if is_image is False, defaults to ‘point’
 
 
 
 * **Raises**
 
     **InvalidKwargError** – Raised when a function is called with the invalid keyword argument(s)
     that do not belong to the requested API end call
 
 
 
 * **Returns**
 
     A feature collection as a GeoJSON
 
 
 
 * **Return type**
 
     dict
 
 
 ## mapillary.controller.save module
 
 ### mapillary.controllers.save
 
 This module implements the saving business logic functionalities of the Mapillary Python SDK.
 
 For more information, please check out [https://www.mapillary.com/developer/api-documentation/](https://www.mapillary.com/developer/api-documentation/)
 
 
 * Copyright: (c) 2021 Facebook
 
 
 * License: MIT LICENSE
 
 
 ### mapillary.controller.save.save_as_csv_controller(data: str, path: str, file_name: str)
 Save data as CSV to given file path
 
 
 * **Parameters**
 
     
     * **data** (*str*) – The data to save as CSV
 
 
     * **path** (*str*) – The path to save to
 
 
     * **file_name** (*str*) – The file name to save as
 
 
 
 * **Returns**
 
     None
 
 
 
 * **Return type**
 
     None
 
 
 
 ### mapillary.controller.save.save_as_geojson_controller(data: str, path: str, file_name: str)
 Save data as GeoJSON to given file path
 
 
 * **Parameters**
 
     
     * **data** (*str*) – The data to save as GeoJSON
 
 
     * **path** (*str*) – The path to save to
 
 
     * **file_name** (*str*) – The file name to save as
 
 
 
 * **Returns**
 
     None
 
 
 
 * **Return type**
 
     None
 
 
 ## Module contents
 
 ### mapillary.controller.__init__
 
 This package contains all the business logic implementations of interfaces used within the
 Mapillary Python SDK.
 
 
 * Copyright: (c) 2021 Facebook
 
 
 * License: MIT LICENSE
