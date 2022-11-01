from django.urls import path
from lugares.api.views.general_views import LugarUnitListAPIView, IndicatorListAPIView, CategoryLugarListAPIView
#from products.api.views.product_viewset import ProductListCreateAPIView, ProductRetrieveUpdateDestroyAPIView

urlpatterns =  [

    path('lugar_unit/', LugarUnitListAPIView.as_view(), name = 'lugar_unit'),
    path('indicator/', IndicatorListAPIView.as_view(), name = 'indicator'),
    path('category_lugar/',CategoryLugarListAPIView.as_view(), name = 'category_lugar'),
    #path('product/list/', ProductListAPIView.as_view(), name = 'product_list'), JUNTAMOS EL GET Y EL POST EN EL LISTCREATE
    #path('product/', ProductListCreateAPIView.as_view(), name = 'product_create'),
    #path('product/retrieve/<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name = 'product_retrieve_update_destroy'),
]


