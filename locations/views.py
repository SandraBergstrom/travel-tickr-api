from rest_framework import generics, permissions
from backend.permissions import IsOwnerOrReadOnly
from .models import Location
from .serializers import LocationSerializer


class LocationList(generics.ListCreateAPIView):
    """
    List all locations.
    Create a location if logged in.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)