from django.contrib import admin
from .models import Patient, Appointment


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "phone", "email")


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("id", "patient", "appointment_date",
                    "appointment_time", "reason")
