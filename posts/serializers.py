from rest_framework import serializers
from posts.models import Post
from likes.models import Like
from bucketlist.models import Bucketlist
from django.contrib.humanize.templatetags.humanize import naturaltime


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    traveler_id = serializers.ReadOnlyField(source='owner.traveler.id')
    traveler_image = serializers.ReadOnlyField(
        source='owner.traveler.image.url')
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()
    like_id = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()
    bucketlist_id = serializers.SerializerMethodField()
    bucketlists_count = serializers.ReadOnlyField()
    comments_count = serializers.ReadOnlyField()

    # Convert creation and update timt to human readable format
    def get_created_at(self, obj):
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)

    # Validat image size and dimensions
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

    # Check if the authenticated user is the owner of the post
    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    # Get like ID associated with teh authenticated user and the post
    def get_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(
                owner=user, post=obj
            ).first()
            return like.id if like else None
        return None

    # Get bucketlist ID associated with the authenticated user and the post
    def get_bucketlist_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            bucketlist = Bucketlist.objects.filter(
                owner=user, post=obj
            ).first()
            return bucketlist.id if bucketlist else None
        return None

    class Meta:
        model = Post
        fields = [
            'id', 'owner', 'is_owner', 'traveler_id',
            'traveler_image', 'created_at', 'updated_at',
            'title', 'content', 'image', 'likes_count',
            'comments_count', 'like_id', 'bucketlists_count',
            'bucketlist_id', 'location', 'country'
        ]
