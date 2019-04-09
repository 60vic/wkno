from django.http import HttpResponse
from django.shortcuts import render
#from django.template import loader
from .models import Item

import markdown

# Create your views here.

#def detail(request, question_id):
#	return HttpResponse("You're looking at question %s." % question_id)

def detail(request):
	return HttpResponse("You're looking at question %s." % 10)

def item(request,item_id):
	try:
		i = Item.objects.get(name = item_id)
	except Item.DoesNotExist:
		return HttpResponse("Item not found")
	return HttpResponse(markdown.markdown(i.body,extensions=["tables"]))

def add(request):
	#template = loader.get_template('main/add.html')
	#context = { "123":x, }
	render(request, 'main/add.html', {
		'123': 'x',
	})
	#return HttpResponse(template.render(context, request))