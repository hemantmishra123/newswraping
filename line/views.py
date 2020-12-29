from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from.models import Todoitem
import matplotlib.pyplot as plt
import io
import math
import urllib,base64
#create with django model data.
#it is the function for relating the data inside my templates.
def home(request):
    #let craete a list of all the isnerting item and do.
    todo=[]
    li=[]
    objects=Todoitem.objects.all()   
    return render(request,'show.html',{'dataset':objects})
def graph(request):
    #variable=int(request.POST.get('graph'))
    li=[]
    ptr=[]
    var=int(request.POST.get('graph'))
    temp=Todoitem.objects.get(id=var)
    #setter list of the data
    setter=[100,100,100,100,100]
    #getter list fo the data
    getter=[30,30,30,30,30]
    #It is the different entity of the table inside my databse and it is the list of the table i am fteching through
    #the table 
    # Name    subjects[MATH DBMS DS ALG CD]
    # student name is The-->Text FielD 
    # data1,data2,data3,data4,data5 ->is the integer Field
    ptr.append(2*temp.data1)
    #data is passing to blog of the instruction for.
    #data
    li.append(temp.data1)
    ptr.append(2*temp.data2)
    li.append(temp.data2)
    ptr.append(2*temp.data3)
    li.append(temp.data3)
    ptr.append(2*temp.data4)
    li.append(temp.data4)
    ptr.append(2*temp.data5)
    li.append(temp.data5)
    plt.axes().spines['bottom'].set_position(('data',0))
    fig=plt.gcf()
    plt.axes().spines["left"].set_position(('data',0))
    fig=plt.gcf()
    #it is the plotter of the graph in XY PLane
    #x->mmarks is obtained in the exam.
    #y->total marks
    
    plt.plot(ptr,li,color='g')
    fig=plt.gcf()
    plt.plot(li,setter,color='r')
    fig=plt.gcf()
    buf=io.BytesIO()
    fig.savefig(buf,format="png")
    buf.seek(0)
    string=base64.b64encode(buf.read())
    uri=urllib.parse.quote(string)
    return render(request,'graph.html',{'data':uri})
def addhome(request):
    newitem=Todoitem(content=request.POST.get('name'),data1=int(request.POST.get('data1')),data2=int(request.POST.get('data2')),data3=int(request.POST.get('data3')),data4=int(requets.POST.get('data4')),data5=int(request.POST,get('data5'))) 
    newitem.save()
    objects=Todoitem.objects.all()
    return render(request,'home.html',{'dataset':objects})
#it is the dataflow set for saving a new node in my list
def dataflow(request):
    #it is the programme for contating a new object in my list of the given data
    node=Todoitem(content=requets.Get.get('data'))
    node.save()
    objects=Todoitem.objects.all()
    return HttpResponseRedirect("/thanks/")
def function(request):
    limit=[]
    #limit h--> 0 for every dataset for given blocks for opening field  equation for delta blocks.
    #for the site of the operation for the previous set.
    







