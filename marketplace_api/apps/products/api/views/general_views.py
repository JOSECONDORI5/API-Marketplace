from rest_framework import generics
from rest_framework import viewsets
from rest_framework.response import Response

from apps.base.api import GeneralListApiView
from apps.products.models import MeasureUnit, Indicator, CategoryProduct
from apps.products.api.serializers.general_serializers import MeasureUnitSerializer, IndicatorSerializer, CategoryProductSerializer

class MeasureUnitViewSet(viewsets.GenericViewSet):
    """
    Hola desde unidad de medida
    """
    model = MeasureUnit
    serializer_class = MeasureUnitSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state=True)

    def list(self, request):
        """
        Retorna todas las unidades de medida disponibles

        params.
        name → nombre de la unidad de medida
        """
        data = self.get_queryset()
        data = self.get_serializer(data, many=True)
        return Response(data.data)

    def create(self, request):
        return Response({})

class IndicatorViewSet(viewsets.ModelViewSet):
    serializer_class = IndicatorSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state=True)

class CategoryProductViewSet(viewsets.ModelViewSet):
    serializer_class = CategoryProductSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state=True)
