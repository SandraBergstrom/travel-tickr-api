from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Traveler
from .serializers import TravelerSerializer


class TravelerList(APIView):
    def get(self, request):
        travelers = Traveler.objects.all()
        serializer = TravelerSerializer(travelers, many=True)
        return Response(travelers)