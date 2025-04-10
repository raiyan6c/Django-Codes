from django.http import HttpResponse

def home(request):
    return HttpResponse('This is the Home page.')
def contact(request):
    return HttpResponse('This is the Contact page.')
