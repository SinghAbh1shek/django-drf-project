from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegisterSerializer
from rest_framework import status

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
            print(e)
            return Response({
                'status': False,
                'message': 'something went wrong',
                'data': {}
            }, status=500)