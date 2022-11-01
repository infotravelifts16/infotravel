from django.db import models
from base.models import BaseModel
from simple_history.models import HistoricalRecords

class LugarUnit(BaseModel):
    description = models.CharField('Descripción', max_length=50, blank=False, null=False, unique=True)
    historical = HistoricalRecords()

    @property
    def _histoty_user(self):
        return self.changed_by
    
    @_histoty_user.setter
    def _history_user(self, value):
        self.changed_by = value
    
# Create your models here.
    class Meta:
        verbose_name = 'Lugar Unit'
        verbose_name_plural = 'Lugares Units'




    def __str__(self):

        return self.description

class CategoryLugar(BaseModel):
    description = models.CharField('Description', max_length = 50, blank = False, null = False, unique = True)
    historical = HistoricalRecords()

    @property
    def _histoty_user(self):
        return self.changed_by
    
    @_histoty_user.setter
    def _history_user(self, value):
        self.changed_by = value

    
# Create your models here.
    class Meta:
        verbose_name = 'Categoria de Lugar'
        verbose_name_plural = 'Categorias de Lugares'

    def __str__(self):

        return self.description


class Indicator(BaseModel):
    descount_value = models.PositiveSmallIntegerField(default = 0)
    category_lugar = models.ForeignKey(CategoryLugar, on_delete=models.CASCADE, verbose_name = 'Indicador de Oferta')
    historical = HistoricalRecords()

    @property
    def _histoty_user(self):
        return self.changed_by
    
    @_histoty_user.setter
    def _history_user(self, value):
        self.changed_by = value


    class Meta:
        verbose_name = 'Indicador de Oferta'
        verbose_name_plural = 'Indicadores de Ofertas'

    def __str__(self):
        return f'Oferta de la categoría {self.category_lugar} : {self.descount_value}%' 


class Lugar(BaseModel):
    """Model definition for Lugar."""

    name = models.CharField('Nombre de Lugar', max_length=150, unique=True, blank=False, null=False)
    description = models.TextField('Descripción del Lugar', blank=False, null=False)
    image = models.ImageField('Imagen del Lugar', upload_to='lugares/', blank=True, null=True)
    lugar_unit = models.ForeignKey(LugarUnit, on_delete=models.CASCADE, verbose_name='Lugar Unit', null=True)
    category_lugar = models.ForeignKey(CategoryLugar, on_delete=models.CASCADE, verbose_name='Categoria del Lugar', null=True)
    historical = HistoricalRecords()

    @property
    def _histoty_user(self):
        return self.changed_by
    
    @_histoty_user.setter
    def _history_user(self, value):
        self.changed_by = value


    class Meta:
        """Meta definition for Lugar."""

        verbose_name = 'Lugar'
        verbose_name_plural = 'Lugares'

    def __str__(self):
        """Unicode representation of Lugar."""
        return self.name
