from  django.urls import path 
from . import views


urlpatterns  = [  
    path('user',views.usersView), 
    path('userinsert',views.insertusersview)
]