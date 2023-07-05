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
    This viewset also handles filtering by fields defined in `filterset_fields`
    and ordering by fields defined in `ordering_fields`.
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
        'owner__following__created_at',
        'owner__followed__created_at',
    ]


class TravelerDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve or update a traveler if you're the owner.
    This viewset also applies the IsOwnerOrReadOnly permission to ensure
    that only the owner of a traveler instance can update it.
    """
    permission_classes = [IsOwnerOrReadOnly]

    queryset = Traveler.objects.annotate(
        posts_count=Count('owner__post', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True)
    ).order_by('-created_at')
    serializer_class = TravelerSerializer
