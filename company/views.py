from django.shortcuts import render, get_object_or_404, redirect
from company.models import Company
from company.forms import CompanyForm
from account.models import UserProfile
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required


@login_required
def company_list(request):
    companies = Company.objects.all().order_by('-created_at')
    data = {
        'page_title': 'Company',
        'companies': companies,
        'menu_active': 'company',
    }
    return render(request, 'company/company_list.html', data)


@login_required
def company_detail(request, pk):
    company = get_object_or_404(Company, pk=pk)
    user = request.user
    is_subscribed = user.profiles.filter(company=company).exists()    
    data = {
        'page_title': 'Company',
        'company': company,
        'menu_active': 'company',
        'is_subscribed': is_subscribed,
    }
    return render(request, 'company/company_detail.html', data)


@login_required
def company_create(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Company Created')
            return redirect('company-list')
    else:
        form = CompanyForm()
    data = {
        'page_title': 'Company',
        'form': form,
        'form_action': 'Create',
        'menu_active': 'company',
    }
    return render(request, 'company/company_form.html', data)


@login_required
def company_update(request, pk):
    company = get_object_or_404(Company, pk=pk)
    if request.method == 'POST':
        form = CompanyForm(request.POST, instance=company)
        if form.is_valid():
            form.save()
            messages.success(request, 'Company Updated')
            return redirect('company-detail', pk=pk)
    else:
        form = CompanyForm(instance=company)
    data = {
        'page_title': 'Company',
        'form': form,
        'form_action': 'Update',
        'menu_active': 'company',
    }    
    return render(request, 'company/company_form.html', data)


@require_POST
def company_delete(request, pk):
    company = get_object_or_404(Company, pk=pk)
    company.delete()
    messages.success(request, f'Company "{company.name}" deleted successfully.')
    return redirect('company-list')


@login_required
def subscribe_company(request, pk):
    company = get_object_or_404(Company, pk=pk)
    profile, created = UserProfile.objects.get_or_create(
        user=request.user,
        company=company,
        defaults={'display_name': request.user.username}
    )
    if created:
        messages.success(request, f'You are now subscribed to {company.name}.')
    else:
        messages.info(request, f'You are already subscribed to {company.name}.')
    return redirect('company-detail', pk=pk)    