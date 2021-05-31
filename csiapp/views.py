from django.shortcuts import render
from .models import Event,Member




def home(request):
    
    return render(request,'home.html')




def aboutus(request):
    return render(request,'aboutus.html')



def contactus(request):
    return render(request,'contact-us.html')



def events(request):
    return render(request,'events.html')


def eventdetails(request,name_slug):
    return render(request,'event-detail.html')

def team(request):
    context={
        
    }
    return render(request,'team-member.html',context)
