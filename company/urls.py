from django.urls import path, include
from company.views import (
    company_list, 
    company_detail, 
    company_create, 
    company_update, 
    company_delete, 
    subscribe_company,
)
# project_task_detail, project_task_create, project_task_update, project_task_delete, project_delete

urlpatterns = [
    path('', company_list, name="company-list"),
    path('<int:pk>/', company_detail, name="company-detail"),
    path('create/', company_create, name="company-create"),
    path('<int:pk>/update/', company_update, name="company-update"),
    path('<int:pk>/delete/', company_delete, name="company-delete"),

    path('<int:pk>/subscribe/', subscribe_company, name='company-subscribe'),




    # path('<int:project_pk>/tasks/<int:task_pk>/', project_task_detail, name="project-task-detail"),
    # path('<int:project_pk>/tasks/create/', project_task_create, name="project-task-create"),
    # path('<int:project_pk>/tasks/<int:task_pk>/update', project_task_update, name="project-task-update"),

    # path('<int:project_pk>/tasks/<int:task_pk>/delete', project_task_delete, name="project-task-delete"),

]