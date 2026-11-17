from mapillary.models.geojson import GeoJSON
from mapillary.utils.format import detection_features_to_geojson


def test_detections_with_and_without_image_geometry():
    point = {"type": "Point", "coordinates": [12.5, 48.25]}
    detections = [
        {"id": "1", "image": {"geometry": point}},
        {"id": "2", "geometry": "pixel-shape", "value": "object--catch-basin"},
    ]

    collection = GeoJSON(detection_features_to_geojson(detections))
    located, unlocated = collection.to_dict()["features"]

    assert located["geometry"] == point
    assert unlocated["geometry"] is None
    assert unlocated["properties"] == {
        "id": "2",
        "pixel_geometry": "pixel-shape",
        "value": "object--catch-basin",
    }


def test_previous_empty_geometry_serializes_as_null():
    collection = GeoJSON(
        {
            "type": "FeatureCollection",
            "features": [
                {"type": "Feature", "geometry": {}, "properties": {"id": "2"}}
            ],
        }
    )
    assert collection.to_dict()["features"][0]["geometry"] is None
