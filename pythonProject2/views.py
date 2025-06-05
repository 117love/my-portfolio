from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world! This myapviews.pyp index page.")