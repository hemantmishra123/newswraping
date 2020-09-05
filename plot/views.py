from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from.models import Todoitem

#create with django model data.
#it is the function for relating the data inside my templates.
def home(request):
    objects=Todoitem.objects.all()   
    return render(request,'show.html',{'dataset':objects})
def addhome(request):
    newitem=Todoitem(content=request.POST.get('name')) 
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





