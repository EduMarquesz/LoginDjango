from django import template
from django.shortcuts import render
from django.http import HttpResponse, response
from django.template import loader
from .models import Question
# Create your views here.

def index(request):
    return HttpResponse("Olá amigos e amigas!")

def detail(request, question_id):
    return HttpResponse('Você está olhando para a pergunta %s.' % question_id)

def results(request, question_id):
    response = "Você está olhando os resultados da pergunta %s. " 
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("Você está votando na questão %s." % question_id)

'''def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))'''

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
