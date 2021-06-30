from marketplace_api.apps.products.models import MeasureUnit, CategoryProduct, Indicador

from marketplace_api import serializers

class MeasureUnitSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MeasureUnit
        exclude = ('state',)
    
class CategoryProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CategoryProduct
        exclude = ('estate',)
    
class IndicadorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Indicador
        exclude = ('state')