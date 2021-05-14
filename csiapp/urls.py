from django.urls import path
from  . import views

app_name='csitsec'

urlpatterns = [

    path('',views.home, name="home-page"),
    path('about/',views.aboutus, name="aboutus-page"),
    path('contact/',views.contactus, name="contactus-page"),
    path('events/',views.events, name="event-page"),
    path('eventdetails/<int:id>',views.eventdetails, name="eventdetail-page"),
    path('team/',views.team, name="team-page"),
    #path('',views., name=""),
   
   
   
    
    
    
    
    
]