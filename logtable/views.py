from django.shortcuts import render

def home(request):
    return render (request, 'register.html')


def create_account(request):
    return render(request, 'admin.home.html')