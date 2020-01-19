from django.views.generic import TemplateView
from django.shortcuts import render
from django.conf import settings

class Home(TemplateView):
    template_name = 'base.html'
    def get(self, request):
        context = {
            'title_name' : 'home',
            'ga_tag' : settings.GA_TAG,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        pass