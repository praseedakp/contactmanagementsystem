from django.db import models



# Create your models here.

class regmodel(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=20)
    image=models.FileField(upload_to='cms_app/static')
    emailid=models.EmailField()
    addr=models.CharField(max_length=250)
    contact=models.IntegerField()

