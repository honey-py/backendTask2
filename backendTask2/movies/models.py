from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField()
    release_year = models.IntegerField(blank=True, null=True)
    runtime = models.CharField(max_length=10, blank=True, null=True)
    rating = models.CharField(max_length=50, blank=True, null=True)
    showtime1 = models.TimeField(blank=True, null=True)
    showtime2 = models.TimeField(blank=True, null=True)
    showtime3 = models.TimeField(blank=True, null=True)

    def __str__(self):
        return self.title
