from django.conf import settings

from herald import registry
from herald.base import EmailNotification

from .bases import EmailPropertyDetailNotification, PropertyDetailInProcess


@registry.register_decorator()
class PropertyDetailEmail(EmailNotification):
    template_name = "property_detail_update"

    def __init__(self, subject, property_detail, client_email, staff_email):
        self.context = {
            "property_detail": property_detail,
            "front_end": settings.FRONTEND_DOMAIN,
            "http": settings.HTTP_PROTOCOL,
        }
        self.subject = "Property detail updated: Ticket number - " + subject
        self.to_emails = [client_email, staff_email]


@registry.register_decorator()
class JobOrderGeneralEmail(EmailNotification):
    template_name = "job_order_general_update"

    def __init__(self, subject, job_order, client_email, staff_email):
        self.context = {
            "job_order": job_order,
            "front_end": settings.FRONTEND_DOMAIN,
            "http": settings.HTTP_PROTOCOL,
        }
        self.subject = "Job order updated: Ticket number - " + subject
        self.to_emails = [client_email, staff_email]


@registry.register_decorator()
class JobOrderCategoryEmail(EmailNotification):
    template_name = "job_order_category_update"

    def __init__(self, subject, job_order_category, client_email, staff_email):
        self.context = {
            "job_order_category": job_order_category,
            "front_end": settings.FRONTEND_DOMAIN,
            "http": settings.HTTP_PROTOCOL,
        }
        self.subject = "Job order category updated: Ticket number - " + subject
        self.to_emails = [client_email, staff_email]


@registry.register_decorator()
class JobOrderCommentEmail(EmailNotification):
    template_name = "job_order_comment_update"

    def __init__(self, subject, job_order_comment, client_email, staff_email):
        self.context = {
            "job_order": job_order_comment,
            "front_end": settings.FRONTEND_DOMAIN,
            "http": settings.HTTP_PROTOCOL,
        }
        self.subject = "Comment update for Ticket number - " + subject
        self.to_emails = [client_email, staff_email]


class JobOrderCategoryCommentEmail(EmailNotification):
    template_name = "job_order_category_comment"

    def __init__(self, subject, job_order_category, client_email, staff_email):
        self.context = {
            "job_order": job_order_category,
            "front_end": settings.FRONTEND_DOMAIN,
            "http": settings.HTTP_PROTOCOL,
        }
        self.subject = "Comment update for Ticket number - " + subject
        self.to_emails = [client_email, staff_email]
