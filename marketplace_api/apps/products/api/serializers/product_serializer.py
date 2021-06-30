from marketplace_api.apps.products.models import Product

from marketplace_api import serializers

class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        exclude = ('state',)
        