from django.urls import path
from .views import ProductView, main


urlpatterns = [
    path('api/v0/products/', ProductView.as_view(), name='products'),

    # html
    path('', main)
]