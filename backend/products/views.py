from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.models import Product
from django.shortcuts import get_object_or_404
from products.serializers import ProductSerializer 

class ProductListCreateApiView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(content=content)

class ProductDetailApiView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductUpdateApiView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    
    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title

class ProductDestroyApiView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    
    def perform_destroy(self, instance):
        #instance
        super().perform_destroy(instance)


@api_view(['GET','POST'])
def product_all_view(request,pk=None,*args,**kwargs):
    method = request.method

    if method == "GET":
        if pk is not None:
            #get Request -> detail view
            obj = get_object_or_404(Product,pk=pk)
            data = ProductSerializer(obj, many = False).data
            return Response(data)
        else:
            #list view 
            queryset = Product.objects.all()
            data = ProductSerializer(queryset,many=True).data
            return Response(data)
    if method =="POST":
        # create an item
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content') or None
            if content is None:
                content = title
            serializer.save(content=content)
            return Response(serializer.data)
        return Response({"incalid": "not good Data"},status=400)