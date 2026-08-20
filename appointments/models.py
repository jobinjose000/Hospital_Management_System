from django.conf import settings
from django.db import models


class Appointment(models.Model):

    class Status(models.TextChoices):
        PENDING = 'PENDING', 'Pending'
        CONFIRMED = 'CONFIRMED', 'Confirmed'
        COMPLETED = 'COMPLETED', 'Completed'
        CANCELLED = 'CANCELLED', 'Cancelled'

    patient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='patient_appointments',
        limit_choices_to={'role': 'PATIENT'}
    )

    doctor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='doctor_appointments',
        limit_choices_to={'role': 'DOCTOR'}
    )

    appointment_date = models.DateField()

    appointment_time = models.TimeField()

    reason = models.TextField(
        blank=True
    )

    patient_notes = models.TextField(
        blank=True
    )

    doctor_notes = models.TextField(
        blank=True
    )

    consultation_fee = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ['-appointment_date', '-appointment_time']

    def __str__(self):
        return (
            f"{self.patient.get_full_name() or self.patient.username} "
            f"→ Dr. {self.doctor.get_full_name() or self.doctor.username} "
            f"({self.appointment_date})"
        )