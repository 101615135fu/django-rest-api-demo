from django.urls import path
from . import views

urlpatterns = [
    path('list/selectAll', views.select_all),
    path('stocks/quotes', views.get_stock_quotes),

    # ✅ JSON 数据接口
    path('industry_summary_api/<str:industry_name>', views.get_industry_summary),

    # ✅ 页面 HTML 视图
    path('industry_summary/<str:industry_name>', views.industry_page),
]
