---
sidebar position: 7
---


### mapillary.controller.rules.verify

This module implements the verification of the filters or keys passed to each of the controllers
under ./controllers that implement the business logic functionalities of the Mapillary
Python SDK.

For more information, please check out [https://www.mapillary.com/developer/api-documentation/](https://www.mapillary.com/developer/api-documentation/)


* Copyright: (c) 2021 Facebook


* License: MIT LICENSE


### mapillary.utils.verify.bbox_validity_check(bbox)

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



### mapillary.utils.verify.international_dateline_check(bbox)

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
