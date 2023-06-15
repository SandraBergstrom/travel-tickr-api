from django.db.models import Count
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from backend.permissions import IsOwnerOrReadOnly
from .models import Traveler
from .serializers import TravelerSerializer


class TravelerList(generics.ListAPIView):
    """
    List all travelers.
    No create view as traveler creation is handled by django signals.
    """
    queryset = Traveler.objects.annotate(
        posts_count=Count('owner__post', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True)
    ).order_by('-created_at')
    serializer_class = TravelerSerializer
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'owner__following__followed__traveler',
        'owner__followed__owner__traveler',
    ]
    ordering_fields = [
        'posts_count',
        'followers_count',
        'following_count',
        'owner_following_created_at',
        'owner_followed_created_at',
    ]


class TravelerDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve or update a traveler if you're the owner.
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Traveler.objects.all()
    serializer_class = TravelerSerializer

    queryset = Traveler.objects.annotate(
        posts_count=Count('owner__post', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True)
    ).order_by('-created_at')