from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import (
    FormSerializer, ChoicesSerializer, AnswersSerializer, QuestionsSerializer, ResponsesSerializer
)
from django.contrib.auth import get_user_model
from .models import Form

User = get_user_model()

class FormAPI(APIView):
    def get(self, request):
        return Response({
            'status': True,
            'message': 'server is running'
        })
    
    def post(self, request):
        try:
            data = request.data
            user = User.objects.first()
            form = Form().create_blank_form(user)
            serializer = FormSerializer(form)
            return Response({
                'status': True,
                'message': 'form created successfully',
                'data': serializer.data
            })
            
        except Exception as e:
            return Response({
                'status': False,
                'message': 'something went wrongs',
                'data': {}
            })
        
    def patch(self, request):
        try:
            data = request.data
            if not data.get('form_id'):
                return Response({
                    'status': False,
                    'message': 'Form ID is required',
                    'data': {}
                })
            form_obj = Form.objects.filter(id = data.get('form_id'))
            if form_obj.exists():
                serializer = FormSerializer(form_obj[0], data=data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response({
                        'status': True,
                        'message': 'form updated successfully',
                        'data': serializer.data
                    })
                return Response({
                    'status': False,
                    'message': 'something went wrong',
                    'err': serializer.errors
                })
            return Response({
                'status': False,
                'message': 'invalid form id',
                'data': {}
            })
        except Exception as e:
            return Response({
                'status': False,
                'message': 'something went wrongs',
                'data': {}
            })