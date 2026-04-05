from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Sum, Count, Q, F
from django.db.models.functions import TruncMonth
from records.models import Record
from records.serializers import RecordSerializer
from django.core.paginator import Paginator
from utils.paginator import paginate
from django_filters.rest_framework import DjangoFilterBackend
from records.filter import RecordFilter


class DashboardAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get_summary(self, records):
        data = records.aggregate(
            total_income=Sum('amount', filter=Q(type='income')),
            total_expense=Sum('amount', filter=Q(type='expense'))
        )

        income = data['total_income'] or 0
        expense = data['total_expense'] or 0

        return {
            "total_income": income,
            "total_expense": expense,
            "net_balance": income - expense
        }
    
    def get_top_category(self, records):
        return records.filter(type='expense').values(
            category_name=F('category__category')
        ).annotate(
            total_spent=Sum('amount')
        ).order_by('-total_spent').first()
    
    def get_monthly_trends(self, records):
        monthly = records.annotate(
            month=TruncMonth('date')
        ).values('month').annotate(
            income=Sum('amount', filter=Q(type='income')),
            expense=Sum('amount', filter=Q(type='expense'))
        ).order_by('month')

        return [
            {
                "month": m['month'].strftime("%b %Y"),
                "income": m['income'] or 0,
                "expense": m['expense'] or 0
            }
            for m in monthly
        ]

    def get_category_data(self, records, page):
        data =  records.filter(type='expense').values(
            category_name=F('category__category')
        ).annotate(
            total_spent=Sum('amount'),
            total_transactions=Count('id')
        ).order_by('-total_spent')

        paginator = Paginator(data, 10)
        return paginate(data, paginator, page)

    

    def get_per_user_summary(self, records, page):
        users = records.values('created_by__username').annotate(
            total_income=Sum('amount', filter=Q(type='income')),
            total_expense=Sum('amount', filter=Q(type='expense'))
        )

        data =  [
            {
                "username": user['created_by__username'],
                "total_income": user['total_income'] or 0,
                "total_expense": user['total_expense'] or 0,
                "net_balance": (user['total_income'] or 0) - (user['total_expense'] or 0)
            }
            for user in users
        ]

        paginator = Paginator(data, 10)
        return paginate(data, paginator, page)
    
    def get_recent(self, records):
        recent = records.order_by('-created_at')[:5]
        return RecordSerializer(recent, many=True).data
    

    
    def get(self, request):
        per_user_page = int(request.GET.get('per_user_page', 1))
        category_page = int(request.GET.get('category_page', 1))
        user = request.user

        records = Record.objects.select_related('category', 'created_by')

        filterset = RecordFilter(request.GET, queryset=records)
        if filterset.is_valid():
            records = filterset.qs

        # Role-based filtering
        if user.role == 'user':
            records = records.filter(created_by=user)

        return Response({
            "summary": self.get_summary(records),
            # "top_category": self.get_top_category(records),
            "monthly_trends": self.get_monthly_trends(records),
            "category_data": self.get_category_data(records, category_page),
            "per_user": self.get_per_user_summary(records, per_user_page),
            "recent": self.get_recent(records),
        })