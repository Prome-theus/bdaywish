from django.shortcuts import render, HttpResponseRedirect
from core.models import bday
# from .forms import bday

def Home(request):
    data = {}
    try:
        if request.method == "POST":
            fname = request.POST.get('fname')
            lname = request.POST.get('lname')
            msg = request.POST.get('msg')
            song = request.POST.get('song')
            mn = bday(fname = fname,
                      lname = lname,
                      msg = msg,
                      song = song)
            mn.save()
    except:
        pass
        
    return render(request,"home.html")

def main(request):
    return render(request,"bday.html")

# def Home(request):
#     if request.method =="POST":
#         form = bday(request.POST)
#         if form.is_valid():
#             return HttpResponseRedirect("/thanks/")
#         else:
#             form = bday()

#     return render(request, "home.html", {"form" : form })