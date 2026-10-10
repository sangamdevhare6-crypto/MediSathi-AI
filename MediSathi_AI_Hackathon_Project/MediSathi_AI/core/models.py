from django.conf import settings
from django.db import models

class Profile(models.Model):
    ROLE_CHOICES = [("patient", "Patient"), ("doctor", "Doctor"), ("admin", "Admin")]
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile")
    role = models.CharField(max_length=12, choices=ROLE_CHOICES, default="patient")
    phone = models.CharField(max_length=30, blank=True)
    preferred_language = models.CharField(max_length=10, default="en")
    def __str__(self): return f"{self.user.username} ({self.role})"

class Appointment(models.Model):
    STATUS_CHOICES = [("pending", "Pending"), ("confirmed", "Confirmed"), ("completed", "Completed"), ("cancelled", "Cancelled")]
    patient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="patient_appointments")
    doctor_name = models.CharField(max_length=120)
    specialty = models.CharField(max_length=100, default="General Physician")
    appointment_at = models.DateTimeField()
    reason = models.CharField(max_length=240, blank=True)
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta: ordering = ["appointment_at"]
    def __str__(self): return f"{self.patient.username} - {self.doctor_name}"

class MedicineReminder(models.Model):
    patient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="medicine_reminders")
    medicine_name = models.CharField(max_length=120)
    instructions = models.CharField(max_length=180, blank=True)
    reminder_time = models.TimeField()
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self): return f"{self.medicine_name} for {self.patient.username}"

class MedicalRecord(models.Model):
    patient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="medical_records")
    title = models.CharField(max_length=150)
    record_date = models.DateField()
    notes = models.TextField(blank=True)
    attachment = models.FileField(upload_to="records/", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self): return f"{self.title} — {self.patient.username}"
