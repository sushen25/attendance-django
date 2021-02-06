from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=64, blank=False)
    last_name = models.CharField(max_length=64, blank=False)
    phone = models.CharField(max_length=64, blank=False, null=True)
    year_level = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(12)], blank=False, null=True)
    school = models.CharField(max_length=64, blank=True, null=True)
    parent_name = models.CharField(max_length=64, blank=True, null=True)

