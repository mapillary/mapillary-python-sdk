---
sidebar position: 2
---


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
11. creator - the username and user ID who owns and uploaded the image
12. exif_orientation - enum, orientation of the camera as given by the exif tag
    (see: https://sylvana.net/jpegcrop/exif_orientation.html)
13. geometry - GeoJSON Point geometry
14. height - int, height of the original image uploaded
15. make - string, the manufacturer name of the camera device
16. model - string, the model or product series name of the camera device
17. thumb_256_url - string, URL to the 256px wide thumbnail
18. thumb_1024_url - string, URL to the 1024px wide thumbnail
19. thumb_2048_url - string, URL to the 2048px wide thumbnail
20. thumb_original_url - string, URL to the original wide thumbnail
21. merge_cc - int, id of the connected component of images that were aligned together
22. mesh - { id: string, url: string } - URL to the mesh
23. quality_score - float, how good the image is (experimental)
24. sequence - string, ID of the sequence
25. sfm_cluster - { id: string, url: string } - URL to the point cloud
26. width - int, width of the original image uploaded
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
