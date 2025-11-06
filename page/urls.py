from django.urls import path
from page.views import dashboard


urlpatterns = [
    path('', dashboard, name='dashboard')
]
