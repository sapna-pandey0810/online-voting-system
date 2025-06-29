from django.contrib.auth.models import User
from django.db import models

class Candidate(models.Model):
    name = models.CharField(max_length=100)
    total_votes = models.IntegerField(default=0)
    image_path = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.name

class Vote(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Ensures one vote per user
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'candidate'], name='unique_user_candidate_vote')
        ]