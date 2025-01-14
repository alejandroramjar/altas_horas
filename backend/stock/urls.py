from django.urls import include, path
from rest_framework import routers
from .views import MercanciaViewSet

router = routers.DefaultRouter()
router.register(r'mercancias', MercanciaViewSet)

urlpatterns = [
    path('stk/', include(router.urls))
    ]