from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
def test(request):
    que = "Who developed Python?"
    a="James Gosling"
    b="Guido van Rossum"
    c="Dennis Ritchie"
    d="Bjarne Stroustrup"
    context={
        'que':que,
        'a':a,
        'b':b,
        'c':c,
        'd':d
    }
    template=loader.get_template('test.html')
    return HttpResponse(template.render(context,request))
