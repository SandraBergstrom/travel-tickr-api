from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Traveler
from .serializers import TravelerSerializer
from django.http import Http404


class TravelerList(APIView):
    def get(self, request):
        travelers = Traveler.objects.all()
        serializer = TravelerSerializer(travelers, many=True)
        return Response(travelers)


class TravelerDetail(APIView):
    serializer_class = TravelerSerializer
    
    def get_object(self, pk):
        try:
            traveler = Traveler.objects.get(pk=pk)
            return traveler
        except Traveler.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        traveler = self.get_object(pk)
        serializer = TravelerSerializer(traveler)
        return Response(serializer.data)

    def put(self, request, pk):
        traveler = self.get_object(pk)
        serializer = TravelerSerializer(traveler, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

