from django.http import HttpResponse
from django.shortcuts import render 



def auth(request):
    if request.user.is_authenticated:
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=401)

def home_page(request):
    return render(request,'home_page.html')



