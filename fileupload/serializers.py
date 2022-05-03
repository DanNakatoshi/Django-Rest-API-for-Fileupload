from rest_framework import serializers
from .models import StoreDoc

class StoreDocSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreDoc
        fields = "__all__"
