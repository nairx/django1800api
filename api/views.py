from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view()
def getData(request):
    return Response({"message":"Hello World"})
 
@api_view()
def greet(request):
    return Response({"message":"Good Morning"})

@api_view()
def products(request):
    myproducts = [
        {"name":"Product 1","price":34},
        {"name":"Product 2","price":84},
        {"name":"Product 3","price":24}
        ]
    return Response({"products":myproducts})