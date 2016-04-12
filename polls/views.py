from django.shortcuts import render
from django.http import HttpResponse
from django.conf.urls import url
from . import views
# Create your views here.

def index(request):
	return HttpResponse("Hello, world. You're at the polls index.")
	
def detail(request, question_id):
	return HttpResponse("You're looking at question %s." % question_id)
	 
def results(request,question_id):
	response = "You're looking at the results of question %s."
	return HttpResponse(response % question_id)

def vote(request,question_id):
	return HttpResponse("You're voting on question %s." % question_id)
	
urlpatterns = [
	url(r'^$', view.index, name='index'),
	url(r'(^?P<question_id>[0-9]+)/results/$', view.results, name='results'),
	url(r'(^P<question_id>[0-9]+/vote/$)',view.vote, name='vote'),
]	