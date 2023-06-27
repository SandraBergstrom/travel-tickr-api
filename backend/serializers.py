from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers


class CurrentUserSerializer(UserDetailsSerializer):
    traveler_id = serializers.ReadOnlyField(source='traveler.id')
    traveler_image = serializers.ReadOnlyField(source='traveler.image.url')

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + (
            'traveler_id', 'traveler_image'
        )
