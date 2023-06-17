from rest_framework import generics, permissions
from backend.permissions import IsOwnerOrReadOnly
from .models import BucketListItem
from .serializers import BucketListSerializer


class BucketList(generics.ListCreateAPIView):
    """
    List bucketlist or create a bucketlistitem if logged in
    The perform_create method associates the bucketlist with the logged in user.
    """
    serializer_class = BucketListSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = BucketListItem.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class BucketListDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a bucketlist item and edit or delete it if you own it.
    """
    serializer_class = BucketListSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = BucketListItem.objects.all()