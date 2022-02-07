from django.shortcuts import render
# Create your views here.

def index(request):
    return render(request, 'welcome/welcome.html', context={})

def auth_redir(request):
    return render(request, 'auth/', context={})
