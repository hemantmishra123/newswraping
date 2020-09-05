from django.urls import path
from.import views

urlpatterns = [
    path('',views.home , name="home"),
    path('addhome/',views.addhome,name="addhome"),
    path('dataflow/',views.dataflow,name="dataflow")
]
