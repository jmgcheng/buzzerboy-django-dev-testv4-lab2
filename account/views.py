from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from account.forms import RegisterForm, ProfileForm, UserProfileForm, EmailAuthenticationForm
from account.models import UserProfile
from django.utils import translation
from django.utils.translation import gettext as _
from django.contrib.auth.views import LogoutView, LoginView
from django.conf import settings
# from django.utils.translation import LANGUAGE_SESSION_KEY


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully! You can now log in.")
            return redirect("login")
    else:
        form = RegisterForm()
    return render(request, "account/register.html", {"form": form})


@login_required
def profile(request):
    active_profile_id = request.session.get('active_profile_id')
    profile = None
    if active_profile_id:
        profile = get_object_or_404(UserProfile, id=active_profile_id, user=request.user)
    else:
        profile = request.user.profiles.first()  # fallback

    data = {
        'page_title': 'Profile',
        "active_profile": profile,
        'menu_active': 'profile',
    }            
    return render(request, "account/profile.html", data)


@login_required
def profile_update(request):
    active_profile_id = request.session.get('active_profile_id')
    profile = None
    if active_profile_id:
        profile = get_object_or_404(UserProfile, id=active_profile_id, user=request.user)
    else:
        profile = request.user.profiles.first()

    if request.method == "POST":
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()

            # Optional: update extra fields from UserProfile
            profile.language = request.POST.get('language', profile.language)
            profile.save()

            messages.success(request, "Your profile has been updated!")
            return redirect("profile")
    else:
        form = ProfileForm(instance=request.user)
    
    data = {
        'page_title': 'Profile',
        "active_profile": profile,
        'menu_active': 'profile',
        'form': form,
        'form_action': 'Update',
    }    

    return render(request, "account/profile_form.html", data)


@login_required
def switch_profile(request, pk):
    profile = get_object_or_404(UserProfile, pk=pk, user=request.user)
    request.session['active_profile_id'] = profile.id

    # 
    user_lang = (profile.language or 'EN').lower()
    request.session['django_language'] = user_lang
    
    # Save last active for persistence across logouts
    request.user.last_active_profile = profile
    request.user.save()    

    messages.success(request, f'Active profile switched to {profile}')
    # return redirect(request.GET.get('next') or 'homepage')

    # also set the cookie for language to persist
    response = redirect(request.GET.get('next') or 'homepage')
    response.set_cookie(
        settings.LANGUAGE_COOKIE_NAME,
        user_lang,
        path=settings.LANGUAGE_COOKIE_PATH,
        domain=settings.LANGUAGE_COOKIE_DOMAIN,
        secure=settings.LANGUAGE_COOKIE_SECURE,
        httponly=settings.LANGUAGE_COOKIE_HTTPONLY,
        samesite=settings.LANGUAGE_COOKIE_SAMESITE,
    )    
    return response    


@login_required
def userprofile_update(request):
    active_profile_id = request.session.get('active_profile_id')
    profile = get_object_or_404(UserProfile, id=active_profile_id, user=request.user)

    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()

            user_lang = (profile.language or 'EN').lower()
            request.session['django_language'] = user_lang
            request.user.last_active_profile = profile
            request.user.save(update_fields=['last_active_profile'])
            response = redirect("profile")
            response.set_cookie(
                settings.LANGUAGE_COOKIE_NAME,
                user_lang,
                path=settings.LANGUAGE_COOKIE_PATH,
                domain=settings.LANGUAGE_COOKIE_DOMAIN,
                secure=settings.LANGUAGE_COOKIE_SECURE,
                httponly=settings.LANGUAGE_COOKIE_HTTPONLY,
                samesite=settings.LANGUAGE_COOKIE_SAMESITE,
            )

            try:
                messages.success(request, f"Your {profile.company.name} profile was updated.")
            except AttributeError:
                messages.success(request, f"Your UserProfile was updated.")

            # return redirect("profile")
            return response
    else:
        form = UserProfileForm(instance=profile)

    return render(request, "account/userprofile_form.html", {
        'page_title': 'Profile',
        'form': form,
        'profile': profile,
        'form_action': 'Update',
    })




class CustomLoginView(LoginView):
    authentication_form = EmailAuthenticationForm
    template_name = "account/login.html"
    
    def form_valid(self, form):
        response = super().form_valid(form)  # Calls login, which triggers signals to set session
        
        # Set cookie to match session (for immediate persistence)
        lang = self.request.session.get('django_language')
        if lang:
            response.set_cookie(
                settings.LANGUAGE_COOKIE_NAME,
                lang,
                path=settings.LANGUAGE_COOKIE_PATH,
                domain=settings.LANGUAGE_COOKIE_DOMAIN,
                secure=settings.LANGUAGE_COOKIE_SECURE,
                httponly=settings.LANGUAGE_COOKIE_HTTPONLY,
                samesite=settings.LANGUAGE_COOKIE_SAMESITE,
            )
        return response


class CustomLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        response.delete_cookie(settings.LANGUAGE_COOKIE_NAME)
        return response