import os
from random import choice
from django.core.management.base import BaseCommand
from django_seed import Seed
from django.conf import settings
from users.models import User
from categories.models import Category


class Command(BaseCommand):

    help = "This command super user"

    def handle(self, *args, **options):
        try:
            User.objects.get(username="ebadmin")
            self.stdout.write(self.style.SUCCESS(f'superuser already exist!'))

        except User.DoesNotExist:
            User.objects.create_superuser(
                "ebadmin", "smkang0321@gmail.com", os.environ.get("DJANGO_ADMIN_PASS"))
            self.stdout.write(self.style.SUCCESS(f'superusers created!'))
