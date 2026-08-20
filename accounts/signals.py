from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import (
    User,
    PatientProfile,
    DoctorProfile,
    LabStaffProfile,
    PharmacyStaffProfile,
)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):

    if not created:
        return

    if instance.role == User.Role.PATIENT:
        PatientProfile.objects.create(user=instance)

    elif instance.role == User.Role.DOCTOR:
        DoctorProfile.objects.create(
            user=instance,
            specialization='Not specified',
            qualification='Not specified',
            license_number=f'TEMP-{instance.id}',
        )

    elif instance.role == User.Role.LAB:
        LabStaffProfile.objects.create(
            user=instance,
            employee_id=f'TEMP-LAB-{instance.id}',
        )

    elif instance.role == User.Role.PHARMACY:
        PharmacyStaffProfile.objects.create(
            user=instance,
            employee_id=f'TEMP-PHARMACY-{instance.id}',
        )