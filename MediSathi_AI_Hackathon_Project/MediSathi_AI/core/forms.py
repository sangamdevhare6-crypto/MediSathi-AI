from django import forms
from django.contrib.auth.models import User
from .models import Appointment, MedicineReminder, MedicalRecord, Profile

class SignupForm(forms.Form):
    username = forms.CharField(max_length=150)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput, min_length=8)
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="Confirm password")
    def clean_username(self):
        username = self.cleaned_data["username"]
        if User.objects.filter(username=username).exists(): raise forms.ValidationError("Username already exists.")
        return username
    def clean(self):
        data = super().clean()
        if data.get("password") != data.get("confirm_password"): self.add_error("confirm_password", "Passwords do not match.")
        return data

class AppointmentForm(forms.ModelForm):
    appointment_at = forms.DateTimeField(input_formats=["%Y-%m-%dT%H:%M"], widget=forms.DateTimeInput(attrs={"type":"datetime-local"}))
    class Meta:
        model = Appointment
        fields = ["doctor_name", "specialty", "appointment_at", "reason"]

class ReminderForm(forms.ModelForm):
    reminder_time = forms.TimeField(widget=forms.TimeInput(attrs={"type":"time"}))
    class Meta:
        model = MedicineReminder
        fields = ["medicine_name", "instructions", "reminder_time"]

class MedicalRecordForm(forms.ModelForm):
    class Meta:
        model = MedicalRecord
        fields = ["title", "record_date", "notes", "attachment"]
        widgets = {"record_date": forms.DateInput(attrs={"type":"date"})}
