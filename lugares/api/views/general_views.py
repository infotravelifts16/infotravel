from base.api import GeneralListApiView
from lugares.api.serializers.general_serializers import LugarUnitSerializer, IndicatorSerializer, CategoryLugarSerializer


class LugarUnitListAPIView(GeneralListApiView):
    serializer_class = LugarUnitSerializer
    
class IndicatorListAPIView(GeneralListApiView):
    serializer_class = IndicatorSerializer

class CategoryLugarListAPIView(GeneralListApiView):
    serializer_class = CategoryLugarSerializer
    



