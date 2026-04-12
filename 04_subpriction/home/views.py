from rest_framework import viewsets
from rest_framework.response import Response
from .models import Blog
from .serializers import BlogSerializer,BlogDetailsSerializer
from rest_framework.decorators import action


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogDetailsSerializer

    def get_queryset(self):
        return Blog.objects.all()
    

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        return Response({
            'status': True,
            'message': 'blog fetched',
            'data': {
                'count': self.queryset.count(),
                'data': BlogSerializer(queryset, many=True).data
            }
        })
    
    @action(detail=True, methods=['get'])
    def blog_details(self, request, pk=None):
        try:
            blog_obj = Blog.objects.filter(pk=pk).first()

            if not blog_obj:
                return Response({
                    'status': False,
                    'message': "invalid id",
                    'data': {}
                })

            return Response({
                'status': True,
                'message': "record fetched",
                'data': self.serializer_class(blog_obj).data
            })

        except Exception as e:
            print(e)
            return Response({
                'status': False,
                'message': "something went wrong",
                'data': {}
            })
    