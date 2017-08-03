from django.test import TestCase
from .models import Exercise
from rest_framework.test import APIClient
from django.core.urlresolvers import reverse

# Create your tests here.
class ModelTestCase(TestCase):
    """This class defines the test suite for the Exercise model."""

    def setUp(self):
        """Define the test client and other test variables"""
        self.exercise_name = "Bench Press"
        self.muscle_number = 3
        self.exercise = Exercise(name=self.exercise_name, muscleGroupId=self.muscle_number)

    def test_model_can_create_an_exercise(self):
        """Test the exercise model can create an exercise."""
        old_count = Exercise.objects.count()
        self.exercise.save()
        new_count = Exercise.objects.count()
        self.assertNotEqual(old_count, new_count)

class ViewTestCase(TestCase):
    """Test suite for API views."""
    def setUp(self):
        self.client = APIClient()
        self.exercise_data = {'name': "Bench Press", "muscleGroupId": 0}
        self.response = self.client.post(
            reverse('create'),
            self.exercise_data,
            format="json")

    def test_api_can_create_exercise(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
