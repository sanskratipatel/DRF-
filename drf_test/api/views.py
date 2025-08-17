from django.shortcuts import render
from rest_framework.response import Response
from  users.models import user 
from .serializers import UsersSerializers
from rest_framework import status
from rest_framework.decorators import api_view



@api_view(['GET'])
def usersView(request):  
    try: 
        if request.method == 'GET':
            # Get data from users all 
            users = user.objects.all() 
            serializer = UsersSerializers(users ,many =True) 
            return Response(serializer.data ,status =status.HTTP_200_OK)
    except Exception as e:
         return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST']) 
def insertusersview(request) : 
    try: 
        serializer = UsersSerializers(data = request.data) 
        if serializer.is_valid(): 
           serializer.save() 
           return Response(serializer.data,status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
    except Exception as e : 
        return Response ({"error": str(e)} , status = status.HTTP_500_INTERNAL_SERVER_ERROR)