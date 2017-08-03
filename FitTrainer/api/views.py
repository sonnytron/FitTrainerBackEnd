from django.shortcuts import render
from rest_framework import generics
from .serializers import ExerciseSerializer
from .models import Exercise

# Create your views here.
class CreateView(generics.ListCreateAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer

    def perform_create(self, serializer):
        serializer.save()
