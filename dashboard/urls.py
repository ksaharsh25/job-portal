from django.urls import path
from . import views
# from imageapp import views
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

app_name = 'dashboard'
urlpatterns = [
    path('', views.index, name='home'),
    path('error', views.error, name='404'),
    
    path('aboutUs', views.AboutUs, name='about'),
    
    path('blog_details/<int:blogID>', views.blog_details, name='blog_details'),
    path('blog', views.blog, name='blog'),
   # path('candidates_Listing', views.candidates_Listing, name='candidates_Listing'),
    path('jobseeker/<int:JobSeekerID>', views.candidates_details, name='jobseeker'), 
    
    path('employer/<int:empID>', views.EmployersDetails, name='EmployerDetails'),
    
    path('contact', views.Contact, name='Contact'),
    path('Dashboard_Company_Profile', views.Dashboard_Company_Profile, name='Dashboard_Company_Profile'),

    path('PostJob', views.PostJob, name='PostJob'),
    path('EmployersListing', views.EmployersListing, name='EmployersListing'),
    path('Dashboard_My_Profile', views.Dashboard_My_Profile, name='Dashboard_My_Profile'),
    
    path('JobDetails/<int:jobID>', views.jobDetails, name='job_detail'), 
    path('JobListing', views.JobListing, name='Joblisting'),
    path('LoginRegisterPopup', views.Candidates_Dashboard, name='LoginRegisterPopup'),
    path('LoginRegister', views.register, name='LoginRegister'),
    
    path('PrivacyPolicy', views.PrivacyPolicy, name='PrivacyPolicy'),
  
    path('TermsCondition', views.TermsCondition, name='TermsCondition'),
    # path('JobDetails', views.job_details, name='job_detail'), 
    path('candidates_Listing', views.whychooseus, name='candidates_Listing'),
    path('applied/<int:JobSeekerID>', views.appliedjobdetails, name='applied'),
    path('apply/<int:id>', views.ApplyJob, name= 'jobapply'),

]

if settings.DEBUG: urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
