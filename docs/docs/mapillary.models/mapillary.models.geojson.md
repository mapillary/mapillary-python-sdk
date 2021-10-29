---
sidebar position: 4
---


### mapillary.models.geojson

This module contains the class implementation for the geojson

For more information about the API, please check out
[https://www.mapillary.com/developer/api-documentation/](https://www.mapillary.com/developer/api-documentation/).


* Copyright: (c) 2021 Facebook


* License: MIT LICENSE


### class mapillary.models.geojson.Feature(feature: dict)
Bases: `object`

Representation for a feature in a feature list


* **Parameters**

    **feature** (*dict*) – The GeoJSON as the input



* **Raises**

    **InvalidOptionError** – Raised when the geojson passed is the invalid type - not a dict



* **Returns**

    A class representation of the model



* **Return type**

    mapillary.models.geojson.Feature



#### to_dict()
Return the dictionary representation of the Feature


### class mapillary.models.geojson.GeoJSON(geojson: dict)
Bases: `object`

Representation for a geojson


* **Parameters**

    **geojson** (*dict*) – The GeoJSON as the input



* **Raises**

    **InvalidOptionError** – Raised when the geojson passed is the invalid type - not a dict



* **Returns**

    A class representation of the model



* **Return type**

    mapillary.models.geojson.GeoJSON


Usage:

```
>>> import mapillary as mly
>>> from models.geojson import GeoJSON
>>> mly.interface.set_access_token('MLY|XXX')
>>> data = mly.interface.get_image_close_to(longitude=31, latitude=31)
>>> geojson = GeoJSON(geojson=data)
>>> type(geojson)
... <class 'mapillary.models.geojson.GeoJSON'>
>>> type(geojson.type)
... <class 'str'>
>>> type(geojson.features)
... <class 'list'>
>>> type(geojson.features[0])
... <class 'mapillary.models.geojson.Feature'>
>>> type(geojson.features[0].type)
... <class 'str'>
>>> type(geojson.features[0].geometry)
... <class 'mapillary.models.geojson.Geometry'>
>>> type(geojson.features[0].geometry.type)
... <class 'str'>
>>> type(geojson.features[0].geometry.coordinates)
... <class 'list'>
>>> type(geojson.features[0].properties)
... <class 'mapillary.models.geojson.Properties'>
>>> type(geojson.features[0].properties.captured_at)
... <class 'int'>
>>> type(geojson.features[0].properties.is_pano)
... <class 'str'>
```


#### append_feature(feature_inputs: dict)
Given a feature dictionary, append it to the GeoJSON object


* **Parameters**

    **feature_inputs** (*dict*) – A feature as dict



* **Returns**

    None



#### append_features(features: list)
Given a feature list, append it to the GeoJSON object


* **Parameters**

    **features** (*list*) – A feature list



* **Returns**

    None



#### encode()
Serializes the GeoJSON object


* **Returns**

    Serialized GeoJSON



#### to_dict()
Return the dict format representation of the GeoJSON


### class mapillary.models.geojson.Geometry(geometry: dict)
Bases: `object`

Representation for the geometry in a GeoJSON


* **Parameters**

    **geometry** (*dict*) – The geometry as the input



* **Raises**

    **InvalidOptionError** – Raised when the geometry passed is the invalid type - not a dict



* **Returns**

    A class representation of the model



* **Return type**

    mapillary.models.geojson.Geometry



#### to_dict()
Return dictionary representation of the geometry


### class mapillary.models.geojson.Properties(\*properties, \*\*kwargs)
Bases: `object`

Representation for the properties in a GeoJSON


* **Parameters**

    **properties** (*dict*) – The properties as the input



* **Raises**

    **InvalidOptionError** – Raised when the geojson passed is the invalid type - not a dict



* **Returns**

    A class representation of the model



* **Return type**

    mapillary.models.geojson.Properties



#### to_dict()
Return the dictionary representation of the Properties

## Module contents

### mapillary.models.__init__

This package contains the class representations of logic within the Mapillary Python SDK.


* Copyright: (c) 2021 Facebook


* License: MIT LICENSE
