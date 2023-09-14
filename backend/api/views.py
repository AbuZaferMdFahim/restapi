from django.http import JsonResponse,HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
import json
from django.forms.models import model_to_dict
from products.models import Product
from products.serializers import ProductSerializer

@api_view(["POST"])
def api_home(request,*args, **kwargs):
    #request --> HTTPRequest --> Django
    #request.body
    #print dirr request
    #print(request.GET)
    #print(request.POST)
    #body=request.body # byte string  json data
    #data = {}
    #try:
    #    data = json.loads(body) # string of json data -> python dictionary
    #except:
    #    pass
    #print(data)
    #data['params'] = dict(request.GET)
    #data['headers'] = dict(request.headers) #request.META -->
  
    #data['content_type'] = request.content_type 
    #return JsonResponse(data)
    # api view
    # if request.method != "POST":
    #     return Response({"detail": "GET not allowed"},status=405)
    # model_data = Product.objects.all().order_by("?").first()
    # data = {}
    # if model_data:
    #     data = model_to_dict(model_data,fields=['id','title','price','sale_price'])
        #json_data_str = json.dumps(data)  
        # data['id'] = model_data.id
        # data['title'] = model_data.title
        # data['content'] = model_data.content
        # data['price'] = model_data.price

        #model instance(model_data)
        #turn a python dict
        #return JSON to my client
        #serialization
    # return Response(data)    
    #return HttpResponse(json_data_str,headers={'contnt-type':"application/json"})
    # instance = Product.objects.all().order_by("?").first()
    # data = {}
    # if instance:
    #     #data = model_to_dict(instance,fields=['id','title','price','sale_price'])
    #     data = ProductSerializer(instance).data
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        #instance = serializer.save()
        
        #data = serializer.data
        return Response(serializer.data)
    return Response({"incalid": "not good Data"},status=400)