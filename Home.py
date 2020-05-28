
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

class Home():

    def home(self):
        template = get_template('index.html')
        return HttpResponse(template.render())

    def form(self):
        template = get_template('Form.html')
        return HttpResponse(template.render())

    '''def index(request):
        return render(request, 'index.html',{
        })'''