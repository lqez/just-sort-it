from django.http import HttpResponse


def welcome(request):
    return HttpResponse('welcome page')

def webhook(request):
    return HttpResponse('webhook page')
