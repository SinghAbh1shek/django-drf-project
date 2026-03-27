from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import (
    FormSerializer, ChoicesSerializer, AnswersSerializer, QuestionsSerializer, ResponsesSerializer
)
from django.contrib.auth import get_user_model
from .models import Form, Questions, Choices

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
        
class QuestionAPI(APIView):

    def post(self, request):
        try:
            data = request.data
            data['question'] = 'Untitled Question'
            data['question_type'] = 'multiple choice'

            if not data.get('form_id'):
                return Response({
                        'status': False,
                        'message': 'Form ID is required',
                        'data': {}
                    })

            serializer = QuestionsSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                form = Form.objects.get(id = data['form_id'])
                form.questions.add(Questions.objects.get(id = serializer.data['id']))

                return Response({
                    'status': True,
                    'message': 'question created',
                    'data': serializer.data
                })
            return Response({
                'status': False,
                'message': 'invalid form',
                'data': {}
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
            if not data.get('question_id'):
                return Response({
                    'status': False,
                    'message': 'question_id is required',
                    'data': {}
                })
            question_obj = Questions.objects.filter(id = data.get('question_id'))
            if not question_obj.exists():
                return Response({
                    'status': False,
                    'message': 'invalid question_id',
                    'data': {}
                })
            serializer = QuestionsSerializer(question_obj[0], data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status': True,
                    'message': 'question updated',
                    'data': serializer.data
                })
            return Response({
                'status': False,
                'message': 'something went wrong',
                'err': serializer.errors
            })
            
                

        except Exception as e:
            return Response({
                'status': False,
                'message': 'something went wrongs',
                'data': {}
            })
            
class ChoiceAPI(APIView):
    def post(self, request):
        try:
            data = request.data
            if not data.get('form_id') or not data.get('question_id'):
                return Response({
                    'status': False,
                    'message': 'form_id and question_id both are required',
                    'data': {}
                })
            serializer = ChoicesSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                form = Form.objects.get(id=data['form_id'])
                form.questions.get(id=data['question_id']).choices.add(Choices.objects.get(id=serializer.data['id']))
                return Response({
                    'status': True,
                    'message': 'a choice created',
                    'data': serializer.data
                })
            return Response({
                'status': False,
                'message': 'invalid form_id or question_id',
                'err': serializer.errors
            })

        except Exception as e:
            return Response({
                'status': False,
                'message': 'something went wrongs',
                'err': {}
            })