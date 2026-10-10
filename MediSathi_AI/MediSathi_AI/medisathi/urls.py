from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from core import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.dashboard, name="dashboard"),
    path("accounts/login/", auth_views.LoginView.as_view(template_name="core/login.html"), name="login"),
    path("accounts/logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("accounts/signup/", views.signup, name="signup"),
    path("appointments/", views.appointments, name="appointments"),
    path("reminders/", views.reminders, name="reminders"),
    path("assistant/", views.assistant, name="assistant"),
    path("records/", views.records, name="records"),
    path("api/overview/", views.overview_api, name="overview_api"),
]
