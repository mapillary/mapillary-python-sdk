"""
mapillary.config.api.entities

This module contains the class implementation of the
Entities functionalities for the entity API endpoint aspect
of the APIv4 of Mapillary.

REFERENCE,

1. https://www.mapillary.com/developer/api-documentation/
"""

# Local imports
from models.exceptions import InvalidFieldError


class Entities:
    """Each API call requires specifying the fields of the Entity you're
    interested in explicitly. A sample image by ID request which returns
    the id and a computed geometry could look as below. For each entity
    available fields are listed in the relevant sections. All IDs are
    unique and the underlying metadata for each entity is accessible at
    https://graph.mapillary.com/:id?fields=A,B,C. The responses are
    uniform and always return a single object, unless otherwise stated
    (collection endpoints). All collection endpoint metadata are wrapped
    in a {"data": [ {...}, ...]} JSON object.

    Usage::
        >>> GET https://graph.mapillary.com/$IMAGE_ID? \
        access_token=$TOKEN&fields=id,computed_geometry
        >>> {
        >>>     "id": "$IMAGE_ID",
        >>>     "computed_geometry": {
        >>>         "type": "Point",
        >>>         "coordinates": [0, 0]
        >>>     }
        >>> }
    """

    @staticmethod
    def get_image(image_id: str, options: list) -> str:
        """Represents the metadata of the image on the Mapillary platform with
        the following properties.

        Usage::
            >>> https://graph.mapillary.com/:image_id # endpoint

                    Represents the metadata of the image on the Mapillary
                    platform with the following

        Fields::
            1. altitude - float, original altitude from Exif
            2. atomic_scale - FIXME, FIXME
            3. camera_parameters - FIXME, FIXME
            4. camera_type - enum, type of camera used for taking the phone.
            VALUES: FIXME
            5. captured_at - timestamp, capture time
            6. compass_angle - float, original compass angle of the image
            7. computed_altitude - float, altitude after running image
            processing
            8. computed_compass_angle - float, compass angle after running
            image processing
            9. computed_geometry - GeoJSON Point, location after running image
            processing
            10. computed_rotation - enum, corrected orientation of the image
            11. exif_orientation - enum, original orientation of the image.
            VALUES: FIXME
            12. geometry - GeoJSON Point geometry
            13. height - int, height of the original image uploaded
            14. thumb_256_url - string, URL to the 256px wide thumbnail
            15. thumb_1024_url - string, URL to the 1024px wide thumbnail
            16. thumb_2048_url - string, URL to the 2048px wide thumbnail
            17. merge_cc
            18. mesh - { id: string, url: string } - URL to the mesh
            19. quality_score - float, how good the image is (experimental)
            20. sequence - string, ID of the sequence
            21. sfm_cluster - { id: string, url: string } - URL to the point
            cloud
            22. width - int, width of the original image uploaded
        """

        for option in options:
            if option not in [
                "altitude",
                "atomic_scale",
                "camera_parameters",
                "camera_type",
                "captured_at",
                "compass_angle",
                "computed_altitude",
                "computed_compass_angle",
                "computed_geometry",
                "computed_rotation",
                "exif_orientation",
                "geometry",
                "height",
                "thumb_256_url",
                "thumb_1024_url",
                "thumb_2048_url",
                "merge_cc",
                "mesh",
                "quality_score",
                "sequence",
                "sfm_cluster",
                "width",
            ]:
                raise InvalidFieldError(option, 
                'https://graph.mapillary.com/:image_id?fields=options...')


        return f"https://graph.mapillary.com/{image_id}/?fields={','.join(options)}"

    @staticmethod
    def get_map_feature(map_feature_id: str, options: list) -> str:
        """These are objects with a location which have been derived from
        multiple detections in multiple images.

        Usage::
            >>> https://graph.mapillary.com/:map_feature_id # endpoint

        Fields::
            1. first_seen_at - timestamp, timestamp of the least recent
            detection contributing to this feature
            2. last_seen_at - timestamp, timestamp of the most recent
            detection contributing to this feature
            3. object_value - string, what kind of map feature it is
            4. object_type - string, either a traffic_sign or point
            5. geometry - GeoJSON Point geometry
            6. images - list of IDs, which images this map feature was derived
            from
        """

        for option in options:
            if option not in [
                "first_seen_at",
                "last_seen_at",
                "object_value",
                "object_type",
                "geometry",
                "images",
            ]:
                raise InvalidFieldError(option, 
                'https://graph.mapillary.com/:map_feature_id?fields=')

        return (
            f"https://graph.mapillary.com/{map_feature_id}/?"
            f'fields={",".join(options)}'
        )

    @staticmethod
    def get_detection_with_image_id(
        image_id: str,
        options: list,
    ) -> list:
        """Represent an object detected in a single image. For convenience
        this version of the API serves detections as collections. They can be
        requested as a collection on the resource (e.g. image) they contribute
        or belong to.

        Usage::
            >>> https://graph.mapillary.com/:image_id/detections # detections
            in the image with ID image_id

        Fields::
            1. created_at - timestamp, when was this detection created
            2. geometry - string, base64 encoded polygon
            3. image - object, image the detection belongs to
            4. value - string, what kind of object the detection represents
        """

        for option in options:
            if option not in [
                "created_at",
                "geometry",
                "image",
                "value"
            ]:
                raise InvalidFieldError(option, 
                'https://graph.mapillary.com/:image_id/detections/?fields='
                'options...')


        return (
            f"https://graph.mapillary.com/{image_id}/detections/?"
            f'fields={",".join(options)}'
        )

    @staticmethod
    def get_detection_with_map_feature_id(
        map_feature_id: str,
        options: list,
    ) -> list:
        """Represent an object detected in a single image. For convenience
        this version of the API serves detections as collections. They can be
        requested as a collection on the resource (e.g. map feature) they
        contribute or belong to.

        Usage::
            >>> https://graph.mapillary.com/:map_feature_id/detections
            >>> # detections in the image with ID map_feature_id

        Fields::
            1. created_at - timestamp, when was this detection created
            2. geometry - string, base64 encoded polygon
            3. image - object, image the detection belongs to
            4. value - string, what kind of object the detection represents
        """

        for option in options:
            if option not in [
                "created_at",
                "geometry",
                "image",
                "value"
            ]:
                raise InvalidFieldError(option, 
                'https://graph.mapillary.com/:map_feature_id/detections/?'
                'fields=')


        return (
            f"https://graph.mapillary.com/{map_feature_id}/detections/"
            f'?fields={",".join(options)}'
        )

    @staticmethod
    def get_organization_id(
        organization_id: str,
        options: list,
    ) -> str:
        """Represents an organization which can own the imagery if users
        upload to it

        Usage::
            >>> https://graph.mapillary.com/:organization_id # endpoint

        Fields::
            1. slug - short name, used in URLs
            2. name - nice name
            3. description - public description of the organization
        """

        for option in options:
            if option not in [
                "slug",
                "name",
                "description"
            ]:
                raise InvalidFieldError(option, 
                'https://graph.mapillary.com/:organization_id?fields=')


        return (
            f"https://graph.mapillary.com/{organization_id}/"
            f'?fields={",".join(options)}'
        )

    @staticmethod
    def get_sequence(
        sequence_id: str,
    ) -> str:
        """Represents a sequence of Image IDs ordered by capture time

        Usage::
            >>> https://graph.mapillary.com/image_ids?sequence_id=XXX
            >>> # endpoint

        Fields::
            1. id - ID of the image belonging to the sequence
        """

        return f"https://graph.mapillary.com/image_ids?sequence_id={sequence_id}"
