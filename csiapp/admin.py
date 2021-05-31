from django.contrib import admin
from . models import Event,Contact,Subscribe,Member

# Register your models here.
admin.site.register(Event)
admin.site.register(Contact)
admin.site.register(Subscribe)
admin.site.register(Member)