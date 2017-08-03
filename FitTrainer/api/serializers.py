from rest_framework import serializers
from .models import Exercise

class ExerciseSerializer(serializers.ModelSerializer):
    """Serializer to map Model instance into JSON format."""
    class Meta:

        model = Exercise
        fields = ('id', 'name', 'muscleGroupId', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')
