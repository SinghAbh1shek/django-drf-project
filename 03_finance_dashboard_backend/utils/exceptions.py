from rest_framework.response import Response
from rest_framework import status

def custom_404_handler(request, exception):
    return Response({
        "status": False,
        "message": "API endpoint not found",
        "data": {}
    }, status=status.HTTP_404_NOT_FOUND)