from django.urls import path
from. import views
app_name = 'shop'

urlpatterns=[
    path('', views.allProdCat,name='allProdcat'),
    path('shop/<slug:c_slug>/',views.allProdCat, name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/',views.proDetail, name='prodCatdetail'),
    path('allprodcat/',views.allProdCat, name='allProdCat'),
]