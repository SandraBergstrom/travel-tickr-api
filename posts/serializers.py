from rest_framework import serializers
from posts.models import Post
from likes.models import Like
from bucketlist.models import Bucketlist
# from locations.models import Location
from django.contrib.humanize.templatetags.humanize import naturaltime


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    traveler_id = serializers.ReadOnlyField(source='owner.traveler.id')
    traveler_image = serializers.ReadOnlyField(
        source='owner.traveler.image.url')
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()
    like_id = serializers.SerializerMethodField()
    # location_id = serializers.SerializerMethodField()
    bucketlist_owner = serializer.ReadOnlyField(source='bucketlist.owner.traveler.id')
    bucketlist_id = serializers.SerializerMethodField()
    bucketlists_count = serializers.ReadOnlyField()
    comments_count = serializers.ReadOnlyField()

    def get_created_at(self, obj):
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)

    def validate_image(self, value):
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError('Image size larger than 2MB!')
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px!'
            )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(
                owner=user, post=obj
            ).first()
            return like.id if like else None
        return None

    def get_bucketlist_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            bucketlist = Bucketlist.objects.filter(
                owner__owner=user, post=obj
            ).first()
            return bucketlist.id if bucketlist else None
        return None

    # def get_location_id(self, obj):
    #     user = self.context['request'].user
    #     if user.is_authenticated:
    #         location = Location.objects.filter(
    #             owner=user, post_id=obj.id
    #         ).first()
    #         return location.id if location else None
    #     return None

    class Meta:
        model = Post
        fields = [
            'id', 'owner', 'is_owner', 'traveler_id',
            'traveler_image', 'created_at', 'updated_at',
            'title', 'content', 'image', 'likes_count',
            'comments_count', 'like_id', 'bucketlists_count',
            'bucketlist_id' 
        ]
