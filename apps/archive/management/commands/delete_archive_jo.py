from lib2to3.pytree import Base
from django.core.management.base import BaseCommand

from apps.gpg.models import JobOrderCategory, JobOrderGeneral
from apps.archive.models import ArchiveJobOrderApn, ArchiveJobOrder
from apps.authentication.models import Staff


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        ArchiveJobOrder.objects.all().delete()
        ArchiveJobOrderApn.objects.all().delete()
