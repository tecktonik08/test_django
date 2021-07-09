from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def index(request):
    path = request.path
    resultstr = ''
    if path == '/home':
        resultstr = '<h1>안녕하세요. HOME 입니다.</h1>'
    else :
        resultstr = '<h1>여기는 main 입니다.</h1>'
    return HttpResponse(resultstr)

def index01(request):
    result = {'n':'HOI', 'f':'K'}
    return render(request, 'index.html', context=result)

def index02(request):
    result = {'n':request.GET['n'], 'f':request.GET['f']}
    return render(request, 'index.html', context=result)