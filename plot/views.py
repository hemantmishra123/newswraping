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
    var=int(request.POST.get('graph'))
    temp=Todoitem.objects.get(id=var)
    ptr=temp.data
    ptr2=temp.data2
    plt.axes().spines['bottom'].set_position(('data',0))
    fig=plt.gcf()
    plt.axes().spines["left"].set_position(('data',0))
    fig=plt.gcf()
    plt.plot(ptr,ptr2,color='r')
    fig=plt.gcf()
    plt.scatter(ptr,ptr2)
    fig=plt.gcf()
    buf=io.BytesIO()
    fig.savefig(buf,format="png")
    buf.seek(0)
    string=base64.b64encode(buf.read())
    uri=urllib.parse.quote(string)
    return render(request,'graph.html',{'data':uri})
def addhome(request):
    newitem=Todoitem(content=request.POST.get('name'),data=request.POST.get('data'),data2=request.POST.get('data2')) 
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
