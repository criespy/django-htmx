from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from django.http import HttpResponse
#from htmx.client import htmx

class homepageView(TemplateView):
    template_name = 'home.html'

class clicked(TemplateView):
    template_name = 'clicked.html'
#class dataSend(View):
#    def get(self, request):
#        html = """
#        <div id="my-div">
#            <h1>This is my div</h1>
#        </div>
#        """

        # This code will update the text of the h1 element in the div
        # with the value of the `message` variable.
#        html = htmx.update(html, id="my-div", message="Hello, world!")

#        return HttpResponse(html)