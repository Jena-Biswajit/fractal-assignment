from django.db import models

class SentimentRecord(models.Model):
    text = models.TextField()
    polarity = models.FloatField()
    sentiment = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sentiment} ({self.polarity})"
