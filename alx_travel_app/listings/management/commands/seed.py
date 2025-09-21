from django.core.management.base import BaseCommand
from listings.models import Listing
from django.contrib.auth.models import User
import random


class Command(BaseCommand):
    help = "Seed the database with sample listings"

    def handle(self, *args, **kwargs):
        if not User.objects.filter(username="demo").exists():
            User.objects.create_user("demo", password="password123")

        listings_data = [
            {"title": "Beachfront Villa", "description": "Beautiful villa by the sea", "price_per_night": 250.00, "location": "Miami"},
            {"title": "Mountain Cabin", "description": "Cozy cabin in the mountains", "price_per_night": 120.00, "location": "Denver"},
            {"title": "City Apartment", "description": "Modern apartment in downtown", "price_per_night": 180.00, "location": "New York"},
        ]

        for data in listings_data:
            Listing.objects.get_or_create(**data)

        self.stdout.write(self.style.SUCCESS("Database seeded with sample listings!"))
