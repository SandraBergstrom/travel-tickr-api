from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers


# Custom serializer for user details.
# This serializer extends the UserDetailsSerializer from
# 'dj_rest_auth' to include 'traveler_id' and 'traveler_image' fields.
# These additional fields are read-only and sourced from the
# related 'traveler' object.
class CurrentUserSerializer(UserDetailsSerializer):
    traveler_id = serializers.ReadOnlyField(source='traveler.id')
    traveler_image = serializers.ReadOnlyField(source='traveler.image.url')

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + (
            'traveler_id', 'traveler_image'
        )
