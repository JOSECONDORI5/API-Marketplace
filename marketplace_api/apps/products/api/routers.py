from rest_framework.routers import DefaultRouter
from apps.products.api.serializers.general_serializers import MeasureUnitSerializer, IndicatorSerializer
from apps.products.api.views.product_viewsets import ProductViewSet

router = DefaultRouter()

router.register(r'products', ProductViewSet, basename='products')
router.register(r'measure-unit', ProductViewSet, basename='measure_unit')
router.register(r'indicators', ProductViewSet, basename='indicators')
router.register(r'category-products', ProductViewSet, basename='category_products')

urlpatterns = router.urls
