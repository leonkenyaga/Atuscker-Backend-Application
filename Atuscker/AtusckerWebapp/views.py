from django.http import JsonResponse
from django.http import HttpResponse
from django.template import loader
from .models import Product
from .serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET','POST'])
def index(request):

  return HttpResponse(request)

def product_list(request):
   if request.method =='GET':
      products = Product.objects.all()
      serializer= ProductSerializer(products, many=True)
      return JsonResponse(serializer.data,safe=False)
   if request.method == 'POST':
      serializer=ProductSerializer(data=request.data)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data, status=status.HTTP_201_CREATED)
      

def specific_product(request):
   products = Product.objects.filter(productname='Trouser')
   serializer= ProductSerializer(products, many=True)
   return JsonResponse(serializer.data,safe=False)

