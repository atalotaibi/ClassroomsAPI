from rest_framework import serializers
from classes.models import Classroom

class ClassroomListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = [
            'subject',
            'year',
            'teacher',
            ]


class ClassroomtDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = '__all__'

class ClassroomCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = '__all__'