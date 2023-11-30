from django.db import models

class Prepod(models.Model):
    full_name = models.CharField(max_length=250, unique=True)
    photo3x4 = models.ImageField(blank=True, null=True)
    short_info = models.TextField()

    def __str__(self):
        return self.full_name

class JobHistory(models.Model):
    prepod = models.ForeignKey('Prepod', on_delete=models.CASCADE, null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    job_characteristic = models.TextField()

    def __str__(self):
        return f"{self.prepod.full_name} - {self.start_date.year} to {self.end_date.year}"