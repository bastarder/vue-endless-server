#-- coding: utf-8 --

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User

from login.models import SaveString
from login.serializers import SaveStringSerializer,UserSerializer

from rest_framework.decorators import api_view,renderer_classes,authentication_classes,permission_classes
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from collections import OrderedDict


# Create your views here.

@api_view(['POST'])
@renderer_classes((JSONRenderer,))
def signup(request,format = None):
    username = request.data.get('username')

    if User.objects.filter(username = username):
        return Response({
            'error': True,
            'msg': '注册失败! 用户已存在!'
        })
    
    newUser = UserSerializer(
      data = request.data
    )

    if newUser.is_valid():
        newUser.save()
        return Response({
            'user': newUser.data
        })
    else:
        return Response({
            'error': True,
            'msg': '注册失败! 账号或者密码不符合条件!'
        })


@api_view(['POST'])
@renderer_classes((JSONRenderer,))
def signin(request, format = None):

    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(
        username = username, 
        password = password
    )

    if user is not None:
        if user.is_active:
            login(request, user)
            return Response({
                'user' : UserSerializer(user).data,
            })
        else:
            msg = "账号被冻结!"
    else:
        msg = "账号或密码错误!"

    return Response({
        'error': True,
        'msg': msg
    })

