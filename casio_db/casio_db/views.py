from django.shortcuts import render
from .models import Message

def hello_world(request):
    messageObj = Message.objects.first()
    if(messageObj):
        message = messageObj.content
    else:
        message = "Theres nothing to display"
    
    context = {'message': message}
    return render(request, 'casio_db/hello_world.html', context)