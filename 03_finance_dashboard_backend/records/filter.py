import django_filters
from .models import Record

class RecordFilter(django_filters.FilterSet):
    category_name = django_filters.CharFilter(
        field_name='category__category',
        lookup_expr='iexact'
    )
    created_by = django_filters.CharFilter(
        field_name='created_by__username',
        lookup_expr='iexact'
    )

    class Meta:
        model = Record
        fields = ['type', 'date']