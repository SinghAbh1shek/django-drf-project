from rest_framework.response import Response
from rest_framework.views import APIView
from .models import (Animal)
from .serializers import (AnimalSerializer)
from django.db.models import Q

class AnimalAPI(APIView):
    def get(self, request):
        queryset = Animal.objects.all()

        if request.GET.get('search'):
            search = request.GET.get('search')
            queryset = queryset.filter(
                Q(name__icontains = search) |
                Q(description__icontains = search) |
                Q(gender__iexact = search) |
                Q(breed__breed__icontains = search) |
                Q(color__color__icontains = search)
            )

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