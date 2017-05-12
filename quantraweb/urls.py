"""quantraweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView

from stock import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='container2.html')),

    url(r'^api/stock/date_range', views.date_range),
    url(r'^api/stock/market', views.market),
    url(r'^api/stock/stock_list', views.stock_list),
    url(r'^api/stock/stock', views.stock),

    url(r'^api/stock/charts/volume_chart', views.volume_chart),
    url(r'^api/stock/charts/macd_chart', views.macd_chart),
    url(r'^api/stock/charts/kdj_chart', views.kdj_chart),
    url(r'^api/stock/charts/boll_chart', views.boll_chart),
    url(r'^api/stock/charts/psy_chart', views.psy_chart),

    url(r'^ws/realtime_price', views.realtime_price),
]
