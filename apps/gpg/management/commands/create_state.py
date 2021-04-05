import xlrd
import argparse
import os

from apps.gpg.models import State

from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string


class Command(BaseCommand):
    help = "Create set of State from an excel file."

    def dir_path(self, string):
        if os.path.isdir(string):
            return string
        else:
            raise NotADirectoryError(string)

    def add_arguments(self, parser):
        parser.add_argument('-f', '--file_path', type=str,
                            help="Gets the location of the xls file.")

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']

        if file_path:
            loc = ('{file_path}'.format(file_path=file_path))
            wb = xlrd.open_workbook(loc)
            sheet = wb.sheet_by_index(0)
            sheet.cell_value(0, 0)

            for i in range(sheet.nrows):
                if sheet.cell_value(i, 0):
                    state = (sheet.cell_value(i, 0))
                    state = State.objects.create(name=state)
                    self.stdout.write(self.style.SUCCESS(f"State of {state.name} created with success"))
        else:
            self.stdout.write(self.style.WARNING("Please add '--file <file location>' to point what excel file to use for this command."))