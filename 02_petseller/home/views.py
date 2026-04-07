from rest_framework.response import Response
from rest_framework.views import APIView
from .models import (Animal)
from .serializers import (AnimalSerializer, RegisterSerializer, LoginSerializer)
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

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
            return Response({
                'status': False,
                'message': 'something went wrong',
                'data': {}
            })

class LoginAPI(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = LoginSerializer(data = data)
            if serializer.is_valid():
                user = authenticate(username = serializer.data['username'], password = serializer.data['password'])
                if user:
                    token, _ = Token.objects.get_or_create(user=user)
                    return Response({
                        'status': True,
                        'message': 'auth token created',
                        'data': {
                            'token': str(token)
                        }
                    })

                return Response({
                    'status': False,
                    'message': 'invalid credential',
                    'data': {}
                })
            return Response({
                'status': False,
                'message': 'keys error',
                'data': serializer.errors
            })

        except Exception as e:
            return Response({
                'status': False,
                'message': 'something went wrong',
                'data': {}
            })

class AnimalCreateAPI(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        try:
            data = request.data
            data['owner']=request.user.id
            serializer = AnimalSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status': True,
                    'message': 'animal data created',
                    'data': serializer.data
                })
            return Response({
                'status': False,
                'message': 'invalid input',
                'data': serializer.errors
            })
        except Exception as e:
            print(e)
            return Response({
                'status': False,
                'message': 'something went wrong',
                'data': {}
            })