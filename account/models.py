from django.db import models
from django.conf import settings
from company.models import Company
from django.contrib.auth.models import AbstractUser


class UserProfile(models.Model):
    LANGUAGE_CHOICES = [
        ('EN', 'English'),
        ('FR', 'French'),
        ('ES', 'Spanish'),
        ('IT', 'Italian'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profiles')
    company = models.ForeignKey('company.Company', on_delete=models.CASCADE, related_name='profiles', null=True, blank=True)
    display_name = models.CharField(max_length=200, blank=True)
    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES, default='EN')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        if self.company:
            return f"{self.display_name or self.user.username} @ {self.company.name} : {self.language}"
        return f"{self.display_name or self.user.username} (personal) : {self.language}"


class User(AbstractUser):
    email = models.EmailField(unique=True)

    last_active_profile = models.ForeignKey(
        UserProfile,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Last active profile"
    )

    def __str__(self):
        return self.username
