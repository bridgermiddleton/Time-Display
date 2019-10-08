from django.shortcuts import render, redirect
from time import gmtime, strftime
def index(request):
    context = {
        "time": strftime("%b %d, %Y %H:%M %p", gmtime())
    }
    return render(request, "time_display/index.html", context)
def timedis(request):
    return redirect("/")
# Create your views here.
