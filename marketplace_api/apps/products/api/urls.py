from django.urls import path
from apps.products.api.views.general_views import MeasureUnitListAPIView

urlpatterns = [
    path('measure_unit/', MeasureUnitListAPIView.as_view(), name='measure_unit'),
]
