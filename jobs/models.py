from email.policy import default
from django.db import models
from datetime import datetime
from django.conf import settings
from jobs import utils
from user.models import User
from Address.models import Country, State, City
from django.core.validators import RegexValidator
from smart_selects.db_fields import ChainedForeignKey
#from phone_field import PhoneField
from multiselectfield import MultiSelectField
from django.core.validators import MaxValueValidator, MinValueValidator
from tinymce.models import HTMLField

Published_By = (('Frontend', 'Frontend'),('Backend', 'Backend'),)
class RoleModel(models.Model):
    userrolemodal = models.CharField(max_length=200)

    def __str__(self):
        return self.userrolemodal

class JobType(models.Model):
    type = models.CharField(choices=utils.CHOICES, max_length=200, unique=True)

    def __str__(self):
        return self.type
    
    class Meta:
        verbose_name_plural = "Job Type" 

class UserRole(models.Model):
    User_role = models.ForeignKey(
        RoleModel, on_delete=models.CASCADE, verbose_name="Company_infos")
    Name = models.CharField(max_length=50)
    Email = models.EmailField()
    phone_number = models.BigIntegerField(max_length=13)

    def __str__(self):
        return self.Name
    
    class Meta:
        verbose_name_plural = "User role" 





class CompanyCategories(models.Model):
    company_categories = models.CharField(blank=False, max_length=100, verbose_name="category",unique=True)
    company_sub_categories = models.CharField(blank=True, max_length=100, verbose_name="department")
    categories_image  = models.ImageField(upload_to='category', default='default/1.png')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company_categories
    
    class Meta:
        verbose_name_plural = "Company Categories" 


class Employer(models.Model):
    
    industry = models.ForeignKey(CompanyCategories, on_delete=models.CASCADE, verbose_name="company category", null=True, blank=True)
  #  industry=ChainedForeignKey(CompanyCategories,chained_field="company_categories",chained_model_field="company_categories",show_all=False,auto_choose=True,sort=True)
    employer = models.CharField(blank=False, max_length=100) 
    established_date = models.DateField(blank=True, null=True)
    address = models.CharField(blank=False, max_length=200)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, blank=True)
    state = ChainedForeignKey(State,chained_field="country",chained_model_field="country",show_all=False,auto_choose=True,sort=True, null=True, blank=True)
    city = ChainedForeignKey(City,chained_field="state",chained_model_field="state",show_all=False,auto_choose=True,sort=True, null=True, blank=True)
    pin_code = models.PositiveIntegerField(max_length=7,null=True, blank=True)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,10}$', message="Phone number must be entered in the format +919999999999. Up to 14 digits allowed.")
    mobile_number = models.CharField(
        validators=[phone_regex], blank=False, max_length=11, unique=True)
    website = models.CharField(blank=True, max_length=200)
    email = models.CharField(blank=False, unique=True, max_length=100)
    about_company = HTMLField(null=True, blank=True)
    Facebook = models.URLField(blank=True, null=True)
    Twitter = models.URLField(blank=True, null=True)
    Linkedin = models.URLField(blank=True, null=True)
    Instagram = models.URLField(blank=True, null=True)
    Youtube = models.URLField(blank=True , null=True)
    Others = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='companyimage', default='default/1.png')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    # profile_image = models.ImageField(upload_to='companyimage', null=True, blank=True)

    def __str__(self):
        return str(self.employer)
    
    class Meta:
        verbose_name_plural = "Employer" 


class HrInfo(models.Model):
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE, verbose_name="employer")
    hr_name = models.CharField(blank=False, max_length=30)
    
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,10}$', message="Phone number must be entered in the format +919999999999. Up to 11 digits allowed.")
    
    hr_phone = models.CharField(validators=[phone_regex], blank=False, max_length=11, unique=True)
    hr_email = models.CharField(blank=False, unique=True, max_length=100)
    
#    staff_name = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="staff name", blank=True,null=True,editable=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.hr_name)

    def employer_name(self):
        return self.employer

    def employer_email(self):
        return self.employer.email

    def employer_number(self):
        return self.employer.mobile_number
    
    class Meta:
        verbose_name_plural = "Hr" 



  
class JobSeeker(models.Model):
    job_seeker_id = models.BigAutoField(primary_key=True)
    full_name = models.CharField(max_length=355, null=True, blank=True)
    date_birth = models.DateField(blank=True, null=True)
   
    job_category = models.ManyToManyField(CompanyCategories,null=True, blank=True)
    gender = models.CharField(max_length=10,   null=True, blank=True)
    
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,10}$', message="Phone number must be entered in the format +919999999999. Up to 14 digits allowed.")
    mobile_number = models.CharField(
        validators=[phone_regex], blank=False, max_length=11, unique=True)
    otp = models.CharField(max_length=7, blank=True, null=True)
    email_id = models.EmailField(null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, blank=True)
    state = ChainedForeignKey(State,chained_field="country",chained_model_field="country",show_all=False,auto_choose=True,sort=True, null=True, blank=True)
    city = ChainedForeignKey(City,chained_field="state",chained_model_field="state",show_all=False,auto_choose=True,sort=True, null=True, blank=True)
    pin_code = models.PositiveIntegerField(max_length=7, null=True, blank=True)
    looking_for = models.ManyToManyField(JobType, max_length=200)
    working_experience = models.IntegerField(default=0, validators=[MaxValueValidator(100), MinValueValidator(1)], null=True, blank=True)
    about_me = HTMLField(null=True, blank=True)
    address = models.TextField(max_length=300, null=True, blank=True)
    education= models.CharField(choices=utils.educations_choices, max_length=150)
    profile_image = models.ImageField(upload_to='profileimage',default='default/2.jpg')
    my_file = models.FileField(upload_to='documents', null=True, blank=True)
    # is_phone_verified=models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def job_categories(self):
        joblist = []
        for i in self.job_category.values():
            joblist.append(i['company_categories'])
        return joblist    


    def __str__(self):
        return self.mobile_number
    
    class Meta:
        verbose_name_plural = "Job seeker" 
   



class Job(models.Model):

    job_title = models.CharField(max_length=200)
    staff_name = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="staff name",null=True, blank=True)
    published_by = models.CharField(choices=Published_By, max_length=30, null=True, blank=True)
    job_catagories = models.ForeignKey(CompanyCategories, on_delete=models.CASCADE, verbose_name="job category")
    employer= ChainedForeignKey(Employer,chained_field="job_catagories",chained_model_field="industry",show_all=False,auto_choose=True,sort=True)
    
    hr_name= ChainedForeignKey(HrInfo,chained_field="employer",chained_model_field="employer",show_all=False,auto_choose=True,sort=True,null=True, blank=True)
  
    
    job_designation = models.CharField(blank=False, max_length=100, verbose_name="job designation")
    
    country = models.ForeignKey(Country, on_delete=models.CASCADE,blank=True, null=True)
    state = ChainedForeignKey(State,chained_field="country",chained_model_field="country",show_all=False,auto_choose=True,sort=True,blank=True, null=True)
    city = ChainedForeignKey(City,chained_field="state",chained_model_field="state",show_all=False,auto_choose=True,sort=True,blank=True, null=True)
    pin_code = models.PositiveIntegerField(max_length=7,blank=True, null=True)
    
    description = HTMLField(null=True, blank=True)
    about_company = HTMLField(null=True, blank=True)
    key_responsibilities = HTMLField(null=True, blank=True)
    skill_experience = HTMLField(null=True, blank=True)
    
    
    job_opening_date = models.DateField(default=datetime.now, blank=True)
    job_type = models.CharField(choices=utils.CHOICES, max_length=150)
    is_published = models.BooleanField(default=True)
    Number_vacancy = models.CharField(max_length=10, null=True)
    experience = models.CharField(max_length=100)
    
    salary_min = models.IntegerField(default=1, validators=[MaxValueValidator(100000), MinValueValidator(1)])
    salary_max = models.IntegerField(default=1, validators=[MaxValueValidator(100000), MinValueValidator(1)])
    company_profile_image = models.ImageField(upload_to='companyimage', null=True, blank=True)
    job_end_date = models.DateField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.job_title

    def hr_phone(self):
        if self.hr_name != None:
            return self.hr_name.hr_phone
        else:
            pass

    def hr_email(self):
        if self.hr_name != None:
            return self.hr_name.hr_email
        else:
            pass

    def staff_fullname(self):
        if self.staff_name != None:
            return self.staff_name.full_name

    def staff_email(self):
        if self.staff_name != None:
            return self.staff_name.email

    def staff_mobile(self):
        if self.staff_name != None:
            return self.staff_name.mobile_number
        
    class Meta:
        verbose_name_plural = "Job List"


class FavouriteJob(models.Model):
    jobseeker = models.ForeignKey(JobSeeker, on_delete=models.CASCADE, verbose_name="JobSeeker")
    job = models.ForeignKey(Job, on_delete=models.CASCADE, verbose_name="JobSeeker")

    class Meta:
        unique_together = ['jobseeker', 'job']


class Applicant(models.Model):
    job_Application_id = models.BigAutoField(primary_key=True)
    job_catagories = models.ForeignKey(CompanyCategories, on_delete=models.CASCADE, verbose_name="job category")
    employer= ChainedForeignKey(Employer,chained_field="job_catagories",chained_model_field="industry",show_all=False,auto_choose=True,sort=True,null=True, blank=True)
    
    hr_name= ChainedForeignKey(HrInfo,chained_field="employer",chained_model_field="employer",show_all=False,auto_choose=True,sort=True,null=True, blank=True)
    job_Application_name = ChainedForeignKey(Job,chained_field="hr_name",chained_model_field="hr_name",show_all=False,auto_choose=True,sort=True,null=True, blank=True)
   
   
    staff_name = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="staff name",null=True, blank=True)
    jobseeker_name = models.ForeignKey(JobSeeker, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    selection_status = models.CharField(choices=utils.selection_chose, max_length=30)
    

    class Meta:
        unique_together = ('job_catagories', 'jobseeker_name', 'job_Application_name')
        verbose_name_plural = "Applications"

    def __str__(self):
        return self.selection_status

    def jobseekers_name(self):
         return self.jobseeker_name.full_name

    def jobseeker_email(self):
        return self.jobseeker_name.email_id

    def jobseeker_number(self):
        return self.jobseeker_name.mobile_number
         



class JobPosting(models.Model):
    job_title=models.CharField(max_length=55,null=True, blank=True)
    published_by = models.CharField(choices=Published_By, max_length=30, null=True, blank=True, default='Frontend')
    job_description=models.TextField(max_length=1055,null=True, blank=True)
    comapny_Name = models.CharField(max_length=55,null=True, blank=True)
    job_catagories = models.ForeignKey(CompanyCategories, on_delete=models.CASCADE, verbose_name="job category",null=True, blank=True)
    email = models.CharField(max_length=55,null=True, blank=True)
    offered_salary=models.IntegerField(max_length=55,null=True, blank=True)
    experience=models.CharField(max_length=55,null=True, blank=True)
    industry: models.CharField(max_length=55,null=True, blank=True)
    qualification= models.CharField(max_length=55,null=True, blank=True)
    deadline_date=models.DateField(auto_now=True)
    States=models.CharField(max_length=55,null=True, blank=True)
    city= models.CharField(max_length=55,null=True, blank=True)
    complete_address= models.CharField(max_length=155,null=True, blank=True)
    company_image2 = models.ImageField(upload_to='companyimage', null=True, blank=True)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,10}$', message="Phone number must be entered in the format +919999999999. Up to 14 digits allowed.")
    mobile_number = models.CharField(validators=[phone_regex], blank=True, max_length=11, null=True)
    is_verified = models.BooleanField(default=False, help_text=('verify the employer then save'))
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)  
    
    def __str__(self):
            return self.job_title
    
    
    class Meta:
        verbose_name_plural = "Post Job"     
        
    def save(self, *args, **kwargs):
        try:
            not_verified_job_posting = JobPosting.objects.get(id = self.id)
            if not_verified_job_posting.is_verified == False and self.is_verified == True:
                try:
                    company = Employer.objects.filter(employer = self.comapny_Name)
                except Employer.DoesNotExist:    
                    company = Employer.objects.create(employer=self.comapny_Name, email=self.email, mobile_number=self.mobile_number)
                Job.objects.create(job_title=self.job_title, employer=company, salary_max= self.offered_salary, is_published=True, description=self.job_description, job_catagories=self.job_catagories, published_by=self.published_by)
            return super().save()
        except:
            return super().save()
