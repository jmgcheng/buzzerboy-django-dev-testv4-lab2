from django.urls import path
from page.views import dashboard, index, pricing


urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('pricing/', pricing, name='pricing'),
    path('', index, name='index'),
]
