from rest_framework import viewsets
from .serializers import MercanciaSerializer
from .models import Mercancia

class MercanciaViewSet(viewsets.ModelViewSet):
    queryset = Mercancia.objects.all()
    serializer_class = MercanciaSerializer
