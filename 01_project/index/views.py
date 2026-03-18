from rest_framework.response import Response
from rest_framework.views import APIView


class TestAPI(APIView):
    def get(self, request):
        return Response({
            'status': True,
            'message': 'server is running'
        })
