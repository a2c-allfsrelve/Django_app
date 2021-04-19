
from django.shortcuts import render
from django.http import HttpResponse
from .forms import HelloForm
from .forms import HelloForm2
from django.views.generic import TemplateView


class HelloView(TemplateView):
    
    def __init__(self):
        self.params = {
            'title': 'Hello/Index',
            'message ' : 'ゆあでーた：',
            'form' : HelloForm(),
            'form2' : HelloForm2(),
            'result': None
        }

    #GETメソッド
    def get(self, request):
        return render(request, 'hello/index.html', self.params)
        
    #POSTメソッド
    def post(self, request):
        msg = 'あなたは' + request.POST['name'] + '(' + request.POST['age'] + ')さんです。'\
            '<br>メアドは、:' + request.POST['mail'] + 'だね。'
        self.params['message'] = msg
        self.params['form'] = HelloForm(request.POST) #フォームもこうやってとってこれるからいいいね。

        return render(request, 'hello/index.html', self.params) 


    def post(self, request):
        ch = request.POST['choise']
        self.params['result'] = 'selected : ' + ch + '.'
        self.params['form'] = HelloForm2(request.POST)
        
        return render(request, 'hello/index.html', self.params)






# def index(request):
#     params = {
#         'title': 'Hello/Index',
#         'message ' : 'ゆあでーた：',
#         'form' : HelloForm(),       
#     }
#     if (request.method == 'POST'): #indexをPOSTでも呼ぶことができる
#         params['message'] = '名前:' + request.POST['name'] + \
#             '<br>メール:' + request.POST['mail'] + \
#             '<br>年齢:' + request.POST['age']
#         params['form'] = HelloForm(request.POST)

#     return render(request, 'hello/index.html', params) #settings.pyを忘れるな

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