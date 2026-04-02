from rest_framework.response import Response
from rest_framework.views import APIView
from .models import (Animal)
from .serializers import (AnimalSerializer)

class AnimalAPI(APIView):
    def get(self, request):
        queryset = Animal.objects.all()
        serializer = AnimalSerializer(queryset, many=True)

        return Response({
            'status': True,
            'message': 'record fetched',
            'data': serializer.data
        })
