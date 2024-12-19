from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.
def hello(request):
    return HttpResponse("Привет, это главнае страница написанная на фрейморке Джанго")

def about(request):
    return HttpResponse("Здесь будет информация о нас")

def contacts(request):
    return HttpResponse("А тут будет контактная информация")

