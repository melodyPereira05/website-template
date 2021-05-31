from django.urls import path
from  . import views

app_name='csitsec'

urlpatterns = [

    path('',views.home, name="home"),
    path('about/',views.aboutus, name="aboutus"),
    path('contact/',views.contactus, name="contactus"),
    path('events/',views.events, name="event"),
    path('eventdetails/<slug:name_slug>/',views.eventdetails, name="eventdetail"),
    path('team/',views.team, name="team"),
    
    #path('',views., name=""),
   
   
   
    
    
    
    
    
]