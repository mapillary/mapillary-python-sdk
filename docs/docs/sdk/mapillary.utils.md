---
sidebar_position: 7
---

# mapillary.utils package
 
 ## Submodules
 
 ## mapillary.utils.extract module
 
 ### mapillary.utils.extract
 
 This module deals with extracting multiple fields nested within a GeoJSON packet.
 
 
 * Copyright: (c) 2021 Facebook
 
 
 * License: MIT LICENSE
 
 
 ### mapillary.utils.extract.extract_properties(geojson: dict, properties: list)
 Extracts specific properties from a complete GeoJSON
 
 
 * **Parameters**
 
     
     * **geojson** (*dict*) – GeoJSON object
 
 
     * **properties** (*list*) – A list of properties to extract
 
 
 
 * **Returns**
 
     The extracted fields as a dict
 
 
 
 * **Return type**
 
     dict
 
 
 Usage:
 
 ```
 >>> from utils.extract import extract_properties
 >>> extract_properties(geojson={"type":"FeatureCollection","features":[{"type":"Feature",
 ... "geometry":{"type":"Point","coordinates":[-80.12991070747375,25.787652114106322]},
 ... "properties":{"captured_at":1540386861135, "compass_angle":252.04260253906,"id":
 ... 1274987139570038,"is_pano":'False',"sequence_id":"Vf8Iwxx5SemxI7_b_7J5Kw"}},{"type":
 ... "Feature","geometry":{"type":"Point","coordinates":[-80.13223886489868,
 ... 25.78756517066695]}, "properties":{"captured_at":1422989164000,"compass_angle":
 ... 89.781,"id":169629268373019,"is_pano": "True","sequence_id":"dqjuprkOwUnmdEVt5gx-Iw"}}]}
 ... , properties=['id']) # id most likely exists
 ```
 
 ## mapillary.utils.filter module
 
 ### mapillary.utils.filter
 
 This module contains the filter utilies for high level filtering logic
 
 
 * Copyright: (c) 2021 Facebook
 
 
 * License: MIT LICENSE
 
 
 ### mapillary.utils.filter.by_look_at_feature(image: dict, look_at_feature: geojson.feature.Feature)
 Filter through the given image features and return only features with the look_at_feature
 
 
 * **Parameters**
 
     
     * **image** (*dict*) – The feature dictionary
 
 
     * **look_at_feature** (*A WGS84 GIS feature**, **TurfPy*) – Feature description
 
 
 
 * **Returns**
 
     Whether the given feature is looking at the look_at_features
 
 
 
 * **Return type**
 
     bool
 
 
 
 ### mapillary.utils.filter.compass_angle(data: list, angles: tuple = (0.0, 360.0))
 Filter out images that do not lie within compass angle range
 
 
 * **Parameters**
 
     
     * **data** (*list*) – The data to be filtered
 
 
     * **angles** – The compass angle range to filter through
 
 
 
 * **Returns**
 
     A feature list
 
 
 
 * **Return type**
 
     list
 
 
 
 ### mapillary.utils.filter.existed_at(data: list, existed_at: str)
 Whether the first_seen_at properly existed after a specified time period
 
 
 * **Parameters**
 
     
     * **data** (*list*) – The feature list
 
 
     * **existed_at** (*str*) – The UNIX timestamp
 
 
 
 * **Returns**
 
     The feature list
 
 
 
 * **Return type**
 
     list
 
 
 
 ### mapillary.utils.filter.existed_before(data: list, existed_before: str)
 Whether the first_seen_at properly existed before a specified time period
 
 
 * **Parameters**
 
     
     * **data** (*list*) – The feature list
 
 
     * **existed_before** (*str*) – The UNIX timestamp
 
 
 
 * **Returns**
 
     A feature list
 
 
 
 * **Return type**
 
     list
 
 
 
 ### mapillary.utils.filter.features_in_bounding_box(data: list, bbox: dict)
 Filter for extracting features only in a bounding box
 
 
 * **Parameters**
 
     
     * **data** (*list*) – the features list to be checked
 
 
     * **bbox** (*dict*) – Bounding box coordinates
 
     Example:
 
     ```
     >>> {
     ...     'west': 'BOUNDARY_FROM_WEST',
     ...     'south': 'BOUNDARY_FROM_SOUTH',
     ...     'east': 'BOUNDARY_FROM_EAST',
     ...     'north': 'BOUNDARY_FROM_NORTH'
     ... }
     ```
 
 
 
 
 * **Returns**
 
     Features that only exist within the bounding box selected for the given features list
     provided in the BBox functon
 
 
 
 * **Return type**
 
     list
 
 
 
 ### mapillary.utils.filter.filter_values(data: list, values: list, property: str = 'value')
 Filter the features based on the existence of a specified value
 in one of the property.
 
 *TODO*: Need documentation that lists the ‘values’, specifically, it refers to ‘value’
 *TODO*: under ‘Detection’, and ‘Map feature’, related to issue #65
 
 
 * **Parameters**
 
     
     * **data** (*dict*) – The data to be filtered
 
 
     * **values** (*list*) – A list of values to filter by
 
 
     * **property** (*str*) – The specific parameter to look into
 
 
 
 * **Returns**
 
     A feature list
 
 
 
 * **Return type**
 
     dict
 
 
 
 ### mapillary.utils.filter.haversine_dist(data: dict, radius: float, coords: list, unit: str = 'm')
 Returns features that are only in the radius specified using the Haversine distance, from
 the haversine package
 
 
 * **Parameters**
 
     
     * **data** (*dict*) – The data to be filtered
 
 
     * **radius** (*float*) – Radius for coordinates to fall into
 
 
     * **coords** (*list*) – The input coordinates (long, lat)
 
 
     * **unit** (*str*) – Either ‘ft’, ‘km’, ‘m’, ‘mi’, ‘nmi’, see here [https://pypi.org/project/haversine/](https://pypi.org/project/haversine/)
 
 
 
 * **Returns**
 
     A feature list
 
 
 
 * **Return type**
 
     list
 
 
 
 ### mapillary.utils.filter.hits_by_look_at(data: list, at: dict)
 Whether the given data have any feature that look at the at coordinates
 
 
 * **Parameters**
 
     
     * **data** (*list*) – List of features with an Image entity
 
 
     * **at** (*dict*) – The lng and lat coordinates
 
     Example:
 
     ```
     >>> {
     ...     'lng': 'longitude',
     ...     'lat': 'latitude'
     ... }
     ```
 
 
 
 
 * **Returns**
 
     Filtered results of features only looking at at
 
 
 
 * **Return type**
 
     list
 
 
 
 ### mapillary.utils.filter.image_type(data: list, image_type: str)
 The parameter might be ‘all’ (both is_pano == true and false), ‘pano’ (is_pano == true only),
 or ‘flat’ (is_pano == false only)
 
 
 * **Parameters**
 
     
     * **data** (*list*) – The data to be filtered
 
 
     * **image_type** (*str*) – Either ‘pano’ (True), ‘flat’ (False), or ‘all’ (None)
 
 
 
 * **Returns**
 
     A feature list
 
 
 
 * **Return type**
 
     list
 
 
 
 ### mapillary.utils.filter.in_shape(data: list, boundary)
 Whether the given feature list lies within the shape
 
 
 * **Parameters**
 
     
     * **data** (*list*) – A feature list to be filtered
 
 
     * **boundary** – Shapely helper for determining existence of point within a boundary
 
 
 
 * **Returns**
 
     A feature list
 
 
 
 * **Return type**
 
     list
 
 
 
 ### mapillary.utils.filter.is_looking_at(image_feature: geojson.feature.Feature, look_at_feature: geojson.feature.Feature)
 Return whether the image_feature is looking at the look_at_feature
 
 
 * **Parameters**
 
     
     * **image_feature** (*dict*) – The feature set of the image
 
 
     * **look_at_feature** (*dict*) – The feature that is being looked at
 
 
 
 * **Returns**
 
     Whether the diff is greater than 310, or less than 50
 
 
 
 * **Return type**
 
     bool
 
 
 
 ### mapillary.utils.filter.max_captured_at(data: list, max_timestamp: str)
 Selects only the feature items that are less
 than the max_timestamp
 
 
 * **Parameters**
 
     
     * **data** (*list*) – The feature list
 
 
     * **max_timestamp** (*str*) – The UNIX timestamp as the max time
 
 
 
 * **Returns**
 
     Filtered feature list
 
 
 
 * **Return type**
 
     list
 
 
 Usage:
 
 ```
 >>> max_captured_at([{'type': 'Feature', 'geometry':
 ... {'type': 'Point', 'coordinates': [30.98594605922699, 30.003757307208872]}, 'properties':
 ... { ... }, ...}], '2020-05-23')
 ```
 
 
 ### mapillary.utils.filter.min_captured_at(data: list, min_timestamp: str)
 Selects only the feature items that are less
 than the min_timestamp
 
 
 * **Parameters**
 
     
     * **data** (*list*) – The feature list
 
 
     * **min_timestamp** (*str*) – The UNIX timestamp as the max time
 
 
 
 * **Returns**
 
     Filtered feature list
 
 
 
 * **Return type**
 
     list
 
 
 Usage:
 
 ```
 >>> max_captured_at([{'type': 'Feature', 'geometry':
 ... {'type': 'Point', 'coordinates': [30.98594605922699, 30.003757307208872]}, 'properties':
 ... { ... }, ...}], '2020-05-23')
 ```
 
 
 ### mapillary.utils.filter.organization_id(data: list, organization_ids: list)
 Select only features that contain the specific organization_id
 
 
 * **Parameters**
 
     
     * **data** (*dict*) – The data to be filtered
 
 
     * **organization_ids** (*list*) – The oragnization id(s) to filter through
 
 
 
 * **Returns**
 
     A feature list
 
 
 
 * **Return type**
 
     dict
 
 
 
 ### mapillary.utils.filter.pipeline(data: dict, components: list)
 A pipeline component that helps with making filtering easier. It provides
 access to different filtering mechanism by simplying letting users
 pass in what filter they want to apply, and the arguments for that filter
 
 
 * **Parameters**
 
     
     * **data** (*dict*) – The GeoJSON to be filtered
 
 
     * **components** (*list*) – The list of filters to apply
 
 
 
 * **Returns**
 
     The filtered feature list
 
 
 
 * **Return type**
 
     list
 
 
 Usage:
 
 ```
 >>> # assume variables 'data', 'kwargs'
 >>> pipeline(
 ...     data=data,
 ...     components=[
 ...         {"filter": "image_type", "tile": kwargs["image_type"]}
 ...         if "image_type" in kwargs
 ...         else {},
 ...         {"filter": "organization_id", "organization_ids": kwargs["org_id"]}
 ...         if "org_id" in kwargs
 ...         else {},
 ...         {
 ...             "filter": "haversine_dist",
 ...             "radius": kwargs["radius"],
 ...             "coords": [longitude, latitude],
 ...         }
 ...         if "radius" in kwargs
 ...         else 1000
 ...     ]
 ... )
 ```
 
 
 ### mapillary.utils.filter.pipeline_component(func, data: list, exception_message: str, args: list)
 A pipeline component which is respnonsible for sending functional arguments over
 to the selected target function - throwing a warning in case of an exception
 
 
 * **Parameters**
 
     
     * **func** (*function*) – The filter to apply
 
 
     * **data** (*list*) – The list of features to filter
 
 
     * **exception_message** (*str*) – The exception message to print
 
 
     * **args** (*list*) – Arguments
 
 
 
 * **Returns**
 
     The filtered feature list
 
 
 
 * **Return type**
 
     list
 
 
 Usage:
 
 ```
 >>> # internally used in mapillary.utils.pipeline
 ```
 
 
 ### mapillary.utils.filter.sequence_id(data: list, ids: list)
 Filter out images that do not have the sequence_id in the list of ids
 
 
 * **Parameters**
 
     
     * **data** (*list*) – The data to be filtered
 
 
     * **ids** (*list*) – The sequence id(s) to filter through
 
 
 
 * **Returns**
 
     A feature list
 
 
 
 * **Return type**
 
     list
 
 
 ## mapillary.utils.format module
 
 ### mapillary.utils.format
 
 This module deals with converting data to and from different file formats.
 
 
 * Copyright: (c) 2021 Facebook
 
 
 * License: MIT LICENSE
 
 
 ### mapillary.utils.format.decode_pixel_geometry(base64_string: str, normalized: bool = True, width: int = 4096, height: int = 4096)
 Decodes the pixel geometry, and return the coordinates, which can be specified to be
 normalized
 
 
 * **Parameters**
 
     
     * **base64_string** (*str*) – The pixel geometry encoded as a vector tile
 
 
     * **normalized** (*bool*) – If normalization is required, defaults to True
 
 
     * **width** (*int*) – The width of the pixel geometry, defaults to 4096
 
 
     * **height** (*int*) – The height of the pixel geometry, defaults to 4096
 
 
 
 * **Returns**
 
     A dictionary with coordinates as key, and value as the normalized list
 
 
 
 * **Return type**
 
     list
 
 
 
 ### mapillary.utils.format.decode_pixel_geometry_in_geojson(geojson: Union[dict, mapillary.models.geojson.GeoJSON], normalized: bool = True, width: int = 4096, height: int = 4096)
 Decodes all the pixel_geometry
 
 
 * **Parameters**
 
     
     * **geojson** – The GeoJSON representation to be decoded
 
 
     * **normalized** (*bool*) – If normalization is required, defaults to True
 
 
     * **width** (*int*) – The width of the pixel geometry, defaults to 4096
 
 
     * **height** (*int*) – The height of the pixel geometry, defaults to 4096
 
 
 
 ### mapillary.utils.format.detection_features_to_geojson(feature_list: list)
 Converts a preprocessed list (i.e, features from the detections of either images or
 map_features from multiple segments) into a fully featured GeoJSON
 
 
 * **Parameters**
 
     **feature_list** (*list*) – A list of processed features merged from different segments within a
     detection
 
 
 
 * **Returns**
 
     GeoJSON formatted as expected in a detection format
 
 
 
 * **Return type**
 
     dict
 
 
 Example:
 
 ```
 >>> # From
 >>> [{'created_at': '2021-05-20T17:49:01+0000', 'geometry':
 ... 'GjUKBm1weS1vchIVEgIAABgDIg0JhiekKBoqAABKKQAPGgR0eXBlIgkKB3BvbHlnb24ogCB4AQ==',
 ... 'image': {'geometry': {'type': 'Point', 'coordinates': [-97.743279722222,
 ... 30.270651388889]}, 'id': '1933525276802129'}, 'value': 'regulatory--no-parking--g2',
 ... 'id': '1942105415944115'}, ... ]
 >>> # To
 >>> {'type': 'FeatureCollection', 'features': [{'type': 'Feature', 'geometry':
 ... {'type': 'Point', 'coordinates': [-97.743279722222, 30.270651388889]}, 'properties': {
 ... 'image_id': '1933525276802129', 'created_at': '2021-05-20T17:49:01+0000',
 ... 'pixel_geometry':
 ... 'GjUKBm1weS1vchIVEgIAABgDIg0JhiekKBoqAABKKQAPGgR0eXBlIgkKB3BvbHlnb24ogCB4AQ==',
 ... 'value': 'regulatory--no-parking--g2', 'id': '1942105415944115' } }, ... ]}
 ```
 
 
 ### mapillary.utils.format.feature_to_geojson(json_data: dict)
 Converts feature into a GeoJSON, returns output
 
 From:
 
 ```
 >>> {'geometry': {'type': 'Point', 'coordinates': [30.003755665554, 30.985948744314]},
 ... 'id':'506566177256016'}
 ```
 
 To:
 
 ```
 >>> {'type': 'FeatureCollection', 'features': [{'type': 'Feature', 'geometry': {'type':
 ... 'Point','coordinates': [30.98594605922699, 30.003757307208872]}, 'properties': {}}]}
 ```
 
 
 * **Parameters**
 
     **json_data** (*dict*) – The feature as a JSON
 
 
 
 * **Returns**
 
     The formatted GeoJSON
 
 
 
 * **Return type**
 
     dict
 
 
 
 ### mapillary.utils.format.flatten_dictionary(data: Union[dict, collections.abc.MutableMapping], parent_key: str = '', sep: str = '_')
 Flattens dictionaries
 
 From:
 
 ```
 >>> {'mpy-or': {'extent': 4096, 'version': 2, 'features': [{'geometry': {'type':
 ... 'Polygon', 'coordinates': [[[2402, 2776], [2408, 2776]]]}, 'properties': {}, 'id': 1,
 ... 'type': 3}]}}
 ```
 
 To:
 
 ```
 >>> {'mpy-or_extent': 4096, 'mpy-or_version': 2, 'mpy-or_features': [{'geometry':
 ... {'type':'Polygon', 'coordinates': [[[2402, 2776], [2408, 2776]]]}, 'properties':
 ... {}, 'id': 1,'type': 3}]}
 ```
 
 
 * **Parameters**
 
     
     * **data** (*dict*) – The dictionary itself
 
 
     * **parent_key** (*str*) – The root key to start from
 
 
     * **sep** (*str*) – The separator
 
 
 
 * **Returns**
 
     A flattened dictionary
 
 
 
 * **Return type**
 
     dict
 
 
 
 ### mapillary.utils.format.flatten_geojson(geojson: dict)
 Flattens a GeoJSON dictionary to a dictionary with only the relevant keys.
 This is useful for writing to a CSV file.
 
 Output Structure:
 
 ```
 >>> {
 ...     "geometry": {
 ...         "type": "Point",
 ...         "coordinates": [71.45343, 12.523432]
 ...     },
 ...     "first_seen_at": "UNIX_TIMESTAMP",
 ...     "last_seen_at": "UNIX_TIMESTAMP",
 ...     "value": "regulatory--no-parking--g2",
 ...     "id": "FEATURE_ID",
 ...     "image_id": "IMAGE_ID"
 ... }
 ```
 
 
 * **Parameters**
 
     **geojson** (*dict*) – The GeoJSON to flatten
 
 
 
 * **Returns**
 
     A flattened GeoJSON
 
 
 
 * **Return type**
 
     dict
 
 
 Note,
 
     
     1. The geometry key is always present in the output
 
 
     2. The properties are flattened to the following keys:
 
 
             * “first_seen_at”   (optional)
 
 
             * “last_seen_at”    (optional)
 
 
             * “value”           (optional)
 
 
             * “id”              (required)
 
 
             * “image_id”        (optional)
 
 
             * etc.
 
 
     3. If the ‘geometry\` type is Point, two more properties will be added:
 
 
             * “longitude”
 
 
             * “latitude”
 
 *TODO*: Further testing needed with different geometries, e.g., Polygon, etc.
 
 
 ### mapillary.utils.format.geojson_to_features_list(json_data: dict)
 Converts a decoded output GeoJSON to a list of feature objects
 
 The purpose of this formatting utility is to obtain a list of individual features for
 decoded tiles that can be later extended to the output GeoJSON
 
 From:
 
 ```
 >>> {'type': 'FeatureCollection', 'features': [{'type': 'Feature', 'geometry':
 ... {'type': 'Point','coordinates': [30.98594605922699, 30.003757307208872]},
 ... 'properties': {}}]}
 ```
 
 To:
 
 ```
 >>> [{'type': 'Feature', 'geometry': {'type': 'Point',
 ... 'coordinates': [30.98594605922699, 30.003757307208872]}, 'properties': {}}]
 ```
 
 
 * **Parameters**
 
     **json_data** (*dict*) – The given json data
 
 
 
 * **Returns**
 
     The feature list
 
 
 
 * **Return type**
 
     list
 
 
 
 ### mapillary.utils.format.geojson_to_polygon(geojson: dict)
 Converts a GeoJSON into a collection of only geometry coordinates for the purpose of
 checking whether a given coordinate point exists within a shapely polygon
 
 From:
 
 ```
 >>> {
 ...     "type": "FeatureCollection",
 ...     "features": [
 ...         {
 ...             "geometry": {
 ...                 "coordinates": [
 ...                     -80.13069927692413,
 ...                     25.78523699486192
 ...                 ],
 ...                 "type": "Point"
 ...             },
 ...             "properties": {
 ...                 "first_seen_at": 1422984049000,
 ...                 "id": 481978503020355,
 ...                 "last_seen_at": 1422984049000,
 ...                 "value": "object--street-light"
 ...             },
 ...             "type": "Feature"
 ...         },
 ...         {
 ...             "geometry": {
 ...                 "coordinates": [
 ...                     -80.13210475444794,
 ...                     25.78362849816017
 ...                 ],
 ...                 "type": "Point"
 ...             },
 ...             "properties": {
 ...                 "first_seen_at": 1423228306666,
 ...                 "id": 252538103315239,
 ...                 "last_seen_at": 1423228306666,
 ...                 "value": "object--street-light"
 ...             },
 ...             "type": "Feature"
 ...         },
 ...         ...
 ...     ]
 ... }
 ```
 
 To:
 
 ```
 >>> {
 ... "type": "FeatureCollection",
 ... "features": [
 ...         {
 ...             "type": "Feature",
 ...             "properties": {},
 ...             "geometry": {
 ...                 "type": "Polygon",
 ...                 "coordinates": [
 ...                     [
 ...                         [
 ...                             7.2564697265625,
 ...                             43.69716905314008
 ...                         ],
 ...                         [
 ...                             7.27020263671875,
 ...                             43.69419030566581
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
 
     **geojson** (*dict*) – The input GeoJSON
 
 
 
 * **Returns**
 
     A geojson of the format mentioned under ‘To’
 
 
 
 * **Return type**
 
     dict
 
 
 
 ### mapillary.utils.format.join_geojson_with_keys(geojson_src: dict, geojson_src_key: str, geojson_dest: dict, geojson_dest_key: str)
 Combines two GeoJSONS based on the similarity of their specified keys, similar to
 the SQL join functionality
 
 
 * **Parameters**
 
     
     * **geojson_src** (*dict*) – The starting GeoJSO source
 
 
     * **geojson_src_key** (*str*) – The key in properties specified for the GeoJSON source
 
 
     * **geojson_dest** (*dict*) – The GeoJSON to merge into
 
 
     * **geojson_dest_key** (*dict*) – The key in properties specified for the GeoJSON to merge into
 
 
 
 * **Returns**
 
     The merged GeoJSON
 
 
 
 * **Return type**
 
     dict
 
 
 Usage:
 
 ```
 >>> join_geojson_with_keys(
 ...     geojson_src=geojson_src,
 ...     geojson_src_key='id',
 ...     geojson_dest=geojson_dest,
 ...     geojson_dest_key='id'
 ... )
 ```
 
 
 ### mapillary.utils.format.merged_features_list_to_geojson(features_list: list)
 Converts a processed features list (i.e. a features list with all the needed features merged
 from multiple tiles) into a fully-featured GeoJSON
 
 From:
 
 ```
 >>> [{'type': 'Feature', 'geometry': {'type': 'Point',
 ... 'coordinates': [30.98594605922699, 30.003757307208872]}, 'properties': {}}, ...]
 ```
 
 To:
 
 ```
 >>> {'type': 'FeatureCollection', 'features': [{'type': 'Feature', 'geometry':
 ... {'type': 'Point','coordinates': [30.98594605922699, 30.003757307208872]},
 ... 'properties': {}}, ...]}
 ```
 
 
 * **Parameters**
 
     **features_list** (*list*) – a list of processed features merged from different tiles within a bbox
 
 
 
 * **Returns**
 
     GeoJSON string formatted with all the extra commas removed.
 
 
 
 * **Return type**
 
     str
 
 
 
 ### mapillary.utils.format.normalize_list(coordinates: list, width: int = 4096, height: int = 4096)
 Normalizes a list of coordinates with the respective width and the height
 
 From:
 
 ```
 >>> [[[2402, 2776], [2408, 2776]]]
 ```
 
 To:
 
 ```
 >>> normalize_list(coordinates)
 ... # [[[0.58642578125, 0.677734375], [0.587890625, 0.677734375]]]
 ```
 
 
 * **Parameters**
 
     
     * **coordinates** (*list*) – The coordinate list to normalize
 
 
     * **width** (*int*) – The width of the coordinates to normalize with, defaults to 4096
 
 
     * **height** (*int*) – The height of the coordinates to normalize with, defaults to 4096
 
 
 
 * **Returns**
 
     The normalized list
 
 
 
 * **Return type**
 
     list
 
 
 ## mapillary.utils.time module
 
 ### mapillary.utils.time
 
 This module contains the time utilies for the UNIX epoch seconds, the time and the date range, and
 the date filtering logic.
 
 
 * Copyright: (c) 2021 Facebook
 
 
 * License: MIT LICENSE
 
 
 ### mapillary.utils.time.date_to_unix_timestamp(date: str)
 A utility function that converts the given date
 into its UNIX epoch timestamp equivalent. It accepts the formats, ranging from
 YYYY-MM-DDTHH:MM:SS, to simply YYYY, and a permutation of the fields in between as well
 
 Has a special argument, ‘\*’, which returns current timestamp
 
 
 * **Parameters**
 
     **date** (*str*) – The date to get the UNIX timestamp epoch of
 
 
 
 * **Returns**
 
     The UNIX timestamp equivalent of the input date
 
 
 
 * **Return type**
 
     int
 
 
 Usage:
 
 ```
 >>> from utils.time_utils import date_to_unix_timestamp
 >>> date_to_unix_timestamp('2020-10-23')
 ... "1603393200"
 ```
 
 ## mapillary.utils.verify module
 
 ### mapillary.controller.rules.verify
 
 This module implements the verification of the filters or keys passed to each of the controllers
 under ./controllers that implement the business logic functionalities of the Mapillary
 Python SDK.
 
 For more information, please check out [https://www.mapillary.com/developer/api-documentation/](https://www.mapillary.com/developer/api-documentation/)
 
 
 * Copyright: (c) 2021 Facebook
 
 
 * License: MIT LICENSE
 
 
 ### mapillary.utils.verify.check_file_name_validity(file_name: str)
 Checks if the file name is valid
 
 Valid file names are,
 
 
 * Without extensions
 
 
 * Without special characters
 
 
 * A-Z, a-z, 0-9, _, -
 
 
 * **Parameters**
 
     **file_name** (*str*) – The file name to be checked
 
 
 
 * **Returns**
 
     True if the file name is valid, else False
 
 
 
 * **Return type**
 
     bool
 
 
 
 ### mapillary.utils.verify.image_bbox_check(kwargs: dict)
 Check if the right arguments have been provided for the image bounding box
 
 
 * **Parameters**
 
     **kwargs** (*dict*) – The dictionary parameters
 
 
 
 * **Returns**
 
     A final dictionary with the kwargs
 
 
 
 * **Return type**
 
     dict
 
 
 
 ### mapillary.utils.verify.image_check(kwargs)
 For image entities, check if the arguments provided fall in the right category
 
 
 * **Parameters**
 
     **kwargs** (*dict*) – A dictionary that contains the keyword key-value pair arguments
 
 
 
 ### mapillary.utils.verify.is_image_id(identity: int, fields: Optional[list] = None)
 Checks if the id is an image_id
 
 
 * **Parameters**
 
     
     * **identity** (*int*) – The id to be checked
 
 
     * **fields** (*list*) – The fields to be checked
 
 
 
 * **Returns**
 
     True if the id is an image_id, else False
 
 
 
 * **Return type**
 
     bool
 
 
 
 ### mapillary.utils.verify.kwarg_check(kwargs: dict, options: list, callback: str)
 Checks for keyword arguments amongst the kwarg argument to fall into the options list
 
 
 * **Parameters**
 
     
     * **kwargs** (*dict*) – A dictionary that contains the keyword key-value pair arguments
 
 
     * **options** (*list*) – A list of possible arguments in kwargs
 
 
     * **callback** (*str*) – The function that called ‘kwarg_check’ in the case of an exception
 
 
 
 * **Raises**
 
     **InvalidOptionError** – Invalid option exception
 
 
 
 * **Returns**
 
     A boolean, whether the kwargs are appropriate or not
 
 
 
 * **Return type**
 
     bool
 
 
 
 ### mapillary.utils.verify.points_traffic_signs_check(kwargs: dict)
 Checks for traffic sign arguments
 
 
 * **Parameters**
 
     **kwargs** (*dict*) – The parameters to be passed for filtering
 
 
 
 * **Returns**
 
     A dictionary with all the options available specifically
 
 
 
 * **Return type**
 
     dict
 
 
 
 ### mapillary.utils.verify.resolution_check(resolution: int)
 Checking for the proper thumbnail size of the argument
 
 
 * **Parameters**
 
     **resolution** (*int*) – The image size to fetch for
 
 
 
 * **Raises**
 
     **InvalidOptionError** – Invalid thumbnail size passed raises exception
 
 
 
 * **Returns**
 
     A check if the size is correct
 
 
 
 * **Return type**
 
     bool
 
 
 
 ### mapillary.utils.verify.sequence_bbox_check(kwargs: dict)
 Checking of the sequence bounding box
 
 
 * **Parameters**
 
     **kwargs** (*dict*) – The final dictionary with the correct keys
 
 
 
 * **Returns**
 
     A dictionary with all the options available specifically
 
 
 
 * **Return type**
 
     dict
 
 
 
 ### mapillary.utils.verify.valid_id(identity: int, image=True)
 Checks if a given id is valid as it is assumed. For example, is a given id expectedly an
 image_id or not? Is the id expectedly a map_feature_id or not?
 
 
 * **Parameters**
 
     
     * **identity** (*int*) – The ID passed
 
 
     * **image** (*bool*) – Is the passed id an image_id?
 
 
 
 * **Raises**
 
     **InvalidOptionError** – Raised when invalid arguments are passed
 
 
 
 * **Returns**
 
     None
 
 
 
 * **Return type**
 
     None
 
 
 ## Module contents
 
 ### mapillary.utils.__init__
 
 This package contains all the internal utilities used within the Mapillary python SDK.
 
 
 * Copyright: (c) 2021 Facebook
 
 
 * License: MIT LICENSE
