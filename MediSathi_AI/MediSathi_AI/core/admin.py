from django.contrib import admin
from .models import Profile, Appointment, MedicineReminder, MedicalRecord

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "role", "phone", "preferred_language")
    list_filter = ("role",)
    search_fields = ("user__username", "user__email", "phone")

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("patient", "doctor_name", "specialty", "appointment_at", "status")
    list_filter = ("status", "specialty")
    search_fields = ("patient__username", "doctor_name")

@admin.register(MedicineReminder)
class MedicineReminderAdmin(admin.ModelAdmin):
    list_display = ("patient", "medicine_name", "reminder_time", "active")
    list_filter = ("active",)

@admin.register(MedicalRecord)
class MedicalRecordAdmin(admin.ModelAdmin):
    list_display = ("patient", "title", "record_date")
    search_fields = ("patient__username", "title")
