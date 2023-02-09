from django.contrib import admin
from .models import *
from .views import *
from datetime import datetime
# Register your models here.

@admin.register(contactEnquiry)
class conatctAdminenquiery(admin.ModelAdmin):
    change_list_template = 'admin/change_list_form.html'

    change_form_template = 'admin/change_form.html'

    add_form_template = 'admin/add_form.html'
    menu_title = "Contact Form"
    menu_group = "Frontend"
    
    #search_fields = ['company_categories', 'company_sub_categories', 'created_date', 'updated_date']
    list_display = ['name','email', 'phone_number','msg_subject', 'message','created_date', 'updated_date']
    list_per_page = 10
    
    
@admin.register(indexDashboard)
class IndexDashboardAdmin(admin.ModelAdmin):
    change_list_template = 'admin/change_list_form.html'

    change_form_template = 'admin/change_form.html'

    add_form_template = 'admin/add_form.html'
    menu_title = "Home Page"
    menu_group = "Frontend"
    
    list_display = ['index_title','logo', 'index_bannercontent','Banner_image', 'Scroll_content','created_date', 'updated_date']
    list_per_page = 10
    
@admin.register(testimonialDashboard)
class testimonialDashboardAdmin(admin.ModelAdmin):
    change_list_template = 'admin/change_list_form.html'

    change_form_template = 'admin/change_form.html'

    add_form_template = 'admin/add_form.html'
    menu_title = "Testimonial"
    menu_group = "Frontend"
    
    list_display = ['testimonial_title','client_image', 'client_content','created_date', 'updated_date']
    list_per_page = 10
    
@admin.register(trainingDashboard)
class trainingDashboardAdmin(admin.ModelAdmin):
    change_list_template = 'admin/change_list_form.html'

    change_form_template = 'admin/change_form.html'

    add_form_template = 'admin/add_form.html'
    menu_title = "Training"
    menu_group = "Frontend"

    list_display = ['training_title','training_image','created_date', 'updated_date']
    list_per_page = 10  
    
@admin.register(blogDashboard)
class blogDashboardAdmin(admin.ModelAdmin):
    change_list_template = 'admin/change_list_form.html'

    change_form_template = 'admin/change_form.html'

    add_form_template = 'admin/add_form.html'
    menu_title = "Blog"
    menu_group = "Frontend"

    list_display = ['bloging_title','bloging_image','created_date', 'updated_date']
    list_per_page = 10
    
    
    
@admin.register(termsConditions)
class termsConditionsAdmin(admin.ModelAdmin):
    change_list_template = 'admin/change_list_form.html'

    change_form_template = 'admin/change_form.html'

    add_form_template = 'admin/add_form.html'
    menu_title = "Terms & Conditions"
    menu_group = "Frontend"

    list_display = ['term_conditions_title','term_conditions_image','created_date', 'updated_date']
    list_per_page = 10
    
    
@admin.register(privacyPolicy)
class privacyPolicyAdmin(admin.ModelAdmin):
    change_list_template = 'admin/change_list_form.html'

    change_form_template = 'admin/change_form.html'

    add_form_template = 'admin/add_form.html'
    menu_title = "Privacy policy"
    menu_group = "Frontend"

    list_display = ['privacyPolicy_title','privacyPolicy_image','created_date', 'updated_date']
    list_per_page = 10 
    
@admin.register(aboutUs)
class aboutUsAdmin(admin.ModelAdmin):
    change_list_template = 'admin/change_list_form.html'

    change_form_template = 'admin/change_form.html'

    add_form_template = 'admin/add_form.html'
    menu_title = "About us"
    menu_group = "Frontend"

    list_display = ['about_us_title_head','about_us_image_head','created_date', 'updated_date']
    list_per_page = 10 
    
                                                          






@admin.register(Candidatefront)
class CandidatefrontAdmin(admin.ModelAdmin):
    change_list_template = 'admin/change_list_form.html'

    change_form_template = 'admin/change_form.html'

    add_form_template = 'admin/add_form.html'
    menu_title = "Candidatefront"
    menu_group = "Frontend"

    list_display = ['id','title','created_date','updated_date']
    list_per_page = 10
