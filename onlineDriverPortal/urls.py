"""onlineDriverPortal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from driverjob.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('admin_login', admin_login, name="admin_login"),
    path('user_login', user_login, name="user_login"),
    path('employer_login', employer_login, name="employer_login"),
    path('user_register', user_register, name="user_register"),
    path('employer_register',employer_register, name="employer_register"),
    path('admin_home', admin_home, name="admin_home"),
    path('user_home', user_home, name="user_home"),
    path('user_jobs', user_jobs, name="user_jobs"),
    path('view_users', view_users, name="view_users"),
    path('drivers', drivers, name="drivers"),
    path('user_profile', user_profile, name="user_profile"),
    path('del_user/<int:pid>', del_user, name="del_user"),
    path('employer_home', employer_home, name="employer_home"),
    path('employer_profile', employer_profile, name="employer_profile"),
    path('employers', employers, name="employers"),
    path('employers_pending', employers_pending, name="employers_pending"),
    path('employers_accepted', employers_accepted, name="employers_accepted"),
    path('employers_rejected', employers_rejected, name="employers_rejected"),
    path('change_status/<int:pid>', change_status, name="change_status"),
    path('del_employer/<int:pid>', del_employer, name="del_employer"),
    path('Logout', Logout, name="Logout"),
    path('change_adminpwd', change_adminpwd, name="change_adminpwd"),
    path('change_userpwd', change_userpwd, name="change_userpwd"),
    path('change_emppwd', change_emppwd, name="change_emppwd"),
    path('post_job', post_job, name="post_job"),
    path('job_list', job_list, name="job_list"),
    path('all_jobs', all_jobs, name="all_jobs"),
    path('edit_job/<int:pid>', edit_job, name="edit_job"),
    path('job_details/<int:pid>', job_details, name="job_details"),
    path('apply_job/<int:pid>', apply_job, name="apply_job"),
    path('del_job/<int:pid>', del_job, name="del_job"),
    path('applicants', applicants, name="applicants"),



] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
