from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.db import transaction
from djongo import models as djongo_models
from octofit_tracker import models as app_models

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Delete all data
        User.objects.all().delete()
        app_models.Team.objects.all().delete()
        app_models.Activity.objects.all().delete()
        app_models.Leaderboard.objects.all().delete()
        app_models.Workout.objects.all().delete()

        # Create Teams
        marvel = app_models.Team.objects.create(name='Marvel')
        dc = app_models.Team.objects.create(name='DC')

        # Create Users
        tony = User.objects.create_user(username='tony', email='tony@stark.com', password='ironman', first_name='Tony', last_name='Stark', team=marvel)
        steve = User.objects.create_user(username='steve', email='steve@rogers.com', password='captain', first_name='Steve', last_name='Rogers', team=marvel)
        bruce = User.objects.create_user(username='bruce', email='bruce@wayne.com', password='batman', first_name='Bruce', last_name='Wayne', team=dc)
        clark = User.objects.create_user(username='clark', email='clark@kent.com', password='superman', first_name='Clark', last_name='Kent', team=dc)

        # Create Activities
        app_models.Activity.objects.create(user=tony, type='Run', duration=30, distance=5)
        app_models.Activity.objects.create(user=steve, type='Swim', duration=45, distance=2)
        app_models.Activity.objects.create(user=bruce, type='Cycle', duration=60, distance=20)
        app_models.Activity.objects.create(user=clark, type='Run', duration=50, distance=10)

        # Create Workouts
        app_models.Workout.objects.create(name='Morning Cardio', description='Cardio for all heroes', suggested_for='All')
        app_models.Workout.objects.create(name='Strength Training', description='Strength for DC', suggested_for='DC')
        app_models.Workout.objects.create(name='Agility Drills', description='Agility for Marvel', suggested_for='Marvel')

        # Create Leaderboard
        app_models.Leaderboard.objects.create(user=tony, points=100)
        app_models.Leaderboard.objects.create(user=steve, points=90)
        app_models.Leaderboard.objects.create(user=bruce, points=95)
        app_models.Leaderboard.objects.create(user=clark, points=110)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
