from django.db import models

#Create your models here.craete django models for 
#how to create django models for the data inserting into the database fo the given table.
class Todoitem(models.Model):
    #it is the table of the data that is store inside my databse of the programme
    content=models.TextField()
    data1=models.IntegerField()
    data2=models.IntegerField()
    data3=models.IntegerField()
    data4=models.IntegerField()
    data5=models.IntegerField()

#raw data
#class field    Data-->Field
#Name     #subj1#     #subj2#     #subj3#    #subj4#      #subj5#       INTEGER-field
#############################################################################
#Hemant   DS->50    DBMS->76   CD->93   MATH->98  DATALAB->95   id=1
#Anant    DATA      databse    CD       MATH      DATALAB       id=2
#Mukesh   DATA      DATABSE    CD       MATH      DATALAB       id=3     
#Anmol                                                          id=4    
#Priyanka                                                       id=5   