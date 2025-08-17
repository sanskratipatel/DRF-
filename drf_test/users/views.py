from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from users.models import user
# Create your views here.

def users(requests) :
    # users =[ 
    #     {"name":"abhi" , "id": 3}
    # ]
    users = user.objects.all()  
    user_list = list(users.values())
    print("here===================",user)
    return JsonResponse(user_list,safe =False) 

