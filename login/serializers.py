from rest_framework import serializers
from login.models import SaveString


class SaveStringSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaveString
        fields = ('user', 'text', 'pub_date')
    def create(self, validated_data):
        return SaveString.objects.create(**validated_data)
    