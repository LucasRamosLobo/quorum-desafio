import csv
import os
from django.core.management.base import BaseCommand
from quorum_app.models import Legislator, Bill, Vote, Voteresult

class Command(BaseCommand):
    help = 'Import data from CSV files to Django models'

    def handle(self, *args, **options):
        csv_files = {
            'bills': 'bills_(2).csv',
            'legislators': 'legislators_(2).csv',
            'votes': 'votes_(2).csv',
            'voteresults': 'vote_results_(2).csv',
        }

        for model_name, file_name in csv_files.items():
            file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)
            model = globals()[model_name[:-1].capitalize()] 
            self.stdout.write(self.style.SUCCESS(f'Importing data for {model_name}...'))
            self.import_data(model, file_path)

        self.stdout.write(self.style.SUCCESS('Data import completed successfully!'))

    def import_data(self, model, file_path):
        with open(file_path, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            model.objects.all().delete()

            for row in reader:
                model_instance = model(**row)
                model_instance.save()
