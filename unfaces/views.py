from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    data = {
        'title':'Главная!'
    }
    return render(request, 'unfaces/index.html',data)
def new(request):
    return render(request, 'news/news_home.html')

def text(request):
    dat = {
        'form':form
    }
    return render(request, 'unfaces/new.html', dat)
