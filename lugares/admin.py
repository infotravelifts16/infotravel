from django.contrib import admin
from lugares.models import *

# Register your models here.
class LugarUnitAdmin(admin.ModelAdmin):
    list_display = ('id', 'description')

class CategoryLugarAdmin(admin.ModelAdmin):
    list_display = ('id', 'description')

admin.site.register(LugarUnit, LugarUnitAdmin)
admin.site.register(CategoryLugar, CategoryLugarAdmin)
admin.site.register(Indicator)
admin.site.register(Lugar)
