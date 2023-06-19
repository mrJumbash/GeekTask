import csv
from django.core.management.base import BaseCommand
from service.models import Book, Genre, Writer
import re


class Command(BaseCommand):
    help = "Unload books data from CSV file"

    def add_arguments(self, parser):
        parser.add_argument("csv_file", help="Path to the CSV file")

    def handle(self, *args, **options):
        pass