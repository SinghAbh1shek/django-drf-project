from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view()
def test(request):
    return Response({
        'status': True,
        'message': 'server is running fine'
    })
