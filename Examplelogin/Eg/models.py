
# myapp/models.py
from django.db import models
class UserProfile(models.Model):
    email = models.EmailField()
    full_name = models.CharField(max_length=100)
    age = models.CharField(max_length=15)
    highest_education = models.CharField(max_length=40)
    institute=models.CharField(max_length=40)
    country = models.CharField(max_length=50)
    dept= models.CharField(max_length=20)
    work_exp= models.CharField(max_length=100)
    inscanada= models.CharField(max_length=100) 
    POS= models.CharField(max_length=50)
    feepaid= models.CharField(max_length=50)
    amount=models.IntegerField
    completed_gic=models.CharField(max_length=10)
    gicamount=models.IntegerField
    read = models.IntegerField 
    write=models.IntegerField
    speak=models.IntegerField
    listen=models.IntegerField
    
    
    def __str__(self):
        return self.full_name
    class Meta:  
        db_table = "UserProfile"
