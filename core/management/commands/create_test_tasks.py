from django.core.management.base import BaseCommand
from core.models import Task
from faker import Faker
import random

class Command(BaseCommand):
    help = 'Creates test tasks'

    def handle(self, *args, **kwargs):
        fake = Faker()
        
        for i in range(50):  # Create 50 test tasks
            Task.objects.create(
                title=fake.sentence(),
                description=fake.paragraph(),
                completed=random.choice([True, False])
            )
            
        self.stdout.write(self.style.SUCCESS('Successfully created test tasks'))