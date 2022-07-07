from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Stock
from .serializers import StockSerializer
from rest_framework.response import Response

# Create your views here.
@api_view['GET']
def getStockInfo(request):
    stock_info = Stock.objects.all()
    stock_serializer = StockSerializer(stock_info, many=True)

    return Response(stock_serializer.data)
@api_view['POST']
def addStock(request):
    data = request.data
    serializer = StockSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return

