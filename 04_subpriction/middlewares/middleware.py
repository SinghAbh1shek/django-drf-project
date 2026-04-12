from home.models import SubscriptionOrder
from django.http import JsonResponse
import datetime

class SubscriptionCheckMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        url_path = set((request.path).split('/'))
        if 'blog_details' in url_path:
            print('yes found')
            if not request.user.is_authenticated:
                return JsonResponse({
                    'status': False,
                    'message': 'You are not authenticated',
                    'data': {}
                })

            subscription_order = SubscriptionOrder.objects.filter(user = request.user, is_paid=True, expiry__gte = datetime.datetime.today().date())
            if not subscription_order.exists():
                return JsonResponse({
                    'status': False,
                    'message': 'buy subcription to view',
                    'data': {}
                })
        return self.get_response(request)