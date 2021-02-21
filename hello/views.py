
from django.shortcuts import render
from django.http import HttpResponse
from .forms import HelloForm

def index(request):
    params = {
        'title': 'Hello/Index',
        'msg' : 'おっぱいに吸いつきたい。',
        'form' : HelloForm(),       
    }
    if (request.method == 'POST'): #indexをPOSTでも呼ぶことができる
        params['message'] = '名前:' + request.POST['name'] + \
            '<br>メール:' + request.POST['mail'] + \
            '<br>年齢:' + request.POST['age']
        params['form'] = HelloForm(request.POST)

    return render(request, 'hello/index.html', params) #settings.pyを忘れるな

# def next(request):
#     parms = {
#         'title': 'Hello/index',
#         'msg' : 'これは次のページだよん',
#         'goto' : 'index',
#     }

#     return render(request, 'hello/index.html', parms)

# def form(request):
#     msg = request.POST['msg']
#     params = {
#         'title' : 'Hello/form',
#         'msg' : 'こんにちは' + msg + 'さん'
#     }
#     return render(request, 'hello/index.html', params)