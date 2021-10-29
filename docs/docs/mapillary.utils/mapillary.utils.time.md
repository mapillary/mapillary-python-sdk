---
sidebar position: 6
---


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
