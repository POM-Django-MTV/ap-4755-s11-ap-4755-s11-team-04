from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # template = loader.get_template("book/index.html")
    # return HttpResponse("Hello World. This is the book app")
    return render(request, "book/index.html")