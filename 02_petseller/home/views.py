from rest_framework.response import Response
from rest_framework.views import APIView
from .models import (Animal)
from .serializers import (AnimalSerializer, RegisterSerializer)
from django.db.models import Q
from django.contrib.auth.models import User

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

class RegisterAPI(APIView):

    def post(self, request):
        try:
            data = request.data
            serializer = RegisterSerializer(data = data)
            if serializer.is_valid():
                User.objects.create_user(
                    username=data['username'],
                    email=data['email'],
                    password=data['password'],
                )
                return Response({
                    'status': True,
                    'message': 'account created',
                    'data': {}
                })
            return Response({
                'status': False,
                'message': 'keys error',
                'data': serializer.errors
            })

        except Exception as e:
            print(e)
            return Response({
                'status': False,
                'message': 'something went wrong',
                'data': {}
            })