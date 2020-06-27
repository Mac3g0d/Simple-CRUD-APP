from rest_framework import serializers
from .models import CRUD_api


class CRUD_apiSerializer(serializers.Serializer):
    name = serializers.CharField()
    surname = serializers.CharField()
    phone = serializers.CharField()
    position = serializers.CharField()


    def create(self, validated_data):
        return CRUD_api.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.surname = validated_data.get('surname', instance.surname)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.position = validated_data.get('position', instance.position)
        instance.save()

        return instance
