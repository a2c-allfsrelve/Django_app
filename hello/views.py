
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    prams = {
        'title': 'Hello/Index',
        'msg' : 'おっぱいに吸いつきたい。',
        'goto' : 'next',
        
    }
    return render(request, 'hello/index.html', prams) #settings.pyを忘れるな

def next(request):
    parms = {
        'title': 'Hello/index',
        'msg' : 'これは次のページだよん',
        'goto' : 'index',
    }

    return render(request, 'hello/index.html', parms)