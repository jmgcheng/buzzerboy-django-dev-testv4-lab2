from django.urls import path, include
from account.views import switch_profile


urlpatterns = [
    path('profiles/<int:pk>/switch/', switch_profile, name='switch-profile'),
]