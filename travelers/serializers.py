from rest_framework import serializers
from .models import Traveler
from followers.models import Follower
from likes.models import Like


class TravelerSerializer(serializers.ModelSerializer):
    # Serializer class for the traveler model
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    following_id = serializers.SerializerMethodField()
    like_id = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_following_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            following = Follower.objects.filter(
                owner=user, followed=obj.owner
            ).first()
            # print(following)
            return following.id if following else None
        return None
    
    def get_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(
                owner = user, post = obj
            ).first()
            return like.id if like else None
        return None
    
    class Meta:
        model = Traveler
        fields = ['id', 'owner', 'created_at',
                  'updated_at', 'name', 'content', 'image',
                  'top_bucket_list', 'one_important_thing',
                  'favorite_place', 'is_owner', 'following_id',
                  'like_id']
