from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, Webpage, AccessRecord
# Create your views here.

def index(req):
    webpages_list = Webpage.objects.order_by('name')
    # my_dict = {'insert_me': "Hello I am from the views.py"}
    date_dict = {'access_record':webpages_list}
    return render(req, 'first_app/index.html', context = date_dict)