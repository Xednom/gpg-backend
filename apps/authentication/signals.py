from django.dispatch import receiver
from django.db.models.signals import post_save


@receiver(post_save, sender=User)
    def create_staff_user(sender, instance, created, **kwargs):
        if created:
            if instance.designation_category == "staff":
                Staff.objects.create(user=instance)


@receiver(post_save, sender=User)
    def create_client_user(sender, instance, created, **kwargs):
        if created:
            if (
                instance.designation_category == "new_client"
                or instance.designation_category == "current_client"
                or instance.designation_category == "affiliate_partner"
            ):
                Client.objects.create(user=instance)