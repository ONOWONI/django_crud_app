from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('Hello World, you are my first crud app in django')



def home(request):
    return HttpResponse('Testing the routing function in django')