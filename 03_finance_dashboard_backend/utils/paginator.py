from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class StandardResultPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

    def paginate_queryset(self, queryset, request, view=None, page_param='page'):
        self.page_query_param = page_param  # for dynamic param
        return super().paginate_queryset(queryset, request, view)

    def get_paginated_response(self, data):
        return Response({
            'status': True,
            'message': 'data fetched successfully',
            'pagination': {
                'current_page': self.page.number,
                'total_pages': self.page.paginator.num_pages,
                'total_entries': self.page.paginator.count,
                'start_index': self.page.start_index(),
                'end_index': self.page.end_index(),
                'has_next': self.page.has_next(),
                'has_previous': self.page.has_previous(),
            },
            'results': data
        })