from django.db import models

# Create your models here.

class Exercise(models.Model):
    """This class represents the exercise model"""
    name = models.CharField(max_length=255, blank=False, unique=True)
    muscleGroupId = models.IntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a human readable model instance"""
        return "{}".format(self.name)
