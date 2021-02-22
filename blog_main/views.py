from django.shortcuts import render, redirect
from django.http import HttpResponse



def home(request) :

    for key, value in request.session.items(): 
        print('{} => {}'.format(key, value))

    return render(request, 'front/index.html')

def category(request) :

    return render(request, 'front/category.html')

def detail(request) :

    return render(request, 'front/detail.html')












