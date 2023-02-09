from django.db import models
from datetime import datetime
from tinymce.models import HTMLField
#Create your models here.
class contactEnquiry(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=60)
    phone_number=models.CharField(max_length=58)
    msg_subject=models.CharField(max_length=70)
    message=models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name 
    class Meta:
        verbose_name_plural = "Contact"
        
    
    
class indexDashboard(models.Model):
    index_title=models.CharField(max_length=55)
    logo=models.ImageField(upload_to= 'indexpage' )
    index_bannercontent= HTMLField()  
    Banner_image=models.ImageField(upload_to= 'indexpage' )
    Scroll_content= HTMLField() 
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.index_title 
    
    class Meta:
        verbose_name_plural = "Home Page"
    
    
class testimonialDashboard(models.Model):
    testimonial_title=models.CharField(max_length=55)
    client_image=models.ImageField(upload_to= 'testimonial' )
    client_content= HTMLField() 
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.testimonial_title 
    
    class Meta:
        verbose_name_plural = "Testimonial"
    
class trainingDashboard(models.Model):
    training_title=models.CharField(max_length=55)
    training_image=models.ImageField(upload_to= 'training' )
    client_content= HTMLField() 
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True) 
    
    def __str__(self):
        return self.training_title 
    
    class Meta:
        verbose_name_plural = "Training"       
    
class ContactDashboard(models.Model):
      address_content= models.CharField(max_length=255)
      call_us=models.BigIntegerField(max_length=13)
      email=models.EmailField()
      map_url=models.URLField()
      created_date = models.DateTimeField(auto_now_add=True)
      updated_date = models.DateTimeField(auto_now=True)
      
      
      def __str__(self):
            return self.address_content
        
      class Meta:
            verbose_name_plural = "Contact Details"   
        
class blogDashboard(models.Model):
    bloging_title=models.CharField(max_length=55)
    bloging_image=models.ImageField(upload_to= 'blogDashboard' )
    bloging_content= HTMLField() 
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
            return self.bloging_title
        
    class Meta:
        verbose_name_plural = "Blogs"     
    
class termsConditions(models.Model):
    term_conditions_title=models.CharField(max_length=55)
    term_conditions_image=models.ImageField(upload_to= 'termsConditions' )
    term_conditions_content= HTMLField() 
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)  
    
    def __str__(self):
            return self.term_conditions_title
        
    class Meta:
        verbose_name_plural = "Terms Conditions"     
        
class privacyPolicy(models.Model):
    privacyPolicy_title=models.CharField(max_length=55)
    privacyPolicy_image=models.ImageField(upload_to= 'privacyPolicy' )
    privacyPolicy_content= HTMLField() 
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)  
    
    def __str__(self):
            return self.privacyPolicy_title 
        
    class Meta:
        verbose_name_plural = "Privacy Policy"     
        
        
        
class aboutUs(models.Model):
    about_us_title_head=models.CharField(max_length=55)
    about_us_image_head=models.ImageField(upload_to= 'about_us' )
    about_us_content1= HTMLField() 
    manager_title_head=models.CharField(max_length=55)
    manager_image_head=models.ImageField(upload_to= 'about_us' )
    designation: models.CharField(max_length=55)
    about_us_content= HTMLField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)  
    
    def __str__(self):
            return self.about_us_title_head
    
    class Meta:
        verbose_name_plural = "About us"     
        
        

                     
            
      
       
        


class Candidatefront(models.Model):
    title=models.CharField(max_length=55)
    front_image=models.ImageField(upload_to= 'Candidatefront' )
    candidate_content= HTMLField() 
    sub_title=models.CharField(max_length=55)
    sub_content= HTMLField() 
    back_image=models.ImageField(upload_to= 'Candidatefront' )
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def str(self):
            return self.title
