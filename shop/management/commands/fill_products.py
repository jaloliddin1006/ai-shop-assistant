import random
from django.core.management.base import BaseCommand
from shop.models import RasaProduct

class Command(BaseCommand):
    help = "Fill the database with default RasaProduct data"

    def handle(self, *args, **kwargs):
        categories = ['Shirts', 'Pants', 'Jackets', 'Shoes', 'Accessories']
        materials = ['Cotton', 'Wool', 'Leather', 'Synthetic', 'Denim']
        colors = ['Black', 'White', 'Blue', 'Red', 'Green', 'Yellow']
        genders = ['male', 'female', 'child']
        sizes = ['S', 'M', 'L', 'XL', 'XXL']

        for _ in range(500):
            RasaProduct.objects.create(
                name=f"Product {_}",
                description=f"Description for Product {_}",
                category=random.choice(categories),
                material=random.choice(materials),
                color=random.choice(colors),
                gender=random.choice(genders),
                stock=random.randint(1, 100),
                price=round(random.uniform(10, 500), 2),
                atr_id=random.randint(1, 50),
                ctg_id=random.randint(1, 20),
                size=random.choice(sizes),
            )

        self.stdout.write(self.style.SUCCESS("Successfully filled the database with 500 RasaProduct records"))
