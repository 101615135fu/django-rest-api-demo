from django.urls import path
from . import views

urlpatterns = [
    path('list/selectAll', views.select_all),
    path('stocks/quotes', views.get_stock_quotes),
]
