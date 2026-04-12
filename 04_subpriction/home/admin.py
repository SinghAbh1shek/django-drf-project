from django.contrib import admin
from .models import Blog, Subscription, SubscriptionOrder

admin.site.register(Blog)
admin.site.register(Subscription)
admin.site.register(SubscriptionOrder)
