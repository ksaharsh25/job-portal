from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from .models import *
import random as r
import boto3

client = boto3.client("sns",
    aws_access_key_id="AKIA242PPGB5KEAPBAVE",
    aws_secret_access_key="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",
    region_name="ap-south-1"
)


def get_otp():
    otp = ""
    for i in range(4):
        otp += str(r.randint(1,9))
    return otp


# Create your views here.
def login(request):
    if request.method == "POST":
        phone = request.POST.get('logfirstfield')
        try:
            # if Mobile already exists the take this else create New One
            Mobile = JobSeeker.objects.get(mobile_number=phone)
            request.session['isNewUser'] = False
        except ObjectDoesNotExist:
            JobSeeker.objects.create(
                mobile_number=phone,
            )
            request.session['isNewUser'] = True
            Mobile = JobSeeker.objects.get(
                mobile_number=phone)  # user Newly created Model
        Mobile.save()  # Save the data
        OTP = get_otp()
        client.publish(
            PhoneNumber="+91"+phone,
            Message="You OTP is " + OTP
        )
        Mobile.otp = OTP
        Mobile.save()
        request.session['mobile'] = phone
        return redirect('otp')
        
    return render(request,'login.html')

def otp(request):
    phone = request.session['mobile'] 
    context = {'mobile':phone}
    if request.method == 'POST':
        otp = request.POST.get('logsecondfield')
        jobseeker = JobSeeker.objects.filter(mobile_number=phone,otp=otp).first()

        
        if JobSeeker.objects.filter(mobile_number=phone,otp=otp).count() > 0:
            request.session['jobseeker_name'] = jobseeker.full_name
            request.session['jobseeker_image'] = jobseeker.profile_image.url
            request.session['jobseeker'] = True
            request.session['seeker_id'] = JobSeeker.objects.get(mobile_number=phone).job_seeker_id
            if request.session['isNewUser']== True:
                return redirect('/LoginRegisterPopup')
            else:
                return redirect('/JobListing')
            
        else:
            context = {'message' : 'Wrong OTP' , 'class' : 'danger','mobile':phone }
            return render(request,'otp.html' , context)
    return render(request, 'otp.html', context)


def logout(request):
    del request.session['jobseeker_name']
    del request.session['jobseeker_image']
    del request.session['seeker_id']
    del request.session['jobseeker']
    return redirect('/')
    