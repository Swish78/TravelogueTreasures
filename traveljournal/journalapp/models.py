from django.db import models
from django.contrib.auth.models import User

class TravelJournal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class JournalEntry(models.Model):
    journal = models.ForeignKey(TravelJournal, on_delete=models.CASCADE)
    content_type = models.CharField(max_length=10)  # 'photo', 'video', 'text'
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    journal = models.ForeignKey(TravelJournal, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Recommendation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    journal = models.ForeignKey(TravelJournal, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
