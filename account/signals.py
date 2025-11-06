from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import UserProfile
from django.contrib.auth.signals import user_logged_in
from django.utils import translation
# from django.utils.translation import LANGUAGE_SESSION_KEY
from django.conf import settings


User = get_user_model()


@receiver(post_save, sender=User)
def create_default_profile(sender, instance, created, **kwargs):
    if created:
        profile = UserProfile.objects.create(user=instance, display_name=instance.username)
        instance.last_active_profile = profile
        instance.save()


@receiver(user_logged_in)
def set_default_active_profile(sender, user, request, **kwargs):
    if user.last_active_profile and user.last_active_profile.user == user:
        request.session['active_profile_id'] = user.last_active_profile.id
    else:
        default_profile = user.profiles.first()
        if default_profile:
            request.session['active_profile_id'] = default_profile.id
            user.last_active_profile = default_profile
            user.save()


@receiver(user_logged_in)
def set_language_on_login(sender, user, request, **kwargs):
    active_profile_id = request.session.get('active_profile_id')
    if active_profile_id:
        profile = UserProfile.objects.filter(id=active_profile_id, user=user).first()
        if profile and profile.language:
            user_lang = profile.language.lower()
            request.session['django_language'] = user_lang

