from django.http import HttpResponse

def hello(request):
    return HttpResponse('Welcome to my world !')