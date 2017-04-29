from django.shortcuts import render
from django.http import HttpResponse
import os

def uploadFile(request):
    if request.method=='POST':
        myfile = request.FILES.get('myfile', None)
        if not myfile:
            return HttpResponse("No file")
        dest = open(os.path.join("file", myfile.name), 'wb+')
        for chunk in myfile.chunks():
            dest.write(chunk)
        dest.close()
        return HttpResponse("Success")
def index(request):

    return render(request, 'upload/index.html')


# Create your views here.
