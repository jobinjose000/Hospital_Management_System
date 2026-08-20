from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import (
    User,
    PatientProfile,
    DoctorProfile,
    LabStaffProfile,
    PharmacyStaffProfile,
)


@admin.register(User)
class CustomUserAdmin(UserAdmin):

    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'role',
        'phone',
        'is_verified',
        'is_staff',
        'is_active',
    )

    list_filter = (
        'role',
        'is_verified',
        'is_staff',
        'is_active',
    )

    search_fields = (
        'username',
        'first_name',
        'last_name',
        'email',
        'phone',
    )

    fieldsets = UserAdmin.fieldsets + (
        (
            'Hospital Information',
            {
                'fields': (
                    'role',
                    'phone',
                    'is_verified',
                )
            },
        ),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            'Hospital Information',
            {
                'fields': (
                    'role',
                    'phone',
                    'is_verified',
                )
            },
        ),
    )


@admin.register(PatientProfile)
class PatientProfileAdmin(admin.ModelAdmin):

    list_display = (
        'user',
        'date_of_birth',
        'gender',
        'blood_group',
        'created_at',
    )

    search_fields = (
        'user__username',
        'user__first_name',
        'user__last_name',
    )

    list_filter = (
        'gender',
        'blood_group',
    )


@admin.register(DoctorProfile)
class DoctorProfileAdmin(admin.ModelAdmin):

    list_display = (
        'user',
        'specialization',
        'qualification',
        'department',
        'consultation_fee',
        'is_available',
    )

    search_fields = (
        'user__username',
        'user__first_name',
        'user__last_name',
        'specialization',
        'license_number',
    )

    list_filter = (
        'specialization',
        'department',
        'is_available',
    )


@admin.register(LabStaffProfile)
class LabStaffProfileAdmin(admin.ModelAdmin):

    list_display = (
        'user',
        'employee_id',
        'department',
        'designation',
        'created_at',
    )

    search_fields = (
        'user__username',
        'employee_id',
        'user__first_name',
        'user__last_name',
    )


@admin.register(PharmacyStaffProfile)
class PharmacyStaffProfileAdmin(admin.ModelAdmin):

    list_display = (
        'user',
        'employee_id',
        'designation',
        'created_at',
    )

    search_fields = (
        'user__username',
        'employee_id',
        'user__first_name',
        'user__last_name',
    )