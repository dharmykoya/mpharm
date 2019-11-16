from django.db import models

# Create your models here.

class Diagnosis(models.Model):
    category_code = models.CharField(max_length=500)
    diagnosis_code = models.CharField(max_length=500)
    full_code = models.CharField(max_length=500)
    abbreviated_description = models.CharField(max_length=500)
    full_description = models.CharField(max_length=500)
    category_title = models.CharField(max_length=500)

    def __str__(self):
        return self.category_title
