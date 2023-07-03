from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Comment
from likes.models import Like


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer for the Comment model
    Adds three extra fields when returning a list of Comment instances
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    traveler_id = serializers.ReadOnlyField(source='owner.traveler.id')
    traveler_image = serializers.ReadOnlyField(
        source='owner.traveler.image.url')
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()
    like_id = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(
                owner=user, comment=obj
            ).first()
            return like.id if like else None
        return None

    def get_created_at(self, obj):
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)

    class Meta:
        model = Comment
        fields = [
            'id', 'owner', 'is_owner', 'traveler_id', 'traveler_image',
            'post', 'created_at', 'updated_at', 'content', 'likes_count',
            'like_id'
        ]


class CommentDetailSerializer(CommentSerializer):
    """
    Serializer for the Comment model used in Detail view
    Post is a read only field so that we dont have to set it on each update
    """
    post = serializers.ReadOnlyField(source='post.id')
