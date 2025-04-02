
from django.urls import path
from . import views

app_name = 'ecommerce'





urlpatterns = [
     path('', views.product_list, name='product_list'),
     path('products/<str:product_id>/', views.details, name='product_details'),
     path('products/<slug:slug>/add-review/', views.add_review, name='add_review'),
    # path('dev/', views.dev, name='dev'),
     path('account/', views.account, name='account'),
     path('new_url_r',views.new_url_views, name='home'),
     path('old_url',views.old_url_redirect, name='old url')
]