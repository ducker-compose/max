from rest_framework import serializers

class Register(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

