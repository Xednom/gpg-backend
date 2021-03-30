from apps.core.notifications import BaseModelEmailNotification
from apps.gpg.models import PropertyDetail


class BasePropertyDetailNotification:
    model = PropertyDetail

    def get_context_data(self):
        context = super().get_context_data()
        context.update(
            {
                "property_detail": self.obj
            }
        )
        return context
    
    @classmethod
    def get_demo_args(kls):
        return [kls.models.objects.order_by("?")[0]]


class EmailPropertyDetailNotification(BasePropertyDetailNotification, BaseModelEmailNotification):

    def get_recipients(self):
        return [self.obj.client_email. self.obj.staff_email]


class PropertyDetailInProcess:
    name = "PropertyDetailInProcess"
    template_name = "property_detail_in_process"