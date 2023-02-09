from typing import Counter
from django.contrib import admin

from jobs.forms import *
from .models import Applicant, JobPosting
from jobs.models import Employer, HrInfo, JobSeeker, CompanyCategories as Category, Job, JobPosting, FavouriteJob, JobType

from import_export.admin import ImportExportModelAdmin
from Address.models import *


@admin.register(Category)
class CompanyCategories(ImportExportModelAdmin):
    change_list_template = 'admin/change_list_form.html'

    change_form_template = 'admin/change_form.html'

    add_form_template = 'admin/add_form.html'
    menu_title = "company categories "
    menu_group = "categories"
    
    search_fields = ['company_categories', 'company_sub_categories', 'created_date', 'updated_date']
    list_display = ['company_categories','company_sub_categories', 'created_date', 'updated_date']
    list_per_page = 10




class EmployerAdmin(ImportExportModelAdmin):
    model = Employer
    field = ['__all__']

    change_list_template = 'admin/change_list_form.html'

    change_form_template = 'admin/change_form.html'
    add_form_template = 'admin/add_form.html'

    menu_title = "Employer"
    menu_group = "Accounts"
   # list_filter = ['employer', 'created_date', 'updated_date']
    list_display = ['id','employer', 'mobile_number', 'email',
                    'country', 'state', 'city', 'industry', 'created_date', 'updated_date']
    autocomplete_fields = ['industry']
    search_fields = ['employer', 'industry__company_categories', 'country__country', 'state__state', 'city__city', 'mobile_number', 'email']
    list_per_page = 10

admin.site.register(Employer, EmployerAdmin)


@admin.register(HrInfo)
class HrList(ImportExportModelAdmin):
    change_list_template = 'admin/change_list_form.html'

    change_form_template = 'admin/change_form.html'

    add_form_template = 'admin/add_form.html'
    menu_group = "Accounts"
    menu_title = "hr list"
    search_fields = ['employer__employer', 'employer__email', 'employer__mobile_number',
                     'hr_name', 'hr_phone', 'hr_email']
   # list_filter = ['employer', 'hr_name', 'created_date', 'updated_date']
    list_display = ['employer_name', 'employer_email', 'employer_number', 'hr_name', 'hr_phone',
                    'hr_email', 'created_date', 'updated_date']
    autocomplete_fields = ['employer']
    list_per_page = 10

class FavouriteJobInline(admin.TabularInline):
    model = FavouriteJob
    fields = ('jobseeker', 'job')

    def get_extra(self, request, obj=None, **kwargs):
        if obj:
            return 0
        else:
            return 1


@admin.register(JobSeeker)
class JobSeekers(ImportExportModelAdmin):
    change_list_template = 'admin/change_list_form.html'

    change_form_template = 'admin/change_form.html'

    add_form_template = 'admin/add_form.html'

    menu_group = "Accounts"
    menu_title = "Job seekers"

    inlines = [FavouriteJobInline]

    list_display = ['job_seeker_id', 'full_name', 'email_id', 'mobile_number',
                      'state', 'city','job_categories', 'created_date', 'updated_date']
    search_fields = ['job_seeker_id', 'full_name', 'email_id',
                     'mobile_number', 'job_category__company_categories','job_category__company_sub_categories', 'country__country', 'state__state', 'city__city']

   
    autocomplete_fields = ['job_category']
    list_per_page = 15


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    change_list_template = 'admin/change_list_form.html'

    change_form_template = 'admin/change_form.html'

    add_form_template = 'admin/add_form.html'
    menu_title = "Job list"
    menu_group = "Jobs details"

    list_display = ('job_title' , 'published_by','job_catagories','employer','hr_name', 'hr_phone', 'staff_fullname', 'staff_email',
                    'staff_mobile', 'job_opening_date','state', 'city','job_end_date', 'created_date', 'updated_date')

    search_fields = ['job_title','employer__employer', 'employer__email', 'hr_name__hr_name', 'hr_name__hr_email', 'hr_name__hr_phone', 'job_catagories__company_categories','job_catagories__company_sub_categories',
                     'employer__mobile_number', 'staff_name__first_name', 'staff_name__email', 'staff_name__mobile_number', 'created_date', 'updated_date','country__country', 'state__state', 'city__city']
   # list_filter = ['employer', 'hr_name', 'job_opening_date', 'job_end_date']
    list_editable = ['job_end_date']
    autocomplete_fields = ['job_catagories','staff_name',] #'hr_name', 'employer',
    list_per_page = 10

@admin.register(Applicant)
class Applicant(admin.ModelAdmin):
    change_list_template = 'admin/change_list_form.html'

    change_form_template = 'admin/change_form.html'

    add_form_template = 'admin/add_form.html'
    menu_title = "Application"
    menu_group = "Jobs details"
    list_display = ['jobseekers_name','jobseeker_number', 'jobseeker_email', 'job_Application_name',
                    'created_date', 'updated_date', 'selection_status']
    list_editable = ['selection_status']

    search_fields = ['jobseeker_name__mobile_number', 'jobseeker_name__full_name','employer__employer', 'employer__email', 'employer__mobile_number','hr_name__hr_name', 'hr_name__hr_email', 'hr_name__hr_phone', 
                     'job_Application_name__job_title', 'staff_name__first_name', 'staff_name__email', 'staff_name__mobile_number', 'jobseeker_name__email_id', 'selection_status']
   # list_filter = ['employer', 'hr_name', 'created_date', 'updated_date']
    autocomplete_fields = ['jobseeker_name', 'staff_name',]
    list_per_page = 10



@admin.register(JobPosting)
class JobPostDashboardAdmin(admin.ModelAdmin):
    change_list_template = 'admin/change_list_form.html'

    change_form_template = 'admin/change_form.html'

    add_form_template = 'admin/add_form.html'
    menu_title = "Post Job"
    menu_group = "Jobs details"

    list_display = ['job_title','comapny_Name','published_by',"deadline_date",'created_date', 'updated_date']
    list_per_page = 10      

# admin.site.register(JobType)
