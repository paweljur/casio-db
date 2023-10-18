from django.http import HttpResponse
from .models import Message

def hello_world(request):
    try:
        message = Message.objects.first().content
    except AttributeError:
        message = "Theres nothing to display"
    return HttpResponse(message)