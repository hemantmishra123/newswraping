from django.db import models

#Create your models here.craete django models for 
#how to create django models for the data inserting into the database fo the given table.
class Todoitem(models.Model):
    content=models.TextField()
    data1=models.IntegerField()
    data2=models.IntegerField()
    data3=models.IntegerField()
    data4=models.IntegerField()
    data5=models.IntegerField()