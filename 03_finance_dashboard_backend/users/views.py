from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegisterSerializer, LoginSerializer, ListUserSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .permissions import IsAdmin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import get_user_model
from utils.paginator import StandardResultPagination

User = get_user_model()


class RegisterAPI(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = RegisterSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status': True,
                    'message': 'user created',
                    'data': serializer.data
                }, status=201)
            return Response({
                'status': False,
                'message': 'key error',
                'data': serializer.errors
            }, status=400)
            
        except Exception as e:
            return Response({
                'status': False,
                'message': 'something went wrong',
                'data': {}
            }, status=500)
        
class LoginAPI(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = LoginSerializer(data=data)
            if serializer.is_valid():
                user = authenticate(username = serializer.validated_data['username'], password = serializer.validated_data['password'])
                if user:
                    token, _ = Token.objects.get_or_create(user=user)
                    return Response({
                        'status': True,
                        'message': 'login successful',
                        'data': {
                            'token': str(token)
                        }
                    }, status=200)
                return Response({
                    'status': False,
                    'message': 'invalid credential',
                    'data': {}
                }, status=401)
                
            return Response({
                'status': False,
                'message': 'key error',
                'data': serializer.errors
            }, status=400)
                
        except Exception as e:
            return Response({
                'status': False,
                'message': 'something went wrong',
                'data': {}
            }, status=500)


class ListUserViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, IsAdmin]
    queryset = User.objects.all()
    serializer_class = ListUserSerializer
    pagination_class = StandardResultPagination
