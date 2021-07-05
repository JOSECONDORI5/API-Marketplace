from django.urls import path
from apps.products.api.views.general_views import MeasureUnitListAPIView, CategoryProductListAPIView, \
    IndicatorListAPIView
from apps.products.api.views.product_views import ProductListAPIView, ProductCreateAPIView, ProductRetrieveAPIView, \
    ProductDestroyAPIView

urlpatterns = [
    path('measure_unit/', MeasureUnitListAPIView.as_view(), name='measure_unit'),
    path('indicator/', IndicatorListAPIView.as_view(), name='indicator'),
    path('category_product/', CategoryProductListAPIView.as_view(), name='category_product'),
    path('product/list/', ProductListAPIView.as_view(), name='product'),
    path('product/create/', ProductCreateAPIView.as_view(), name='product_create'),
    path('product/retrieve/<int:pk>/', ProductRetrieveAPIView.as_view(), name='product_retrieve'),
    path('product/destroy/<int:pk>/', ProductDestroyAPIView.as_view(), name='product_destroy')
]

# TODO: 22