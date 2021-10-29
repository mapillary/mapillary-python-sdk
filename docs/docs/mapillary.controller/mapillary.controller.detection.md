---
sidebar position: 2
---


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

