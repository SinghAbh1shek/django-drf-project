from django.db import models
from django.contrib.auth.models import User, AbstractUser
from .choices import QUESTION_CHOICES
from .utils.utility import generate_random_string

class User(AbstractUser, models.Model):
    email = models.EmailField(unique=True)

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Choices(BaseModel):
    choice = models.CharField(max_length=100)

    class Meta:
        db_table = 'choices'
        ordering = ['choice']

class Questions(BaseModel):
    question = models.CharField(max_length=100)
    question_type = models.CharField(choices=QUESTION_CHOICES, max_length=100)
    required = models.BooleanField(default=False)
    choices = models.ManyToManyField(Choices, related_name='question_choices', blank=True)

class Form(BaseModel):
    code = models.CharField(max_length=100, unique=True)
    creater = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    background_color = models.CharField(max_length=100, default='#272124')
    collect_email = models.BooleanField(default=False)
    questions = models.ManyToManyField(Questions, related_name='questions')

    def create_blank_form(user):
        form_token = generate_random_string()
        choices = Choices.objects.create(choice = 'option 1')
        question = Questions.objects.create(question_type="multiple choice", question="untitled question")
        question.choices.add(choices)

        form = Form(code = form_token, title = 'Untitled Form', creator=user)
        form.save()
        form.questions.add(question)
        return form

class Answers(models.Model):
    answer = models.CharField(max_length=100)
    answer_to = models.ForeignKey(Questions, on_delete=models.CASCADE, related_name='answer_to')

class Responses(BaseModel):
    response_code = models.CharField(max_length=100, unique=True)
    response_to = models.ForeignKey(Form, on_delete=models.CASCADE)
    responder_ip = models.CharField(max_length=100)
    responder_email = models.EmailField(null=True, blank=True)
    response = models.ManyToManyField(Answers, related_name='answers')
