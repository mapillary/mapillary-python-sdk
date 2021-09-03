# Copyright (c) Facebook, Inc. and its affiliates. (http://www.facebook.com)
# -*- coding: utf-8 -*-

"""
mapillary.config.api.entities
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module contains the class implementation of the Entities API endpoints
as string, for the entity API endpoint aspect of the API v4 of Mapillary.

For more information, please check out https://www.mapillary.com/developer/api-documentation/.

- Copyright: (c) 2021 Facebook
- License: MIT LICENSE
"""

# Local imports

# # Exception Handling
from mapillary.models.exceptions import InvalidFieldError


class Entities:
    """
    Each API call requires specifying the fields of the Entity you're interested in explicitly.
    A sample image by ID request which returns the id and a computed geometry could look as
    below. For each entity available fields are listed in the relevant sections. All IDs are
    unique and the underlying metadata for each entity is accessible at
    https://graph.mapillary.com/:id?fields=A,B,C. The responses are uniform and always return
    a single object, unless otherwise stated (collection endpoints). All collection endpoint
    metadata are wrapped in a {"data": [ {...}, ...]} JSON object.

    Usage::

        $ GET 'https://graph.mapillary.com/$IMAGE_ID?access_token=TOKEN&fields=id,computed_geometry'
        ... {
        ...     "id": "$IMAGE_ID",
        ...     "computed_geometry": {
        ...         "type": "Point",
        ...         "coordinates": [0, 0]
        ...     }
        ... }
    """

    @staticmethod
    def get_image(image_id: str, fields: list) -> str:
        """
        Represents the metadata of the image on the Mapillary platform with
        the following properties.

        Usage::

            >>> 'https://graph.mapillary.com/:image_id' # endpoint

        Fields::

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
        """

        fields = Entities.__field_validity(
            given_fields=fields,
            actual_fields=Entities.get_image_fields(),
            endpoint="https://graph.mapillary.com/:image_id?fields=",
        )

        return f"https://graph.mapillary.com/{image_id}/?fields={','.join(fields)}"

    @staticmethod
    def get_image_fields() -> list:
        """
        Gets list of possible image fields

        :return: Image field list
        :rtype: list
        """

        return [
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
        ]

    @staticmethod
    def get_map_feature(map_feature_id: str, fields: list) -> str:
        """
        These are objects with a location which have been derived from
        multiple detections in multiple images.

        Usage::

            >>> 'https://graph.mapillary.com/:map_feature_id' # endpoint

        Fields::

            1. first_seen_at - timestamp, timestamp of the least recent detection
                contributing to this feature
            2. last_seen_at - timestamp, timestamp of the most recent detection
                contributing to this feature
            3. object_value - string, what kind of map feature it is
            4. object_type - string, either a traffic_sign or point
            5. geometry - GeoJSON Point geometry
            6. images - list of IDs, which images this map feature was derived from
        """

        fields = Entities.__field_validity(
            given_fields=fields,
            actual_fields=Entities.get_map_feature_fields(),
            endpoint="https://graph.mapillary.com/:map_feature_id?fields=",
        )

        return (
            f"https://graph.mapillary.com/{map_feature_id}/?fields={','.join(fields)}"
        )

    @staticmethod
    def get_map_feature_fields() -> list:
        """
        Gets map feature fields

        :return: Possible map feature fields
        :rtype: list
        """

        return [
            "first_seen_at",
            "last_seen_at",
            "object_value",
            "object_type",
            "geometry",
            "images",
        ]

    @staticmethod
    def get_detection_with_image_id(
        image_id: str,
        fields: list,
    ) -> str:
        """
        Represent an object detected in a single image. For convenience
        this version of the API serves detections as collections. They can be
        requested as a collection on the resource (e.g. image) they contribute
        or belong to.

        Usage::

            >>> 'https://graph.mapillary.com/:image_id/detections'
            >>> # detections in the image with ID image_id

        Fields::

            1. created_at - timestamp, when was this detection created
            2. geometry - string, base64 encoded polygon
            3. image - object, image the detection belongs to
            4. value - string, what kind of object the detection represents
        """

        fields = Entities.__field_validity(
            given_fields=fields,
            actual_fields=Entities.get_detection_with_image_id_fields(),
            endpoint="https://graph.mapillary.com/:image_id/detections/?fields=",
        )

        return f"https://graph.mapillary.com/{image_id}/detections/?fields={','.join(fields)}"

    @staticmethod
    def get_detection_with_image_id_fields() -> list:
        """
        Gets list of possible detections for image ids

        :return: Possible detection parameters
        :rtype: list
        """

        return ["created_at", "geometry", "image", "value"]

    @staticmethod
    def get_detection_with_map_feature_id(
        map_feature_id: str,
        fields: list,
    ) -> str:
        """
        Represent an object detected in a single image. For convenience
        this version of the API serves detections as collections. They can be
        requested as a collection on the resource (e.g. map feature) they
        contribute or belong to.

        Usage::

            >>> 'https://graph.mapillary.com/:map_feature_id/detections'
            >>> # detections in the image with ID map_feature_id

        Fields::

            1. created_at - timestamp, when was this detection created
            2. geometry - string, base64 encoded polygon
            3. image - object, image the detection belongs to
            4. value - string, what kind of object the detection represents
        """

        fields = Entities.__field_validity(
            given_fields=fields,
            actual_fields=Entities.get_detection_with_map_feature_id_fields(),
            endpoint="https://graph.mapillary.com/:map_feature_id/detections/?fields=",
        )

        return f"https://graph.mapillary.com/{map_feature_id}/detections/?fields={','.join(fields)}"

    @staticmethod
    def get_detection_with_map_feature_id_fields() -> list:
        """
        Gets list of possible field parameters for map features

        :return: Map feature detection fields
        :rtype: list
        """

        return ["created_at", "geometry", "image", "value"]

    @staticmethod
    def get_organization_id(
        organization_id: str,
        fields: list,
    ) -> str:
        """
        Represents an organization which can own the imagery if users
        upload to it

        Usage::

            >>> 'https://graph.mapillary.com/:organization_id' # endpoint

        Fields::

            1. slug - short name, used in URLs
            2. name - nice name
            3. description - public description of the organization
        """

        fields = Entities.__field_validity(
            given_fields=fields,
            actual_fields=Entities.get_organization_id_fields(),
            endpoint="https://graph.mapillary.com/:organization_id?fields=",
        )

        return (
            f"https://graph.mapillary.com/{organization_id}/?fields={','.join(fields)}"
        )

    @staticmethod
    def get_organization_id_fields() -> list:
        """
        Gets list of possible organization id fields

        :return: Possible organization fields
        :rtype: list
        """

        return ["slug", "name", "description"]

    @staticmethod
    def get_sequence(
        sequence_id: str,
    ) -> str:
        """
        Represents a sequence of Image IDs ordered by capture time

        Usage::

            >>> 'https://graph.mapillary.com/image_ids?sequence_id=XXX'
            >>> # endpoint

        Fields::

            1. id - ID of the image belonging to the sequence
        """

        return f"https://graph.mapillary.com/image_ids?sequence_id={sequence_id}"

    @staticmethod
    def __field_validity(
        given_fields: list, actual_fields: list, endpoint: str
    ) -> list:
        """
        Checks if the given_fields are the actual correct fields for the given endpoint
        Compares against the list provided in `actual_fields`

        :param given_fields: The fields given as argument to check in
        :type given_fields: list

        :param actual_fields: The fields to check against
        :type actual_fields: list

        :param endpoint: The endpoint that is being targeted
        :type endpoint: str

        :raises InvalidFieldError: Raised when an API endpoint is passed invalid field elements

        :return: The given_fields if everything is correct
        :rtype: list
        """

        # Converting the given_fields into lowercase
        given_fields = [field.lower() for field in given_fields]

        # Enforce the existence of 'geometry' in the given_fields
        if "geometry" not in given_fields:
            given_fields.append("geometry")

        # Going through all the given fields
        for field in given_fields:

            # If 'all' is encountered ...
            if field == "all":

                # ... simply return the actual_fields list
                return actual_fields

            # If a field does not exist in the actual_fields ...
            if field not in actual_fields:

                # Raise an InvalidFieldError error
                raise InvalidFieldError(
                    # Specifying what endpoint was specified
                    endpoint=endpoint,
                    # Specify what field triggered the exception
                    field=field,
                )

        # If no error occurred, and all the fields are correct, return the given_fields
        return given_fields
