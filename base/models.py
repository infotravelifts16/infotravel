from simple_history.models import HistoricalRecords
from django.db import models


class BaseModel(models.Model):
    id = models.AutoField(primary_key = True)
    state = models.BooleanField('Estado', default = True)
    created_date = models.DateField('Fecha de Creacion', auto_now=False, auto_now_add= True)
    modified_date = models.DateField('Fecha de Modificacion', auto_now=True, auto_now_add= False)
    #deleted_date = models.DateField('Fecha de Eliminacion', auto_now=False, auto_now_add= False)
    historical = HistoricalRecords()

    @property
    def _histoty_user(self):
        return self.changed_by
    
    @_histoty_user.setter
    def _history_user(self, value):
        self.changed_by = value



    class Meta:
        verbose_name = 'Modelo Base'
        verbose_name_plural = 'Modelos Base'
