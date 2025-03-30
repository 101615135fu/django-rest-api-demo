from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Item
from .serializers import ItemSerializer

@api_view(['GET'])
def select_all(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)

# api/views.py
import requests


@api_view(['GET'])
def get_stock_quotes(request):
    url = "https://yahoo-finance15.p.rapidapi.com/api/v1/markets/stock/quotes"
    querystring = {"ticker":"AAPL,MSFT"}

    headers = {
        "x-rapidapi-host": "yahoo-finance15.p.rapidapi.com",
        "x-rapidapi-key": "2dfa727615msh3c6f698544ce015p142450jsn646a1bc337ef"  # ⚠️ 替换为你自己的
    }

    response = requests.get(url, headers=headers, params=querystring)
    return Response(response.json())
