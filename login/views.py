from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from login.models import SaveString
from login.serializers import SaveStringSerializer

# Create your views here.

class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def save_list(request):
    if request.method == 'GET':
        ss = SaveString.objects.all()
        serializer = SaveStringSerializer(ss, many=True)
        print(serializer.data)
        return JSONResponse(serializer.data)