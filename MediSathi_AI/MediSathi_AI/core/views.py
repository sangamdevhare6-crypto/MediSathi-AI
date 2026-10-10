import json
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.utils import timezone
from .forms import SignupForm, AppointmentForm, ReminderForm, MedicalRecordForm
from .models import Profile, Appointment, MedicineReminder, MedicalRecord

def ensure_profile(user):
    profile, _ = Profile.objects.get_or_create(user=user)
    return profile

def signup(request):
    if request.user.is_authenticated: return redirect("dashboard")
    form = SignupForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = User.objects.create_user(username=form.cleaned_data["username"], email=form.cleaned_data["email"], password=form.cleaned_data["password"])
        Profile.objects.create(user=user, role="patient")
        login(request, user)
        messages.success(request, "Welcome to MediSathi AI.")
        return redirect("dashboard")
    return render(request, "core/signup.html", {"form": form})

@login_required
def dashboard(request):
    profile = ensure_profile(request.user)
    appointments = Appointment.objects.filter(patient=request.user).order_by("appointment_at")[:4]
    reminders = MedicineReminder.objects.filter(patient=request.user, active=True).order_by("reminder_time")[:4]
    records_count = MedicalRecord.objects.filter(patient=request.user).count()
    context = {
        "profile": profile, "appointments": appointments, "reminders": reminders,
        "records_count": records_count,
        "appointment_count": Appointment.objects.filter(patient=request.user).count(),
        "reminder_count": MedicineReminder.objects.filter(patient=request.user, active=True).count(),
    }
    return render(request, "core/dashboard.html", context)

@login_required
def appointments(request):
    form = AppointmentForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        item = form.save(commit=False); item.patient = request.user
        if item.appointment_at < timezone.now():
            form.add_error("appointment_at", "Choose a future date and time.")
        else:
            item.save(); messages.success(request, "Appointment request saved."); return redirect("appointments")
    items = Appointment.objects.filter(patient=request.user)
    return render(request, "core/appointments.html", {"form": form, "items": items})

@login_required
def reminders(request):
    form = ReminderForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        item = form.save(commit=False); item.patient = request.user; item.save()
        messages.success(request, "Reminder added."); return redirect("reminders")
    items = MedicineReminder.objects.filter(patient=request.user)
    return render(request, "core/reminders.html", {"form": form, "items": items})

@login_required
def records(request):
    form = MedicalRecordForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        item = form.save(commit=False); item.patient = request.user; item.save()
        messages.success(request, "Record saved securely."); return redirect("records")
    items = MedicalRecord.objects.filter(patient=request.user)
    return render(request, "core/records.html", {"form": form, "items": items})

@login_required
def assistant(request):
    answer = None
    if request.method == "POST":
        question = request.POST.get("question", "").strip()[:1200]
        if question:
            answer = ("I can share general health information, but I cannot diagnose or prescribe. "
                      "For severe symptoms such as difficulty breathing, chest pain, fainting, or signs of stroke, "
                      "seek emergency medical care now. For personal advice, contact a qualified healthcare professional. "
                      "Your question was received: " + question)
    return render(request, "core/assistant.html", {"answer": answer})

@login_required
def overview_api(request):
    if request.method != "GET": return JsonResponse({"error":"GET only"}, status=405)
    return JsonResponse({
        "appointments": Appointment.objects.filter(patient=request.user).count(),
        "reminders": MedicineReminder.objects.filter(patient=request.user, active=True).count(),
        "records": MedicalRecord.objects.filter(patient=request.user).count(),
    })
