from django.db import models
from simple_history.models import HistoricalRecords

from apps.base.models import BaseModel


class MeasureUnit(BaseModel):
    """ Model definition for MeasureUnit. """

    # TODO: Define fields here
    description = models.CharField('Descripcion', max_length=50, blank=False, null=False, unique=True)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        """ Meta definition for MeasureUnit. """

        verbose_name = 'Unidad de Medida'
        verbose_name_plural = 'Unidades de Medida'

    def __str__(self):
        """ Unicode representation of MeasureUnit. """
        return self.description


class CategoryProduct(BaseModel):
    """ Model definition for CategoryProduct. """

    # TODO: Define fields here
    description = models.CharField('Descripcion', max_length=50, blank=False, unique=True)
    measure_unit = models.ForeignKey(MeasureUnit, on_delete=models.CASCADE, verbose_name='Unidad de Medidda')
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        """ Meta definition for MeasureUnit. """

        verbose_name = 'Categoria de Producto'
        verbose_name_plural = 'Categorias de Productos'

    def __str__(self):
        """ Unicode representation of MeasureUnit. """
        return self.description


# This class indicates which offer is assigned to which product category
class Indicador(BaseModel):
    """Model definition for Indicador."""

    # TODO: Define fields here
    descount_value = models.PositiveSmallIntegerField(default=0)
    category_product = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE, verbose_name='Indicador de Oferta')
    historical = HistoricalRecords()
    
    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        """Meta definition for Indicador."""

        verbose_name = 'Indicador de Oferta'
        verbose_name_plural = 'Indicadores de Ofertas'

    def __str__(self):
        """Unicode representation of Indicador."""
        return f'Oferta de la Categoria {self.category_product}: {self.descount_value}%'


class Product(models.Model):
    """Model definition for Product."""

    # TODO: Define fields here
    name = models.CharField('Nombre de producto', max_length=150, unique=True, blank=False, null=False)
    description = models.TextField('Description del producto', blank=False, null=False)
    image = models.ImageField('Imagen del producto', upload_to='products/', blank=True, null=True)
    historical = HistoricalRecords()
    
    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value
        
    class Meta:
        """Meta definition for Product."""

        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        """Unicode representation of Product."""
        return self.name
