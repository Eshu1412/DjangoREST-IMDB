from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
class StreamPlatForm(models.Model):
    name=models.CharField(max_length=30)
    description=models.CharField(max_length=200)
    website=models.URLField(max_length=100)
    def __str__(self):
        return self.name
class WatchList(models.Model):
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=200)
    platform=models.ForeignKey(StreamPlatForm,on_delete=models.CASCADE,related_name='watchlist')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
class Review(models.Model):
    rating=models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    description=models.CharField(null=True)
    watchlist=models.ForeignKey(WatchList,on_delete=models.CASCADE,related_name='review')
    active=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.rating)+" | "+ self.watchlist.title