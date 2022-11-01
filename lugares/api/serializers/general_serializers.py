from lugares.models import LugarUnit, CategoryLugar,Indicator

from rest_framework import serializers

class LugarUnitSerializer(serializers.ModelSerializer):

    class Meta:
        model = LugarUnit
        exclude = ('state','created_date', 'modified_date')

class CategoryLugarSerializer(serializers.ModelSerializer):

    class Meta:
        model = CategoryLugar
        exclude = ('state','created_date', 'modified_date')

class IndicatorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Indicator
        exclude = ('state','created_date', 'modified _date')
