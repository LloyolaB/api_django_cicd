from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

def indexLanding(request):
    return render(request,template_name="index.html")

@api_view(['GET'])
def hello_world(request):
    return Response({"message": "Hello World!"})