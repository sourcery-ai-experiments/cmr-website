"""
URL configuration for CMR Layouts app.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from django.urls import path

from cmr_layouts import views

urlpatterns = [
    path('customers/<int:customerID>/', views.customer, name='cmr_customer'),
    path('customers/', views.customers, name='cmr_customers'),
    path('locations/<int:locationID>/', views.location, name='cmr_location'),
    path('locations/', views.locations, name='cmr_locations'),
    path('locomotives/<int:locomotiveID>/', views.locomotive, name='cmr_locomotive'),
    path('locomotives/', views.locomotives, name='cmr_locomotives'),
    path(
        'rollingstock/<int:rollingstockID>/',
        views.rollingstock,
        name='cmr_rollingstock',
    ),
    path('rollingstock/', views.rollingstock_list, name='cmr_rollingsstock_list'),
]
