from django.shortcuts import render





def home(request):
    return render(request,'home.html')




def aboutus(request):
    return render(request,'aboutus.html')



def contactus(request):
    return render(request,'contactus.html')



def events(request):
    return render(request,'events.html')


def eventdetails(request):
    return render(request,'event-detail.html')

def team(request):
    context={
        
    }
    return render(request,'team-member.html',context)