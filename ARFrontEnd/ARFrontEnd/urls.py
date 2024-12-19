"""
URL configuration for ARFrontEnd project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from OMS.views import ulogin, home, verify_password, password, ulogout, home_view, order_book_view, strategy_list, get_symbols, get_expiry, get_strikes, add_strategy, trade_book_view, net_position_view, strategy_net_position_view, strategy_watchlist , modify_order, cancel_order, place_order, get_market_depth

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", ulogin, name='ulogin'),
    path("home", home, name='home'),
    path("home_view", home_view, name='home_view'),
    path("password/", password, name='password'),
    path("verify_password/", verify_password, name='verify_password'),
    path("order_book_view/", order_book_view, name='order_book_view'),
    path("trade_book_view/", trade_book_view, name='trade_book_view'),
    path("net_position_view/", net_position_view, name='net_position_view'),
    path("strategy_net_position_view/", strategy_net_position_view, name='strategy_net_position_view'),
    path('strategy-list/', strategy_list, name='strategy_list'),
    path('api/symbols/', get_symbols, name='get_symbols'),
    path('api/expiry/', get_expiry, name='get_expiry'),
    path('api/strikes/', get_strikes, name='get_strikes'),
    path('add-strategy/', add_strategy, name='add_strategy'),
    path('api/modifyOrder/', modify_order, name='modify_order'),
    path('api/cancelOrder/', cancel_order, name='cancel_order'),
    path('api/placeOrder/', place_order, name='place_order'),
    path('strategy-watchlist/', strategy_watchlist, name='strategy_watchlist'),
    path('get_market_depth/', get_market_depth, name='get_market_depth'),
    path("ulogout/", ulogout, name='ulogout'),
]
