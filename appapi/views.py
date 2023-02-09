from rest_framework import generics, filters
from datetime import datetime, timedelta
from django.shortcuts import render, Http404
import random
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView
from rest_framework.response import Response
from jobs.models import JobSeeker, Applicant, FavouriteJob, Job
import boto3
from Address.models import State, City
from appapi.serializer import *
from user.permissions import AppOnlyUser, RequestHelper
# from rest_framework.decorators import api_view, permission_classes, authentication_classes
from user.views import get_tokens_for_user
from rest_framework_simplejwt.views import TokenViewBase


# For Refresh Token
class TokenRefreshView(TokenViewBase):
    """
        Renew tokens (access and refresh) with new expire time based on specific user's access token.
    """
    serializer_class = TokenRefreshLifetimeSerializer


# client = boto3.client("sns",
#                       aws_access_key_id="AKIA242PPGB5HRRGWBLT",
#                       aws_secret_access_key="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",
#                       region_name="ap-south-1"
#                       )
client = boto3.client("sns",
                      aws_access_key_id="AKIA242PPGB5KEAPBAVE",
                      aws_secret_access_key="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",
                      region_name="ap-south-1"
                      )


def get_otp():
    otp = ""
    pretime = str(datetime.now())
    for i in range(4):
        otp += str(random.randint(1, 9))
    return otp + "_" + pretime


class JobSeekerLogin(APIView):

    @staticmethod
    def post(request):
        phone = request.POST["mobile_number"]
        try:
            mobile_number = JobSeeker.objects.get(mobile_number=phone)
            user = "Old"
        except ObjectDoesNotExist:
            JobSeeker.objects.create(mobile_number=phone)
            mobile_number = JobSeeker.objects.get(mobile_number=phone)
            user = "New"
            mobile_number.save()

        otp_verify = get_otp()
        otp = otp_verify.split("_")
        otp = otp[0]
        mobile_number.otp = otp_verify
        client.publish(PhoneNumber="+91"+phone,Message="You OTP is " + otp)
        mobile_number.save()
        request.session['user'] = user
        return Response({"Message": "OTP Send", "Otp": otp}, status=200)


class JobSeekerLoginVerify(APIView):
    @staticmethod
    def post(request):
        user = request.session['user']
        phone = request.POST["mobile_number"]
        otp = request.POST["otp"]
        try:
            mobile_number = JobSeeker.objects.get(mobile_number=phone)
        except ObjectDoesNotExist:
            return Response({"Message": "Incorrect Mobile Number"}, status=404)

        verify_otp = mobile_number.otp.split("_")
        otp_time = verify_otp[0]
        period = datetime.strptime(
            verify_otp[1], '%Y-%m-%d %H:%M:%S.%f')

        if(datetime.now() - period) >= timedelta(minutes=5):
            return Response({"Message": "Otp Time Out try again"}, status=408)

        if otp == otp_time:
            tokens = get_tokens_for_user(mobile_number)
            JobSeeker.objects.filter(mobile_number=phone).update(otp='')
            return Response({"Message": "Login Successful", "UserType": "Jobseeker", "User": user, "Token": tokens}, status=200)

        else:
            return Response({"Message": "Wrong OTP"}, status=404)

class JobSeekerCreate(generics.UpdateAPIView):
    queryset = JobSeeker.objects.all()
    permission_classes = [AppOnlyUser]

    def get_object(self):
        user_id = RequestHelper.get_user_id_from_request(self.request)
        try:
            jobseeker = JobSeeker.objects.get(mobile_number=user_id)
            return jobseeker
        except JobSeeker.DoesNotExist:
            raise Http404

class JobSeekerUpdate(generics.UpdateAPIView):

    queryset = JobSeeker.objects.all()
    serializer_class = JobseekerProfileSerializer
    permission_classes = [AppOnlyUser]

    def get_object(self):
        user_id = RequestHelper.get_user_id_from_request(self.request)
        try:
            jobseeker = JobSeeker.objects.get(mobile_number=user_id)
        except JobSeeker.DoesNotExist:
            raise Http404

        self.request.data._mutable = True

        if "looking_for" in self.request.POST:
            looking_for = self.request.data.get("looking_for").split(',')
            for i in jobseeker.looking_for.values():
                jobseeker.looking_for.remove(i['id']) #removing the previous once

            if looking_for != ['']:
                for i in looking_for:
                    jobseeker.looking_for.add(JobType.objects.get(type=i))
            else:
                looking_for = []

        if "job_category" in self.request.POST:
            job_category = self.request.data.get("job_category").split(',')

            for i in jobseeker.job_category.values():
                jobseeker.job_category.remove(i['id']) #removing the previous once
            if job_category != ['']:
                for i in job_category:
                    jobseeker.job_category.add(
                        CompanyCategories.objects.filter(company_categories=i).first())
            else:
                job_category = []


        if "state" in self.request.POST:
            state = State.objects.filter(
                state=self.request.data.get("state")).first().id

            if "city" in self.request.POST:
                city = City.objects.filter(
                    city=self.request.data.get("city")).first().id
                self.request.data['city'] = city
            else:
                pass
            self.request.data['state'] = state

           


        return jobseeker


# @api_view(["PUT"])
# @permission_classes([AppOnlyUser])
class JobSeekerCreate(generics.UpdateAPIView):
    queryset = JobSeeker.objects.all()
    permission_classes = [AppOnlyUser]

    def get_object(self):
        user_id = RequestHelper.get_user_id_from_request(self.request)
        try:
            jobseeker = JobSeeker.objects.get(mobile_number=user_id)
            return jobseeker
        except JobSeeker.DoesNotExist:
            raise Http404

    def put(self, request):
        user_id = RequestHelper.get_user_id_from_request(self.request)
        mobile_number = request.data.get("mobile_number")
        if mobile_number == None:
            mobile_number = user_id

        name = request.data.get("full_name")
        email = request.data.get("email")
        gender = request.data.get("gender")
        dob = request.data.get("date_birth")
        state = request.data.get("state")
        city = request.data.get("city")

        # Change Date Formate
        try:
            dob = datetime.strptime(dob, '%d/%m/%Y').date()
            if (datetime.now().date() - dob).days < timedelta(days=6575).days:  # checking for 18+ age
                return Response({"Status": "403"}, status=403)
        except TypeError:
            dob = None

        try:
            JobSeeker.objects.get(mobile_number=user_id)
        except ObjectDoesNotExist:
            raise Http404

        JobSeeker.objects.filter(mobile_number=user_id).update(full_name=name, gender=gender,
                                                               state=state, city=city, email_id=email, date_birth=dob, mobile_number=mobile_number)

        return Response(request.data, status=200)


class StateList(generics.ListCreateAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer


class CityList(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer

    def get(self, request, state):
        query_state = State.objects.get(state=state)
        city = City.objects.filter(state=query_state)
        city_list = []
        for i in city:
            city_list.append(i.city)
        return Response(city_list)


class JobseekerProfile(generics.RetrieveAPIView):
    queryset = JobSeeker.objects.all()
    serializer_class = JobseekerProfileSerializer
    permission_classes = [AppOnlyUser]

    def get_object(self):
        user_id = RequestHelper.get_user_id_from_request(self.request)
        try:
            return JobSeeker.objects.get(mobile_number=user_id)
        except JobSeeker.DoesNotExist:
            raise Http404


class JobCategorie(generics.ListAPIView):
    queryset = CompanyCategories.objects.all().order_by('company_categories')
    serializer_class = JobCategoriesSerializer
    permission_classes = [AppOnlyUser]

    def get_object(self):
        user_id = RequestHelper.get_user_id_from_request(self.request)
        try:
            return JobSeeker.objects.get(mobile_number=user_id)
        except JobSeeker.DoesNotExist:
            raise Http404


class Joblist(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JoblistSerializer
    permission_classes = [AppOnlyUser]

    def get_object(self):
        user_id = RequestHelper.get_user_id_from_request(self.request)
        try:
            return JobSeeker.objects.get(mobile_number=user_id)
        except JobSeeker.DoesNotExist:
            raise Http404

    def get_queryset(self):
        categories = self.request.query_params.getlist('category')
        category = CompanyCategories.objects.filter(company_categories__in=categories)
        idlist = []
        for i in category:
            idlist.append(i.id)
        type = self.request.query_params.getlist('type')

        if category or type:
            if category and not type:
                return self.queryset.filter(job_catagories__in=idlist).order_by('-created_date')

            elif category and type:
                return self.queryset.filter(job_type__in=type, job_catagories__in=idlist).order_by('-created_date')

            else:
                return self.queryset.filter(job_type__in=type).order_by('-created_date')

        else:
            return Job.objects.all().order_by('-created_date')


class FavouriteJobCreateView(generics.CreateAPIView):
    queryset = FavouriteJob.objects.all()
    serializer_class = FavouriteJobSerializers
    permission_classes=[AppOnlyUser]

    def get_object(self):
        user_id = RequestHelper.get_user_id_from_request(self.request)
        try:
            jobseeker = JobSeeker.objects.get(mobile_number=user_id)
            return jobseeker
        except JobSeeker.DoesNotExist:
            raise Http404

    def post(self, request, job_id):
        user_id = RequestHelper.get_user_id_from_request(self.request)
        seeker = JobSeeker.objects.get(mobile_number=user_id)
        job = Job.objects.get(id=job_id)

        if FavouriteJob.objects.filter(job=job_id, jobseeker=seeker).exists():
            return Response({"Message": 'Duplicate'}, status=409)

        else:
            FavouriteJob.objects.create(job=job, jobseeker=seeker)
            return Response({"Message": 'Created'}, status=201)



class FavouriteJobDestroyView(generics.DestroyAPIView):
    queryset = FavouriteJob.objects.all()
    serializer_class = FavouriteJobSerializers
    permission_classes = [AppOnlyUser]

    def get_object(self):
        user_id = RequestHelper.get_user_id_from_request(self.request)
        try:
            jobseeker = JobSeeker.objects.get(mobile_number=user_id)
            return jobseeker
        except JobSeeker.DoesNotExist:
            raise Http404

    def delete(self, request, job_id):
        user_id = RequestHelper.get_user_id_from_request(self.request)
        seeker = JobSeeker.objects.get(mobile_number=user_id)
        FavouriteJob.objects.filter(job=job_id, jobseeker=seeker).delete()
        return Response({"Message": 'Deleted'}, status=202)


class FavouriteJobListView(generics.ListAPIView):
    queryset = FavouriteJob.objects.all()
    serializer_class = FavouriteJobListSerializers
    permission_classes=[AppOnlyUser]

    def get_object(self):
        user_id = RequestHelper.get_user_id_from_request(self.request)
        try:
            jobseeker = JobSeeker.objects.get(mobile_number=user_id)
            return jobseeker
        except JobSeeker.DoesNotExist:
            raise Http404

    def get_queryset(self):
        user_id = RequestHelper.get_user_id_from_request(self.request)
        seeker = JobSeeker.objects.get(mobile_number=user_id)
        return self.queryset.filter(jobseeker=seeker)


class ApplyJob(generics.CreateAPIView):
    queryset = Applicant.objects.all()
    serializer_class = ApplyJobSerializer
    permission_classes = [AppOnlyUser]

    def get_object(self):
        user_id = RequestHelper.get_user_id_from_request(self.request)
        try:
            return JobSeeker.objects.get(mobile_number=user_id)
        except JobSeeker.DoesNotExist:
            raise Http404

    def post(self, request, job_id):
        user_id = RequestHelper.get_user_id_from_request(self.request)
        seeker = JobSeeker.objects.get(mobile_number=user_id)
        job = Job.objects.get(id=job_id)

        if Applicant.objects.filter(job_catagories=job.job_catagories, job_Application_name=job, jobseeker_name=seeker).exists():
            return Response({"Message": 'Duplicate'}, status=409)

        else:
            Applicant.objects.create(job_catagories=job.job_catagories, employer=job.employer, job_Application_name=Job.objects.get(
                id=job.id), jobseeker_name=seeker, selection_status='Pending')
            return Response({"Message": 'Created'}, status=201)

class AppliyedJob(generics.ListAPIView):
    queryset = Applicant.objects.all()
    serializer_class = ApplyJobSerializer
    permission_classes = [AppOnlyUser]

    def get_object(self):
        user_id = RequestHelper.get_user_id_from_request(self.request)
        try:
            return JobSeeker.objects.get(mobile_number=user_id)
        except JobSeeker.DoesNotExist:
            raise Http404

    def get_queryset(self):
        user_id = RequestHelper.get_user_id_from_request(self.request)
        seeker = JobSeeker.objects.get(mobile_number=user_id)
        return Applicant.objects.filter(jobseeker_name=seeker).order_by('-created_date')

class JobSearchAPI(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSearchSerializer
    search_fields = ['job_title', 'employer__employer',
                     'job_type', 'state__state', 'city__city', 'job_designation']
    filter_backends = [filters.SearchFilter,]
    permission_classes = [AppOnlyUser]
