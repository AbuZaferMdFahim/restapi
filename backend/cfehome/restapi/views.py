import json
# from django.http import JsonResponse,HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.models import Product
from django.forms.models import model_to_dict

# Create your views here.
@api_view(["GET"])
def api_home(request,*args, **kwargs):
    # API View

    model = Product.objects.all().order_by("?").first() 
    data = {}
    if model:
        data = model_to_dict(model, fields=['id','title','price'])
    return Response(data)