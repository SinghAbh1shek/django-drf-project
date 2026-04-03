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

class AnimalDetailsView(APIView):
    def get(self, request, pk):
        try:
            queryset = Animal.objects.get(pk=pk)
            queryset.incrementViews()
            serializer = AnimalSerializer(queryset)
            return Response({
                'status': True,
                'message': 'record fetched',
                'data': serializer.data
            })
        except Exception as e:
            return Response({
                'status': False,
                'message': 'something went wrong',
                'data': {}
            })