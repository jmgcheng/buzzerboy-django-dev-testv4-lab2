"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import (
    LoginView, 
    LogoutView, 
    PasswordResetView, 
    PasswordResetConfirmView, 
    PasswordResetCompleteView, 
    PasswordResetDoneView,
    PasswordChangeView, 
    PasswordChangeDoneView
)
from account.views import register, profile, profile_update, userprofile_update, CustomLogoutView, CustomLoginView


urlpatterns = [
    path('admin/', admin.site.urls),

    path("profile/", profile, name="profile"),
    path("profile/update/", profile_update, name="profile-update"),
    path("register/", register, name="register"),
    # path("login/", LoginView.as_view(template_name="account/login.html"), name="login"),
    path("login/", CustomLoginView.as_view(template_name="account/login.html"), name="login"),
    # path("logout/", LogoutView.as_view(), name="logout"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
    path("password-reset/", PasswordResetView.as_view(template_name="account/password_reset.html"), name="password-reset"),
    path("password-reset/done/", PasswordResetDoneView.as_view(template_name="account/password_reset_done.html"), name="password_reset_done"),
    path("password-reset-confirm/<uidb64>/<token>/", PasswordResetConfirmView.as_view(template_name="account/password_reset_confirm.html"), name="password_reset_confirm"),
    path("password-reset-complete/", PasswordResetCompleteView.as_view(template_name="account/password_reset_complete.html"), name="password_reset_complete"),

    path("password-change/", PasswordChangeView.as_view(template_name="account/password_change.html"), name="password_change"),
    path("password-change/done/", PasswordChangeDoneView.as_view(template_name="account/password_change_done.html"), name="password_change_done"),

    path("companies/", include("company.urls")),
    path("accounts/", include("account.urls")),
    path('', include('page.urls')),

    path("profile/company/update/", userprofile_update, name="userprofile-update"),

]
