from account.models import UserProfile


def active_profile(request):
    user = request.user
    if not user.is_authenticated:
        return {'active_profile': None}

    profile_id = request.session.get('active_profile_id')
    profile = None
    if profile_id:
        try:
            profile = user.profiles.get(id=profile_id)
        except UserProfile.DoesNotExist:
            pass

    return {'active_profile': profile}
