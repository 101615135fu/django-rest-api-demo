from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Item
from .serializers import ItemSerializer
from django.shortcuts import render
import requests

@api_view(['GET'])
def select_all(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)




# @api_view(['GET'])
# def get_stock_quotes(request):
#     url = "https://yahoo-finance15.p.rapidapi.com/api/v1/markets/stock/quotes"
#     querystring = {"ticker":"AAPL,MSFT"}

#     headers = {
#         "x-rapidapi-host": "yahoo-finance15.p.rapidapi.com",
#         "x-rapidapi-key": "2dfa727615msh3c6f698544ce015p142450jsn646a1bc337ef"  # ⚠️ 替换为你自己的
#     }

#     response = requests.get(url, headers=headers, params=querystring)
#     return Response(response.json())
@api_view(['GET'])
def get_stock_quotes(request):
    url = "https://yahoo-finance15.p.rapidapi.com/api/v1/markets/stock/quotes"
    querystring = {
        "ticker": "AAPL,MSFT,GOOGL,AMZN,META,TSLA,NVDA,JPM,V,JNJ,WMT,PG,BABA,TSM,ORCL"
    }

    headers = {
        "x-rapidapi-host": "yahoo-finance15.p.rapidapi.com",
        "x-rapidapi-key": "2dfa727615msh3c6f698544ce015p142450jsn646a1bc337ef"  # ⚠️ 请替换为你自己的
    }

    response = requests.get(url, headers=headers, params=querystring)
    raw_data = response.json()

    simplified = []
    for stock in raw_data["body"]:
        simplified.append({
            "symbol": stock.get("symbol"),
            "name": stock.get("longName") or stock.get("shortName"),
            "price": stock.get("regularMarketPrice"),
            "change_percent": stock.get("regularMarketChangePercent"),
            "market_cap": stock.get("marketCap"),
            "pe_ratio": stock.get("trailingPE"),
            "volume": stock.get("regularMarketVolume"),
            "currency": stock.get("currency"),
        })

    return Response({"data": simplified})




@api_view(['GET'])
def get_industry_summary(request, industry_name):
    mock_data = {
        "Fintech": {
            "market_size": "720B USD (2024)",
            "top_companies": [
                {"name": "Stripe", "revenue": "14B"},
                {"name": "Square", "revenue": "18B"},
                {"name": "PayPal", "revenue": "30B"},
                {"name": "Revolut", "revenue": "1.5B"},
                {"name": "Robinhood", "revenue": "1.8B"},
                {"name": "Plaid", "revenue": "500M"},
                {"name": "Klarna", "revenue": "1.3B"},
                {"name": "Adyen", "revenue": "7B"},
                {"name": "SoFi", "revenue": "2B"},
                {"name": "Nubank", "revenue": "4B"},
            ],
            "fastest_growing": [
                {"name": "Ramp", "founded": 2020},
                {"name": "Brex", "founded": 2019},
                {"name": "Chime", "founded": 2018}
            ]
        },
        # 可拓展更多行业
        "Healthtech": {
            "market_size": "450B USD (2024)",
            "top_companies": [
                {"name": "Teladoc", "revenue": "2B"},
                {"name": "Amwell", "revenue": "300M"},
                {"name": "Babylon Health", "revenue": "150M"},
                {"name": "Ro", "revenue": "500M"},
                {"name": "Hims & Hers", "revenue": "450M"},
                {"name": "Zocdoc", "revenue": "200M"},
                {"name": "Oscar Health", "revenue": "1.6B"},
                {"name": "Ginger", "revenue": "100M"},
                {"name": "Omada", "revenue": "300M"},
                {"name": "Livongo", "revenue": "800M"},
            ],
            "fastest_growing": [
                {"name": "Modern Health", "founded": 2018},
                {"name": "Cerebral", "founded": 2020},
                {"name": "Lyra Health", "founded": 2019}
            ]
        },

        "Edtech": {
            "market_size": "340B USD (2024)",
            "top_companies": [
                {"name": "Duolingo", "revenue": "400M"},
                {"name": "Coursera", "revenue": "600M"},
                {"name": "Khan Academy", "revenue": "80M"},
                {"name": "Byju’s", "revenue": "1.5B"},
                {"name": "Udemy", "revenue": "700M"},
                {"name": "VIPKid", "revenue": "200M"},
                {"name": "Outschool", "revenue": "100M"},
                {"name": "MasterClass", "revenue": "180M"},
                {"name": "Chegg", "revenue": "500M"},
                {"name": "Skillshare", "revenue": "150M"},
            ],
            "fastest_growing": [
                {"name": "Preply", "founded": 2019},
                {"name": "LingQ", "founded": 2020},
                {"name": "ClassDojo", "founded": 2018}
            ]
        },

        "E-commerce": {
            "market_size": "6.3T USD (2024)",
            "top_companies": [
                {"name": "Amazon", "revenue": "500B"},
                {"name": "Alibaba", "revenue": "150B"},
                {"name": "eBay", "revenue": "10B"},
                {"name": "Shopee", "revenue": "5B"},
                {"name": "JD.com", "revenue": "130B"},
                {"name": "Pinduoduo", "revenue": "50B"},
                {"name": "Mercado Libre", "revenue": "8B"},
                {"name": "Rakuten", "revenue": "12B"},
                {"name": "Flipkart", "revenue": "7B"},
                {"name": "Walmart.com", "revenue": "80B"},
            ],
            "fastest_growing": [
                {"name": "Temu", "founded": 2022},
                {"name": "Thrive Market", "founded": 2019},
                {"name": "Faire", "founded": 2020}
            ]
        },

        "Greentech": {
            "market_size": "1.1T USD (2024)",
            "top_companies": [
                {"name": "Tesla Energy", "revenue": "27B"},
                {"name": "Sunnova", "revenue": "1.5B"},
                {"name": "First Solar", "revenue": "4B"},
                {"name": "Enphase", "revenue": "2.3B"},
                {"name": "Sunrun", "revenue": "1.8B"},
                {"name": "Ørsted", "revenue": "15B"},
                {"name": "NextEra Energy", "revenue": "20B"},
                {"name": "Plug Power", "revenue": "1B"},
                {"name": "Bloom Energy", "revenue": "1.2B"},
                {"name": "Lucid Motors", "revenue": "1.5B"},
            ],
            "fastest_growing": [
                {"name": "Ampd Energy", "founded": 2020},
                {"name": "Arcadia", "founded": 2019},
                {"name": "Octopus Energy", "founded": 2018}
            ]
        },

    }

    industry_name = industry_name.capitalize()  # 防止用户输成 fintech
    if industry_name in mock_data:
        return Response(mock_data[industry_name])
    else:
        return Response({"error": "Industry not found"}, status=404)

def industry_page(request, industry_name):
    return render(request, 'industry.html', context={"default_industry": industry_name})
