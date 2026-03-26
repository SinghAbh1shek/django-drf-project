from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Form, Questions, Answers, Responses, Choices

User = get_user_model()
admin.site.register(User)
admin.site.register(Form)
admin.site.register(Questions)
admin.site.register(Answers)
admin.site.register(Responses)
admin.site.register(Choices)
