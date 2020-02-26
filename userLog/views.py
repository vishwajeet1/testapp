from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from userLog.models import User
from userLog.serializers import UserSerializer
from rest_framework.decorators import api_view
from django.conf import settings
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@api_view(["POST"])
def regUser(request):
    '''
    :param body: {"email":"abcd@gmail.com","mobile":7375677655,"firstName":"newUser","lastName":"verma","password":"abx"}
    '''
    data=request.data
    try:
        try:
            phone_no=User.objects.get(mobile=data['phone_no'])
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"error":"User already exist"})
        except: 
            user=User.objects.create(firstName=data['firstName'],lastName=data['lastName'],mobile=data['mobile'],email=data['email'],password=data['password'])
            user.save()
            name=data['firstName']+" "+data['lastName']
            return Response(status=status.HTTP_200_OK, data={'username': name,'mobile': data['mobile'],'email': user.email})
    except Exception as e:   
        s = "Error {0}".format(str(e)) # string
        msg = s.encode("utf-8")
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"error":msg})

@api_view(["POST"])
def logUser(request):
    '''
    :param body: {"phone_no":7375677655}
    '''
    try:
        data=request.data
        try:
            user=User.objects.get(mobile=data['phone_no'])
            password=user.password
            if(data['password']==password):
                name=user.firstName+" "+user.lastName
                return Response(status=status.HTTP_200_OK, data={'username': name,'phone_no': user.mobile,'email': user.email})
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={"error":"password not match"})    
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"error":"User doen't exist"})
        
    except Exception as e:   
        s = "Error {0}".format(str(e)) # string
        msg = s.encode("utf-8")
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"error":msg})

@api_view(['POST']) 
def admin_del(request):
    '''
    :param body{userName:"xxx",password:"xyz"}
    '''
