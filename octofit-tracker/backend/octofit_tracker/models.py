from djongo import models
from django.contrib.auth.models import AbstractUser

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name

class User(AbstractUser):
    email = models.EmailField(unique=True)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='octofit_users',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='octofit_users_permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

class Activity(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    duration = models.PositiveIntegerField()  # in minutes
    distance = models.FloatField()  # in km
    def __str__(self):
        return f"{self.user.username} - {self.type}"

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    suggested_for = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Leaderboard(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    points = models.IntegerField()
    def __str__(self):
        return f"{self.user.username}: {self.points}"
