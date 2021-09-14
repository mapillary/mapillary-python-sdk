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

- `get_image_close_to` -
- `get_image_looking_at` -
- `get_detections_with_image_id` -
- `get_detections_with_map_feature_id` - 
- `image_thumbnail` -
- `images_in_bbox` -
- `sequences_in_bbox` -
- `map_feature_points_in_bbox` -
- `traffic_signs_in_bbox` -
- `images_in_geojson` -
- `images_in_shape` -
- `map_features_in_geojson` -
- `map_features_in_shape` -
- `feature_from_key` -
- `image_from_key` - 
- `save_locally` - saving data locally

## The What

## Getting Started

Get started by **installing the mapillary package**.

```bash
pip install mapillary
```

Or **try Mapillary immediately** with **[Google Colab](https://colab.research.google.com/drive/1BPWMP5k7QhXFB6nlWckHC1r54vIR0v2L?usp=sharing)**!

## Test Out Interfaces

Start by importing `mapillary.interface`

Generate a new Docusaurus site using the **classic template**:

```shell
npx @docusaurus/init@latest init my-website classic
```

## Start your site

Run the development server:

```shell
cd my-website

npx docusaurus start
```

Your site starts at `http://localhost:3000`.

Open `docs/intro.md` and edit some lines: the site **reloads automatically** and display your changes.
