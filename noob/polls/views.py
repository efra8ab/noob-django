from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World!. You're at the polls")

def results(request):
    return HttpResponse('This is the response page!!!!')

def detail(request, question_id):
    return HttpResponse(f'you are looking at question {question_id} ')

def vote(request, question_id):
    return HttpResponse(f'You are voting on question {question_id} ')

# Create your views here.
