from rest_framework import generics, permissions
from backend.permissions import IsOwnerOrReadOnly
from .models import Bucketlist
from .serializers import BucketlistSerializer


class BucketlistList(generics.ListCreateAPIView):
    """ 
    List all bucketlist items. Create an item if authenticated. 
    The perform_create method associates the item with the logged in user. 
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = BucketlistSerializer
    queryset = Bucketlist.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class BucketlistDetail(generics.RetrieveDestroyAPIView):
    """ 
    Retrieve an item. No Update view, as users can 
    only add or remove a post as a bucketlist item for now. 
    Destroy an item, i.e.  remove a post if owner of that item.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = BucketlistSerializer
    queryset = Bucketlist.objects.all()

