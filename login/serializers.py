from rest_framework import serializers
from login.models import SaveString
from django.contrib.auth.models import User
        
class UserSerializer(serializers.ModelSerializer):
    saveString = serializers.StringRelatedField(read_only=True)
    password = serializers.CharField(write_only = True)
    class Meta:
        model = User
        fields = ('username', 'password', 'saveString')
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class SaveStringSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaveString
        fields = ('text', 'pub_date')
    def create(self, validated_data):
        return SaveString.objects.create(**validated_data)