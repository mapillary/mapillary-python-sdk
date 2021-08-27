---
sidebar_position: 1
---

# mapillary.config.api package
 
 ## Submodules
 
 ## mapillary.config.api.entities module
 
 ### mapillary.config.api.entities
 
 This module contains the class implementation of the Entities API endpoints
 as string, for the entity API endpoint aspect of the API v4 of Mapillary.
 
 For more information, please check out [https://www.mapillary.com/developer/api-documentation/](https://www.mapillary.com/developer/api-documentation/).
 
 
 * Copyright: (c) 2021 Facebook
 
 
 * License: MIT LICENSE
 
 
 ### class mapillary.config.api.entities.Entities()
 Bases: `object`
 
 Each API call requires specifying the fields of the Entity you’re interested in explicitly.
 A sample image by ID request which returns the id and a computed geometry could look as
 below. For each entity available fields are listed in the relevant sections. All IDs are
 unique and the underlying metadata for each entity is accessible at
 [https://graph.mapillary.com/:id?fields=A,B,C](https://graph.mapillary.com/:id?fields=A,B,C). The responses are uniform and always return
 a single object, unless otherwise stated (collection endpoints). All collection endpoint
 metadata are wrapped in a {“data”: [ {…}, …]} JSON object.
 
 Usage:
 
 ```
 $ GET 'https://graph.mapillary.com/$IMAGE_ID?access_token=TOKEN&fields=id,computed_geometry'
 ... {
 ...     "id": "$IMAGE_ID",
 ...     "computed_geometry": {
 ...         "type": "Point",
 ...         "coordinates": [0, 0]
 ...     }
 ... }
 ```
 
 
 #### static get_detection_with_image_id(image_id: str, fields: list)
 Represent an object detected in a single image. For convenience
 this version of the API serves detections as collections. They can be
 requested as a collection on the resource (e.g. image) they contribute
 or belong to.
 
 Usage:
 
 ```
 >>> 'https://graph.mapillary.com/:image_id/detections'
 >>> # detections in the image with ID image_id
 ```
 
 Fields:
 
 ```
 1. created_at - timestamp, when was this detection created
 2. geometry - string, base64 encoded polygon
 3. image - object, image the detection belongs to
 4. value - string, what kind of object the detection represents
 ```
 
 
 #### static get_detection_with_image_id_fields()
 Gets list of possible detections for image ids
 
 
 * **Returns**
 
     Possible detection parameters
 
 
 
 * **Return type**
 
     list
 
 
 
 #### static get_detection_with_map_feature_id(map_feature_id: str, fields: list)
 Represent an object detected in a single image. For convenience
 this version of the API serves detections as collections. They can be
 requested as a collection on the resource (e.g. map feature) they
 contribute or belong to.
 
 Usage:
 
 ```
 >>> 'https://graph.mapillary.com/:map_feature_id/detections'
 >>> # detections in the image with ID map_feature_id
 ```
 
 Fields:
 
 ```
 1. created_at - timestamp, when was this detection created
 2. geometry - string, base64 encoded polygon
 3. image - object, image the detection belongs to
 4. value - string, what kind of object the detection represents
 ```
 
 
 #### static get_detection_with_map_feature_id_fields()
 Gets list of possible field parameters for map features
 
 
 * **Returns**
 
     Map feature detection fields
 
 
 
 * **Return type**
 
     list
 
 
 
 #### static get_image(image_id: str, fields: list)
 Represents the metadata of the image on the Mapillary platform with
 the following properties.
 
 Usage:
 
 ```
 >>> 'https://graph.mapillary.com/:image_id' # endpoint
 ```
 
 Fields:
 
 ```
 1. altitude - float, original altitude from Exif
 2. atomic_scale - float, scale of the SfM reconstruction around the image
 3. camera_parameters - array of float, intrinsic camera parameters
 4. camera_type - enum, type of camera projection (perspective, fisheye, or spherical)
 5. captured_at - timestamp, capture time
 6. compass_angle - float, original compass angle of the image
 7. computed_altitude - float, altitude after running image processing
 8. computed_compass_angle - float, compass angle after running image processing
 9. computed_geometry - GeoJSON Point, location after running image processing
 10. computed_rotation - enum, corrected orientation of the image
 11. exif_orientation - enum, orientation of the camera as given by the exif tag
     (see: https://sylvana.net/jpegcrop/exif_orientation.html)
 12. geometry - GeoJSON Point geometry
 13. height - int, height of the original image uploaded
 14. thumb_256_url - string, URL to the 256px wide thumbnail
 15. thumb_1024_url - string, URL to the 1024px wide thumbnail
 16. thumb_2048_url - string, URL to the 2048px wide thumbnail
 17. merge_cc - int, id of the connected component of images that were aligned together
 18. mesh - { id: string, url: string } - URL to the mesh
 19. quality_score - float, how good the image is (experimental)
 20. sequence - string, ID of the sequence
 21. sfm_cluster - { id: string, url: string } - URL to the point cloud
 22. width - int, width of the original image uploaded
 ```
 
 
 #### static get_image_fields()
 Gets list of possible image fields
 
 
 * **Returns**
 
     Image field list
 
 
 
 * **Return type**
 
     list
 
 
 
 #### static get_map_feature(map_feature_id: str, fields: list)
 These are objects with a location which have been derived from
 multiple detections in multiple images.
 
 Usage:
 
 ```
 >>> 'https://graph.mapillary.com/:map_feature_id' # endpoint
 ```
 
 Fields:
 
 ```
 1. first_seen_at - timestamp, timestamp of the least recent detection
     contributing to this feature
 2. last_seen_at - timestamp, timestamp of the most recent detection
     contributing to this feature
 3. object_value - string, what kind of map feature it is
 4. object_type - string, either a traffic_sign or point
 5. geometry - GeoJSON Point geometry
 6. images - list of IDs, which images this map feature was derived from
 ```
 
 
 #### static get_map_feature_fields()
 Gets map feature fields
 
 
 * **Returns**
 
     Possible map feature fields
 
 
 
 * **Return type**
 
     list
 
 
 
 #### static get_organization_id(organization_id: str, fields: list)
 Represents an organization which can own the imagery if users
 upload to it
 
 Usage:
 
 ```
 >>> 'https://graph.mapillary.com/:organization_id' # endpoint
 ```
 
 Fields:
 
 ```
 1. slug - short name, used in URLs
 2. name - nice name
 3. description - public description of the organization
 ```
 
 
 #### static get_organization_id_fields()
 Gets list of possible organization id fields
 
 
 * **Returns**
 
     Possible organization fields
 
 
 
 * **Return type**
 
     list
 
 
 
 #### static get_sequence(sequence_id: str)
 Represents a sequence of Image IDs ordered by capture time
 
 Usage:
 
 ```
 >>> 'https://graph.mapillary.com/image_ids?sequence_id=XXX'
 >>> # endpoint
 ```
 
 Fields:
 
 ```
 1. id - ID of the image belonging to the sequence
 ```
 
 ## mapillary.config.api.general module
 
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
 
 ## mapillary.config.api.vector_tiles module
 
 ### mapillary.config.api.vector_tiles
 
 This module contains the class implementation of the VectorTile functionalities for the Vector Tile
 aspect of the API v4 of Mapillary.
 
 For more information, please check out [https://www.mapillary.com/developer/api-documentation/](https://www.mapillary.com/developer/api-documentation/).
 
 
 * Copyright: (c) 2021 Facebook
 
 
 * License: MIT LICENSE
 
 
 ### class mapillary.config.api.vector_tiles.VectorTiles()
 Bases: `object`
 
 Vector tiles provide an easy way to visualize vast amounts of data. Mapillary APIs are heavily
 based on vector tiles to provide the developers with flexibility to programmatically interact
 with the data they contain in custom ways. Vector tiles support filtering and querying rendered
 features. Mapillary vector tiles follow the Mapbox Tile Specification,
 [https://docs.mapbox.com/vector-tiles/specification/](https://docs.mapbox.com/vector-tiles/specification/)
 
 
 #### static get_computed_image_layer(x: float, y: float, z: float)
 Contain positions of images and sequences with original geometries (computed) for the
 layer ‘image’
 
 This layer offers,
 
 
 1. zoom: 14
 
 
 2. geometry: Point
 
 
 3. data source: images
 
 With the following properties,
 
 
 1. captured_at, int, timestamp in ms since epoch
 
 
 2. compass_angle, int, the compass angle of the image
 
 
 3. id, int, ID of the image
 
 
 4. sequence_id, string, ID of the sequence this image belongs to
 
 
 5. organization_id, int, ID of the organization this image belongs to. It can be absent
 
 
 6. is_pano, bool, if it is a panoramic image
 
 
 #### static get_computed_overview_layer(x: float, y: float, z: float)
 Contain positions of images and sequences with original geometries
 (computed) for the layer ‘overview’
 
 This layer offers,
 
 
 1. zoom: 0 - 5 (inclusive)
 
 
 2. geometry: Point
 
 
 3. data source: images
 
 With the following properties,
 
 
 1. captured_at, int, timestamp in ms since epoch
 
 
 2. id, int, ID of the image
 
 
 3. sequence_id, string, ID of the sequence this image belongs to
 
 
 4. is_pano, bool, if it is a panoramic image
 
 
 #### static get_computed_sequence_layer(x: float, y: float, z: float)
 Contain positions of images and sequences with original geometries (computed) for the
 layer ‘sequence’
 
 This layer offers,
 
 
 1. zoom: 6 - 14 (inclusive)
 
 
 2. geometry: LineString
 
 
 3. data source: images captured in a single collection, sorted by captured_at
 
 With the following properties,
 
 
 1. captured_at, int, timestamp in ms since epoch
 
 
 2. id, string, ID  of the sequence (the legacy sequence key)
 
 
 3. image_id, int, ID of the ‘best’ (first) image representing the sequence
 
 
 4. organization_id, int, ID of the organization this image belongs to. It can be absent
 
 
 5. is_pano, bool, if it is a panoramic sequence
 
 
 #### static get_image_layer(x: float, y: float, z: float)
 Contain positions of images and sequences with original geometries (not computed) for the
 layer ‘image’
 
 This layer offers,
 
 
 1. zoom: 14
 
 
 2. geometry: Point
 
 
 3. data source: images
 
 With the following properties,
 
 
 1. captured_at, int, timestamp in ms since epoch
 
 
 2. compass_angle, int, the compass angle of the image
 
 
 3. id, int, ID of the image
 
 
 4. sequence_id, string, ID of the sequence this image belongs to
 
 
 5. organization_id, int, ID of the organization this image belongs to. It can be absent
 
 
 6. is_pano, bool, if it is a panoramic image
 
 
 #### static get_map_feature_point(x: float, y: float, z: float)
 These tiles represent positions of map features which are detected on the Mapillary platform
 and are not traffic signs.
 
 This layer offers,
 
 
 1. zoom: 14
 
 
 2. geometry: Point
 
 
 3. data source: map features
 
 With the following resultant properties,
 
 
 1. id, int, ID of the image
 
 
 2. value, string, name of the class which this object represent
 
 
 3. first_seen_at, int, timestamp in ms since epoch, capture time of the earliest image on
 
     which the detection contribute to this map feature
 
 
 4. last_seen_at, int, timestamp in ms since epoch, capture time of the latest image on which
 
     the detection contribute to this map feature
 
 
 #### static get_map_feature_traffic_sign(x: float, y: float, z: float)
 These tiles represent positions of map features which are detected on the Mapillary
 platform and are traffic signs.
 
 The tile metadata is exactly the same as Map feature tiles, points, except that the
 layer name is traffic_sign.
 
 This layer offers,
 
 
 1. zoom: 14
 
 
 2. geometry: Point
 
 
 3. data source: map features
 
 With the following properties,
 
 
 1. id, int, ID of the image
 
 
 2. value, string, name of the class which this object represent
 
 
 3. first_seen_at, int, timestamp in ms since epoch, capture time of the earliest image on
 
     which the detection contribute to this map feature
 
 
 4. last_seen_at, int, timestamp in ms since epoch, capture time of the latest image on
 
     which the detection contribute to this map feature
 
 
 #### static get_overview_layer(x: float, y: float, z: float)
 Contain positions of images and sequences with original
 geometries (not computed) for the layer ‘overview’
 
 This layer offers,
 
 
 1. zoom: 0 - 5 (inclusive)
 
 
 2. geometry: Point
 
 
 3. data source: images
 
 With the following properties,
 
 
 1. captured_at, int, timestamp in ms since epoch
 
 
 2. id, int, ID of the image
 
 
 3. sequence_id, string, ID of the sequence this image belongs to
 
 
 4. is_pano, bool, if it is a panoramic image
 
 
 #### static get_sequence_layer(x: float, y: float, z: float)
 Contain positions of images and sequences with original geometries (not computed) for the
 layer ‘sequence’
 
 This layer offers,
 
 
 1. zoom: 6 - 14 (inclusive)
 
 
 2. geometry: LineString
 
 
 3. data source: images captured in a single collection, sorted by captured_at
 
 With the following properties,
 
 
 1. captured_at, int, timestamp in ms since epoch
 
 
 2. id, string, ID  of the sequence (the legacy sequence key)
 
 
 3. image_id, int, ID of the ‘best’ (first) image representing the sequence
 
 
 4. organization_id, int, ID of the organization this image belongs to. It can be absent
 
 
 5. is_pano, bool, if it is a panoramic sequence
 
 ## Module contents
 
 mapillary.config.api.__init__
 
 This package contains all the API v4 endpoints provided with the Mapillary Python SDK.
 
 
 * Copyright: (c) 2021 Facebook
 
 
 * License: MIT LICENSE
