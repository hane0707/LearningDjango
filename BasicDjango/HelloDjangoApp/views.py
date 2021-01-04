from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render

def index(request):
    now = datetime.now()

    return render(
        request,
        "HelloDjangoApp/index.html",  # templatesフォルダ内のhtmlへの相対パス
        {
            'title' : "Hello Django",
            'message' : "Hello Django!",
            'content' : " on " + now.strftime("%A, %d %B, %Y at %X")
        }
    )