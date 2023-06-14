from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Traveler


class TravelerList(APIView):
    def get(self, request):
        travelers = Traveler.objects.all()
        return Response(travelers)