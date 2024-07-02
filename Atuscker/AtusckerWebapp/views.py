from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import generics
from .models import Product,ProductImage
from .serializers import ProductSerializer, ProductImageSerializer


@csrf_exempt
def product_list(request):
    """
    List all products, or create a new product.
    """
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
   
@csrf_exempt
def product_detail(request, pk):
    """
    Retrieve, update or delete a product.
    """
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ProductSerializer(product, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        product.delete()
        return HttpResponse(status=204)

@csrf_exempt
class ProductUpdateView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer 


@csrf_exempt   
def productimage_list(request):
    """
    List all productimages, or create a new productimage.
    """
    if request.method == 'GET':
        productimages = ProductImage.objects.all()
        serializer = ProductImageSerializer(productimages, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProductImageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def productimage_detail(request, pk):
    """
    Retrieve, update or delete a product image
    """
    try:
        productimage = ProductImage.objects.get(pk=pk)
    except ProductImage.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ProductImageSerializer(productimage)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ProductImageSerializer(productimage, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        productimage.delete()
        return HttpResponse(status=204)
    
def productwithimages(request, pk):
    if request.method=='GET':
       product = Product.objects.get(pk=pk)
       #productserializer = ProductSerializer(product)
       productimages = ProductImage.objects.filter(product=pk)
       #serializer = ProductImageSerializer(productimages, many=True)
       data = {
           'id':product.id,
           'name':product.name,
           'imageAlt':product.imageAlt,
           'price':product.price,
           'color':product.color,
             'images': [
        {
            'id': image.id,  # Assuming 'ProductImage' model has an 'id' field
            'url': image.imageSrc,  # Assuming 'image' field stores the image URL  # Assuming 'caption' field exists for image description
        }
        for image in productimages
    ]
       }
    return JsonResponse(data)

def specificproductimages(request, pk):
     if request.method=='GET':
       
       productimages = ProductImage.objects.filter(product=pk)
       serializer = ProductImageSerializer(productimages, many=True)
      
     return JsonResponse(serializer.data, safe=False)
