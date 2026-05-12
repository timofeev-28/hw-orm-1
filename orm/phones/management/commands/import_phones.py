import csv

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open("phones.csv", "r", encoding="utf-8", newline="") as file:
            phones = list(csv.DictReader(file, delimiter=";"))

        for phone in phones:
            phone = Phone(
                id=int(phone["id"]),
                name=phone["name"].strip(),
                price=float(
                    phone["price"].replace("₽", "").replace(",", ".").strip()
                ),
                image=phone["image"].strip(),
                release_date=phone["release_date"],
                lte_exists=phone["lte_exists"],
            )
            phone.save()
