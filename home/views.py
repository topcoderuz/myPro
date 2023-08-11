from django.shortcuts import render
from django.views.generic import TemplateView

#from django.http import HttpResponse

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'


class ContactPageView(TemplateView):
    template_name = 'contact.html'

#def homeview(request):
#    return HttpResponse('Hello it`s working!')