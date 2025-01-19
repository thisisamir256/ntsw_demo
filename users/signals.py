from django.db.models.signals import post_save
from django.dispatch import receiver
from decouple import config
from .models import CustomUser, Role, UserRole


@receiver(post_save, sender=CustomUser)
def assign_default_role(sender, instance, created, **kwargs):
    if created:
        base_role_name = config('BASE_ROLE_NAME')
        default_role, _ = Role.objects.get_or_create(
            name=base_role_name)
        if default_role:
            UserRole.objects.create(user=instance, role=default_role)
        else:
            print('role dont create for your user')
        # todo:log error in the else block
