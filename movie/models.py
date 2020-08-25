from django.db import models

class Movie(models.Model):
    movieName = models.CharField(max_length=100)
    movieDescription = models.TextField(max_length=200, blank=True)  # Optional
    moviePoster = models.ImageField(upload_to='images', default='images/none.jpg')
    createdDate = models.DateTimeField(auto_now_add=True)
    releasedDate = models.DateField()

    def __str__(self):
        return self.movieName




