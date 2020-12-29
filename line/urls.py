from django.urls import path
from.import views

urlpatterns = [
    path('',views.home , name="home"),
    path('addhome/',views.addhome,name="addhome"),
    path('dataflow/',views.dataflow,name="dataflow"),
    path('graph/',views.graph,name="graph")
    #path("datalab/",views.datalab,name="datalb"),
]

