from rest_framework import serializers
from .models import Traveler


class TravelerSerializer(serializers.ModelSerializer):
    # Serializer class for the traveler model
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Traveler
        fields = ['id', 'owner', 'created_at',
                  'updated_at', 'name', 'content', 'image',
                  'top_bucket_list', 'one_important_thing',
                  'favorite_place', 'is_owner']
