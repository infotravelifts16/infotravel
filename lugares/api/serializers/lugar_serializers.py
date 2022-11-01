from rest_framework import serializers
from lugares.models import Lugar
from lugares.api.serializers.general_serializers import LugarUnitSerializer, CategoryLugarSerializer


class LugarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lugar
        exclude = ('state','created_date', 'modified_date')

    def to_representation(self, instance):
        return{
            'id': instance.id,
            'name': instance.name,
            'description': instance.description,
            'image': instance.image if instance.image != '' else '',
            'lugar_unit': instance.lugar_unit.description if instance.lugar_unit is not  None else '',
            'category_product': instance.category_lugar.description if instance.category_lugar is not None else '',

        }