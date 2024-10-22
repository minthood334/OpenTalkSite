from django.shortcuts import render

def index(request):
    return render(request, 'chatapp/index.html')

def rules(request):
    return render(request, 'chatapp/rules.html')
