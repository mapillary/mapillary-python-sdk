---
sidebar_position: 1
---

# Tutorial Intro

Let's discover **Mapillary Python SDK in less than 5 minutes**.

## The Why

The `mapillary python sdk` was created as a result of wanting to simplify interacting with 
Mapillary's API v4, and to remove tedious code writing to extract meaningful and useful information
from [Mapillary's](https://mapillary.com/app) massive data set.

Using Mapillary's Python SDK you can pull in data for,

1. Vector Tiles
2. Entities
3. Image
4. Map Features
5. Detection
6. Organizations
7. Sequences

See the [API Documentation](https://www.mapillary.com/developer/api-documentation/) for a deep dive of how to
interact with the API.

## The How

Mapillary's Python SDK provides interfaces that remove and abstract away many underlying technical data processing
techniques to output an easy to understand and use GeoJSON format. Currently, all the high level interfaces can
be found at `src/mapillary/interface.py`. It contains functions such as,

- `get_image_close_to` - Function that takes a longitude, latitude as argument and outputs the near images.
- `get_image_looking_at` - Function that takes two sets of latitude and longitude, where the 2nd set is the
    "looking at" location from 1st set's perspective argument and outputs the near images.
- `get_detections_with_image_id` - Extracting all the detections within an image using an image key.
- `get_detections_with_map_feature_id` - Extracting all detections made for a map feature key.
- `image_thumbnail` - Gets the thumbnails of images from the API.
- `images_in_bbox` - Gets a complete list of images with custom filter within a BBox.
- `sequences_in_bbox` - Gets a complete list of all sequences of images that satisfy given filters within a BBox.
- `map_feature_points_in_bbox` - Extracts map feature points within a bounding box (bbox).
- `traffic_signs_in_bbox` - Extracts traffic signs within a bounding box (bbox).
- `images_in_geojson` - Extracts all images within a shape.
- `images_in_shape` - Extracts all images within a shape or polygon.
- `map_features_in_geojson` - Extracts all map features within a GeoJSON's boundaries.
- `map_features_in_shape` - Extracts all map features within a shape/polygon.
- `feature_from_key` - Gets a map feature for the given key argument.
- `image_from_key` - Gets an image for the given key argument.
- `save_locally` - saving data locally

## The What

### Getting Started

Get started by **installing the mapillary package**.

```bash
pip install mapillary
```

Or **try Mapillary immediately** with **[Google Colab](https://colab.research.google.com/drive/1BPWMP5k7QhXFB6nlWckHC1r54vIR0v2L?usp=sharing)**!

### Test Out Interfaces

Start by importing `mapillary.interface` as the following,

```python
"""
On importing the interface
"""

import mapillary.interface as mly

# And then simply import the desired interface
# For example, like
mly.get_image_looking_at(...)
```

### Check out more submodules

Like ths,

```python
import mapillary.config as mly_config # Importing desired configurations
import mapillary.controller as mly_controller # Importing desired controllers
import mapillary.models as mly_models # Importing the used models
import mapillary.utils as mly_utils # Importing utility material
```
