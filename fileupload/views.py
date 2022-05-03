from .models import StoreDoc
from .serializers import StoreDocSerializer
from rest_framework import viewsets


class StoreDocViewSet(viewsets.ModelViewSet):
    queryset = StoreDoc.objects.all()
    serializer_class = StoreDocSerializer
