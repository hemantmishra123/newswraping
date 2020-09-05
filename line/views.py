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
    objects=Todoitem.objects.all()   
    return render(request,'show.html',{'dataset':objects})
def graph(request):
    li=[]
    var=int(request.POST.get('graph'))
    temp=Todoitem.objects.get(id=var)
    setter=[100,100,100,100,100]
    li.append(temp.data1)
    li.append(temp.data2)
    li.append(temp.data3)
    li.append(temp.data4)
    li.append(temp.data5)
    plt.axes().spines['bottom'].set_position(('data',0))
    fig=plt.gcf()
    plt.axes().spines["left"].set_position(('data',0))
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