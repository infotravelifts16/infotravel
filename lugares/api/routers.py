from rest_framework.routers import DefaultRouter
from lugares.api.views.lugar_viewset import LugarViewSet

router = DefaultRouter()


router.register(r'lugares', LugarViewSet, basename= 'lugares')

urlpatterns = router.urls

