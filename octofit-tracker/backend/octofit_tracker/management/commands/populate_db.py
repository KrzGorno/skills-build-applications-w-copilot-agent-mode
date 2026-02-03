from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Usuń stare dane
        Activity.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()

        # Tworzenie drużyn
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Tworzenie użytkowników
        users = [
            User(name='Spider-Man', email='spiderman@marvel.com', team=marvel),
            User(name='Iron Man', email='ironman@marvel.com', team=marvel),
            User(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
            User(name='Batman', email='batman@dc.com', team=dc),
        ]
        for u in users:
            u.save()

        # Tworzenie aktywności
        Activity.objects.create(user=users[0], type='Run', duration=30, date=timezone.now().date())
        Activity.objects.create(user=users[1], type='Swim', duration=45, date=timezone.now().date())
        Activity.objects.create(user=users[2], type='Bike', duration=60, date=timezone.now().date())
        Activity.objects.create(user=users[3], type='Yoga', duration=20, date=timezone.now().date())

        # Tworzenie workoutów
        w1 = Workout.objects.create(name='Hero HIIT', description='High intensity for heroes')
        w2 = Workout.objects.create(name='Power Yoga', description='Yoga for super strength')
        w1.suggested_for.add(marvel)
        w2.suggested_for.add(dc)

        # Tworzenie leaderboard
        Leaderboard.objects.create(team=marvel, points=100)
        Leaderboard.objects.create(team=dc, points=120)

        self.stdout.write(self.style.SUCCESS('Baza octofit_db została wypełniona przykładowymi danymi!'))
