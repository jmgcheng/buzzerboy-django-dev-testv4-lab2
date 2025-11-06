from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# from django.utils.translation import gettext as _
# from django.utils import translation
# from django.conf import settings


@login_required
def index(request):
    data = {
        'page_title': 'Homepage',
        'menu_active': 'homepage',
    }
    return render(request, 'page/homepage.html', data)


@login_required
def dashboard(request):
    data = {
        'page_title': 'Dashboard',
        'menu_active': 'dashboard',
    }
    return render(request, 'page/dashboard.html', data)
