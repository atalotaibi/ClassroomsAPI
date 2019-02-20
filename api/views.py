from django.shortcuts import render
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView,
)
from .serializers import (
    ClassroomListSerializer,
    ClassroomtDetailSerializer,
    ClassroomCreateUpdateSerializer,
)
from classes.models import Classroom

class ClassroomListView(ListAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomListSerializer


class ClassroomDetailView(RetrieveAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomtDetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'classroom_id'


# Complete Me
class ClassroomCreateView(CreateAPIView):
    serializer_class = ClassroomCreateUpdateSerializer

    def perform_create(self, serializer):
        serializer.save(teacher = self.request.user)


class ClassroomUpdateView(RetrieveUpdateAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomCreateUpdateSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'classroom_id'


class ClassroomDeleteView(DestroyAPIView):
    queryset = Classroom.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'classroom_id'