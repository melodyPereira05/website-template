from django.db import models

# Create your models here.


class Member(models.Model):
    STATUS_CHOICES=(
        ('scom','Scom'),
        ('jcom','Jcom')
    )
    full_name=models.CharField(max_length=200)
    designation=models.CharField(max_length=200)
    member_type=models.CharField(max_length=10,choices=STATUS_CHOICES,default='jcom')
    member_photo=models.ImageField(upload_to='photos/seller/%Y/%m/%d/')
    instagram=models.CharField(max_length=200,blank=True)
    linkedin=models.CharField(max_length=200,blank=True)
    facebook=models.CharField(max_length=200,blank=True)
    
    
    def __str__(self):
        return self.full_name
    
    
    
    
class Event(models.Model):
    event_name=models.CharField(max_length=200)
    description=models.CharField(max_length=1000)
    start_date=models.CharField(max_length=200)
    end_date=models.CharField(max_length=200)
    main_photo=models.ImageField(upload_to='photos/main/%Y/%m/%d/')
    photo1=models.ImageField(upload_to='photos/optional/%Y/%m/%d/',blank=True)
    photo2=models.ImageField(upload_to='photos/optional/%Y/%m/%d/',blank=True)
    photo3=models.ImageField(upload_to='photos/optional/%Y/%m/%d/',blank=True)
    photo4=models.ImageField(upload_to='photos/optional/%Y/%m/%d/',blank=True)
    photo5=models.ImageField(upload_to='photos/optional/%Y/%m/%d/',blank=True)
    photo6=models.ImageField(upload_to='photos/optional/%Y/%m/%d/',blank=True)
    photo7=models.ImageField(upload_to='photos/optional/%Y/%m/%d/',blank=True)
    photo8=models.ImageField(upload_to='photos/optional/%Y/%m/%d/',blank=True)
    #countdown timer when next event starts
    
    
    
    # class Subscribe(models.Model):
    #     email=models.EmailField()
    
    # def __str__(self):
    #     return self.email