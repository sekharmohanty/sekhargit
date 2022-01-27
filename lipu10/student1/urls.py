from unicodedata import name
from django.urls import path
from . import views
urlpatterns = [
    
    path('',views.home,name='home'),
    path('student/<int:id>/',views.delete,name='delete'),
    path('<int:id>/',views.update,name='update')
   
]
