from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Traveler
from .serializers import TravelerSerializer
from django.http import Http404
from backend.permissions import IsOwnerOrReadOnly


class TravelerList(APIView):
    """
    List all travelers
    No Create view (post method), as profile creation handled by django signals
    """

    def get(self, request):
        travelers = Traveler.objects.all()
        serializer = TravelerSerializer(
            travelers, many=True, context={'request': request})
        return Response(serializer.data)


class TravelerDetail(APIView):
    serializer_class = TravelerSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_object(self, pk):
        # Retrive a specific traverel based on the primary key
        try:
            traveler = Traveler.objects.get(pk=pk)
            # Check permissions to ensure only the owner can modify their traveler profile.
            self.check_object_permissions(self.request, traveler)
            return traveler
        except Traveler.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        # Handle GET request to retrieve details of a traveler
        traveler = self.get_object(pk)
        serializer = TravelerSerializer(traveler, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk):
        # Handle PUT request to update details of a traveler
        traveler = self.get_object(pk)
        serializer = TravelerSerializer(traveler, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
