from django.shortcuts import render
from .models import Message

def hello_world(request):
    try:
        message = Message.objects.first().content
    except AttributeError:
        message = "Theres nothing to display"
    
    context = {'message': message}
    return render(request, 'casio_db/hello_world.html', context)