from django.core.management.base import BaseCommand

from apps.gpg.models import JobOrderCategory, JobOrderGeneral
from apps.archive.models import ArchiveJobOrderApn, ArchiveJobOrder
from apps.authentication.models import Staff


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        user_list = []
        job_order_generals = JobOrderGeneral.objects.filter(status="Closed")
        job_order_categories = JobOrderCategory.objects.filter(status="Closed")

        if job_order_generals:

            for job_order in job_order_generals:

                archive_job_order_general_exists = ArchiveJobOrder.objects.filter(
                    status="Closed", ticket_number=job_order.ticket_number
                ).exists()

                jo_general_staffs = JobOrderGeneral.objects.filter(
                    status="Closed", ticket_number=job_order.ticket_number
                )
                for staff in jo_general_staffs:
                    for staff in staff.va_assigned.all():

                        if not archive_job_order_general_exists:
                            (
                                archive_job_order,
                                created,
                            ) = ArchiveJobOrder.objects.get_or_create(
                                client=job_order.client,
                                client_file=job_order.client_file,
                                client_email=job_order.client_email,
                                staff_email=job_order.staff_email,
                                ticket_number=job_order.ticket_number,
                                request_date=job_order.request_date,
                                due_date=job_order.due_date,
                                job_title=job_order.job_title,
                                job_description=job_order.job_description,
                                client_notes=job_order.client_notes,
                                va_notes=job_order.va_notes,
                                management_notes=job_order.management_notes,
                                status=job_order.status,
                                date_completed=job_order.date_completed,
                                total_time_consumed=job_order.total_time_consumed,
                                url_of_the_completed_jo=job_order.url_of_the_completed_jo,
                            )
                            archive_job_order.va_assigned.add(staff.id)
            print("Job order general that were closed are now in Archive")

        if job_order_categories:

            for job_order in job_order_categories:
                archive_job_order_category_exists = ArchiveJobOrderApn.objects.filter(
                    status="Closed", ticket_number=job_order.ticket_number
                ).exists()
                jo_category_staffs = JobOrderCategory.objects.filter(
                    status="Closed", ticket_number=job_order.ticket_number
                )
                # print(jo_staffs)
                for staff in jo_category_staffs:
                    for j_staff in staff.staff.all():

                        if not archive_job_order_category_exists:
                            (
                                archive_job_order_cat,
                                created,
                            ) = ArchiveJobOrderApn.objects.get_or_create(
                                ticket_number=job_order.ticket_number,
                                property_detail=job_order.property_detail,
                                client=job_order.client,
                                client_file=job_order.client_file,
                                client_email=job_order.client_email,
                                staff_email=job_order.staff_email,
                                category=job_order.category,
                                deadline=job_order.deadline,
                                status=job_order.status,
                                due_date=job_order.due_date,
                                date_completed=job_order.date_completed,
                                job_description=job_order.job_description,
                                url_of_the_completed_jo=job_order.url_of_the_completed_jo,
                                notes_va=job_order.notes_va,
                                notes_management=job_order.notes_management,
                                total_time_consumed=job_order.total_time_consumed,
                            )
                            archive_job_order_cat.staff.add(j_staff.id)
            print("Job order category that were closed are now in Archive")
