from django.core.management.base import BaseCommand
from shop.models import RasaProduct
import random

class Command(BaseCommand):
    help = "Populate RasaProducts with dummy data"

    def handle(self, *args, **kwargs):
        colors = ['oq', 'qora', 'ko‘k', 'qizil', 'yashil']
        materials = ['paxta', 'polyester', 'jun']
        sizes = ['S', 'M', 'L', 'XL']
        categories = range(1, 10)  # 10 ta kategoriya
        for _ in range(500):
            RasaProduct.objects.create(
                atr_id=random.randint(1, 50),
                ctg_id=random.choice(categories),
                name=f"Mahsulot {_}",
                description=f"Bu mahsulotning tavsifi {_}",
                size=random.choice(sizes),
                price=random.uniform(10.0, 100.0),
                quantity=random.randint(1, 50),
                color=random.choice(colors),
                material=random.choice(materials),
            )
        self.stdout.write("500+ mahsulotlar muvaffaqiyatli yaratildi!")
