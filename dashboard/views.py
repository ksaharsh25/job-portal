# Create your views here
# from msilib.schema import ListView
from django.views.generic import ListView
from django.core.paginator import Paginator
import time
#from multiprocessing import context
from multiprocessing import context
import re
from unittest import result
from django.http import HttpResponse
from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

import json
# from jobs.models import jobs
from django.views.decorators.csrf import csrf_exempt
from .models import *

from jobs.models import Employer, Job, CompanyCategories ,JobSeeker
from jobs.models import *
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from user.forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
#from  .forms import DocumentForm


def index(request):
    data= trainingDashboard.objects.all()   
    data5= JobSeeker.objects.all() 
    data2= testimonialDashboard.objects.all().order_by('-pk')[:3]
    categories = CompanyCategories.objects.all()
    data4 = indexDashboard.objects.all().values()[0]
    jobs = Job.objects.all().values('job_catagories')[:6]
    list_job = []
    for i in jobs:
        job = CompanyCategories.objects.filter(pk = i['job_catagories'])
        for j in job:
            list_job.append(j)
    context={'data':data, 'data2':data2 , 'data3': list_job, 'data4': data4,'data5': data5, 'categories':categories }
    return render(request, 'index.html',context)







def error(request):
        # person= {'lakshya': 'error'}
    data={'person' : 'ajit' }
    return render(request, '404.html',data)


def AboutUs(request):
    data= aboutUs.objects.all().values()[0]
    data2= testimonialDashboard.objects.all().order_by('-pk')[:3]
    context={'data':data, 'data2':data2 }
    return render(request, 'about.html',context)

def Dashboard_My_Profile(request):
    seeker = JobSeeker.objects.get(job_seeker_id=request.session['seeker_id'])
    context={'data':seeker,}
    return render(request, 'candidatesprofile.html',context)





def Contact(request):
    
    if request.method =="POST":
        Your_Name = request.POST['Your_Name']
        Your_Email = request.POST['Your_Email']
        Phone_Number = request.POST['Phone_Number']
        Your_Subject = request.POST['Your_Subject']
        Your_Message = request.POST['Your_Message']
        
        database = contactEnquiry(name=Your_Name, email=Your_Email, phone_number=Phone_Number, 
                              msg_subject=Your_Subject, message=Your_Message)
        database.save()
        time.sleep(3.5)
    
    
    return render(request, 'contact.html')


def TermsCondition(request):
    
    data= termsConditions.objects.all()   
    context={'data':data}
    return render(request, 'terms-condition.html',context)


def PrivacyPolicy(request):
    pdata = privacyPolicy.objects.all()
    context={'pdata': pdata}
    return render(request, 'privacy-policy.html',context)

def blog(request):
    data= blogDashboard.objects.all().order_by('-pk')[:6]
    
    def check_page(data, page_number=None, obj_per_page=None):
        
        paginator = Paginator(data, obj_per_page)
        try:
            page_obj = paginator.get_page(page_number)  # returns the desired page object
        except Paginator.PageNotAnInteger:
            # if page_number is not an integer then assign the first page
            page_obj = paginator.page(1)
        except Paginator.EmptyPage:
            # if page is empty then return last page
            page_obj = paginator.page(paginator.num_pages)
        
        return page_obj
    page_obj = check_page(data, page_number=request.GET.get('page'), obj_per_page=5)
    context={'page_obj': page_obj,'data':data}
    return render(request, 'blog.html',context)

def blog_details(request, blogID):
    data =  blogDashboard.objects.get(id=int(blogID))
    data2 = blogDashboard.objects.all().order_by('-pk')[:8] 
    return render(request, 'blog-details.html', context={'data':data,'data2':data2})



def Candidate_Dashboard_cv_Manager(request):
    return render(request, 'candidates-dashboard-cv-manager.html')    

 
def Categories(request):
    return render(request, 'categories.html')

def ComingSoon(request):
    return render(request, 'coming-soon.html')

def CompanyDetails(request):
    return render(request, 'company-details.html') 

def Company(request):
    return render(request, 'company.html')      

      

def Dashboard_Applicants(request):
    return render(request, 'dashboard-applicants.html')  

def Dashboard_Change_Password(request):
    return render(request, 'dashboard-change-password.html')  

def Dashboard_Company_Profile(request):
    if request.method =="POST":
        Company_name = request.POST['Company_name']
        Email_address = request.POST['Email_address']
        Phone = request.POST['Phone']
        Website = request.POST['Website']
        About_Company = request.POST['About_Company']
        Established_date = request.POST['Established_date']
        # Country = request.POST['Country']
        # City = request.POST['City']
        Complete_Address = request.POST['Complete_Address']
        Pin_Code = request.POST['Pin_Code']
        Facebook_URL = request.POST['Facebook_URL']
        Twitter_URL = request.POST['Twitter_URL']
        Linkedin_URL = request.POST['Linkedin_URL']
        Instagram_URL = request.POST['Instagram_URL']
        company_image1 = request.POST['myprofileimage']
        
 
        Dashboard = Employer(employer=Company_name, email=Email_address, mobile_number=Phone, website=Website,
                             about_company=About_Company, established_date=Established_date, address=Complete_Address, 
                             pin_code=Pin_Code, Facebook=Facebook_URL, Twitter=Twitter_URL, Linkedin=Linkedin_URL,
                             Instagram=Instagram_URL, image=company_image1)
        
        Dashboard.save()
        
    return render(request, 'dashboard-company-profile.html') 


def Dashboard_Manage_Job(request):
    return render(request, 'dashboard-manage-job.html')  

def Dashboard_Messages(request):
    return render(request, 'dashboard-messages.html')  


def PostJob(request):
    categories = CompanyCategories.objects.all()
                
    if request.method == "POST":
        job_title=request.POST['job_title']
        job_dec=request.POST['job_dec']
        mobile_number=request.POST['mobile_number']
        company_name=request.POST['Company_name']
        category=request.POST['category']
        email=request.POST['emailus']
        offered_Salary=request.POST['offered_Salary']
        Experience=request.POST['Experience']
        Qualification=request.POST['Qualification']
        deadline=request.POST['deadline']
        states=request.POST['States']
        city=request.POST['City']
        Address=request.POST['Address']
        company_image2 = request.POST['myprofileimage2']
        category=request.POST['category']
        
        
        postjob = JobPosting(job_title=job_title, job_description=job_dec, 
                      comapny_Name=company_name ,deadline_date=deadline,offered_salary= offered_Salary ,experience=Experience,
                      qualification=Qualification ,States=states ,city=city, complete_address=Address ,email=email, company_image2=company_image2,
                      mobile_number=mobile_number,job_catagories= CompanyCategories.objects.get(id=category) ,
                    #   company_profile_image=attachments
        )        
        
        postjob.save()
        
        return render(request, 'dashboard-post-job.html', context={'data':categories})

    return render(request, 'dashboard-post-job.html', context={'data':categories})  



def EmployersDetails(request, empID):
    # # em = Employer.objects.all().filter(int = industry).first()
   if request.method == 'GET':
        jobs = Job.objects.all().filter(employer_id=empID)
        context = {
            'empID': empID,
            'employer': Employer.objects.get(id=int(empID)),
            'jobs': len(jobs),
            }
  
        return render(request, 'employers-details.html', context) 
   



# @login_required()
def Candidates_Dashboard(request):
    if request.method == "GET":
        seeker = JobSeeker.objects.get(job_seeker_id=request.session['seeker_id'])
        return render(request, 'candidates-dashboard.html', context={'data':seeker})
                
    if request.method == "POST":
        # seeker = JobSeeker.objects.get(mobile_number=request.POST['mobile_number'])
        
        full_name=request.POST['full_name']
        date_birth=request.POST['date_birth']
        gender=request.POST['gender']
        
        working_experience=request.POST['working_experience']
        email_id=request.POST['email_id']
        address=request.POST['address']
        about_me=request.POST['about_me']
        education=request.POST['education']
        
        profile_image=request.FILES['profile_image']
        my_file=request.FILES['my_file']
        
        
        
        JobSeeker.objects.filter(mobile_number=request.POST['mobile_number']).update(full_name=full_name, date_birth=date_birth, 
                      gender=gender ,working_experience= working_experience ,email_id=email_id,
                      address=address, about_me=about_me, education=education,profile_image=profile_image,my_file=my_file
                    
        )        
        
    
    return render(request, 'candidates-dashboard.html', context={'data':request.session['seeker_id']})    


    



def Candidates_Listing(request):
    data= JobSeeker.objects.all().order_by('-pk')[:4]   
    # data2= testimonialDashboard.objects.all().order_by('-pk')[:3]
    context={'data':data }
    return render(request,'candidates-listing.html',context)


def EmployersListing(request):
    data2= trainingDashboard.objects.all()  
    data= Employer.objects.all().order_by('-pk')[:8]   
    context={'data':data,'data2':data2 }
    return render(request, 'employers-listing.html',context)

 
def EmployersDetails(request, empID):
    
        data =  Employer.objects.get(id=int(empID))
        return render(request, 'employers-details.html', context={'data':data})




def candidates_Listing(request):
    data= JobSeeker.objects.all().order_by('-pk')[:8]   
    context={'data':data }
    return render(request,'candidates-listing.html',context)


def candidates_details(request, JobSeekerID):
    data =  JobSeeker.objects.get(job_seeker_id=int(JobSeekerID))
    return render(request, 'candidates-details.html', context={'data':data})


def JobListing(request):
    data = Job.objects.all().order_by('-pk')
    categories = CompanyCategories.objects.all()
    # paginator = Paginator(data, 5)  
    # page_number = request.GET.get('page')
    
    def check_page(data, page_number=None, obj_per_page=None):
        
        paginator = Paginator(data, obj_per_page)
        try:
            page_obj = paginator.get_page(page_number)  # returns the desired page object
        except Paginator.PageNotAnInteger:
            # if page_number is not an integer then assign the first page
            page_obj = paginator.page(1)
        except Paginator.EmptyPage:
            # if page is empty then return last page
            page_obj = paginator.page(paginator.num_pages)
        
        return page_obj
    
    if request.method == 'POST':
        if request.POST['category'] != 'All Categories':
            category = request.POST.get('category')
            data = Job.objects.filter(job_catagories=category).order_by('-pk')
            page_obj = check_page(data, page_number=request.GET.get('page'), obj_per_page=5)
            return render(request, 'job-listing.html', context={'data':data, 'page_obj': page_obj, 'categories':categories})

    
    page_obj = check_page(data, page_number=request.GET.get('page'), obj_per_page=5)
    context={'page_obj': page_obj, 'categories':categories}
    
    return render(request, 'job-listing.html',context)



def jobDetails(request, jobID):
    data =  Job.objects.get(id=int(jobID))
    try:
        seeker = JobSeeker.objects.get(job_seeker_id=request.session["seeker_id"])
        if Applicant.objects.filter(job_catagories=data.job_catagories, job_Application_name=data, jobseeker_name=seeker).exists():
            applied = {'value':True}
        else:
            applied = {'value':False}
    except:
        applied = {'NotValue':'NeedLogin'}
    data2 = {'Facebook': data.employer.Facebook}
    {'Twitter': data.employer.Twitter}
    {'Instagram': data.employer.Instagram}
    {'Youtube': data.employer.Youtube}
    return render(request, 'job-details.html', context={'data':data,'data2':data2, 'applied':applied})



def whychooseus(request):
    data= Candidatefront.objects.all()   
    context={'data':data}
    return render(request,'why-choose.html',context)




def register(request):
    if request.method == "POST":
        full_name=request.POST['Fname']
        mobile_number=request.POST['Mobile']
        gender=request.POST['gender']
        email_id=request.POST['Email']
        password=request.POST['Password']
        register = JobSeeker(full_name=full_name, gender=gender ,mobile_number=mobile_number,email_id=email_id,
                            password=password
        )   
        register.save()
    return render(request, 'register.html')


def ApplyJob(request, id):
    job = Job.objects.get(id = id)
    seeker = JobSeeker.objects.get(job_seeker_id = request.session['seeker_id'])
    appliedjob = Applicant.objects.all().filter(jobseeker_name=seeker)

    if Applicant.objects.filter(job_catagories=job.job_catagories, job_Application_name=job, jobseeker_name=seeker).exists():
        return render(request,template_name="job-details.html", context={'message':'Already Applied', 'data':appliedjob})

    else:
        Applicant.objects.create(job_catagories=job.job_catagories, employer=job.employer, job_Application_name=Job.objects.get(
            id=job.id), jobseeker_name=seeker, selection_status='Pending')
        return render(request,template_name="job-details.html", context={'message':'Applied Successfully', 'data':appliedjob})

def appliedjobdetails(request, JobSeekerID): 
   if request.method == 'GET':
        appliedjob = Applicant.objects.all().filter(jobseeker_name=JobSeekerID)

        return render(request, 'applied.html', context={'data':appliedjob, 'seeker':request.session['seeker_id']})



