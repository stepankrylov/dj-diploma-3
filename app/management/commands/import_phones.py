import csv

from django.core.management.base import BaseCommand
from django.template.defaultfilters import slugify

from app.models import Phones


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('import.csv', 'r', encoding='utf-8') as csvfile:

            phone_reader = csv.reader(csvfile, delimiter=';')
            next(phone_reader)

            for line in phone_reader:

                rec = Phones(
                            id=line[0],
                            name=line[1],
                            image=line[2],
                            price=line[3],
                            description=line[4],
                            slug=slugify(line[1])
                            )
                rec.save()
