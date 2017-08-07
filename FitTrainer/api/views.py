from rest_framework import viewsets

from .models import Exercise
from .serializers import ExerciseSerializer


# Create your views here.
class CreateView(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer

    def perform_create(self, serializer):
        serializer.save()
