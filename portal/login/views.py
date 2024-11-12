from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
def signUp(request):
    template=loader.get_template('login_form.html')
    return HttpResponse(template.render())
