from rest_framework import serializers
from Address.models import State, City
from rest_framework_simplejwt.tokens import RefreshToken
from jobs.models import JobSeeker, CompanyCategories, Job, Employer, Applicant, FavouriteJob
from rest_framework_simplejwt.serializers import (
    TokenRefreshSerializer
)

from jobs.models import JobSeeker, CompanyCategories, JobType


class TokenRefreshLifetimeSerializer(TokenRefreshSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = RefreshToken(attrs['refresh'])
        data['RefreshTokenExpTime'] = (int(refresh.payload['exp'])*1000)
        data['AccessTokenExpTime'] = (
            int(refresh.access_token.payload['exp'])*1000)
        return data


class JobseekerProfileSerializer(serializers.ModelSerializer):
    state = serializers.SerializerMethodField()
    city = serializers.SerializerMethodField()
    looking_for = serializers.SerializerMethodField()
    job_category = serializers.SerializerMethodField()

    class Meta:
        model = JobSeeker
        fields = ['full_name', 'date_birth',
                  'job_category', 'gender', 'mobile_number', 'email_id', 'state', 'city', 'looking_for', 'about_me', 'working_experience', 'address', 'education', 'profile_image', 'my_file']

    def get_state(self, obj):
        if obj.state != None:
            return State.objects.get(id=obj.state.id).state
        else:
            return None

    def get_city(self, obj):
        if obj.city != None:
            return City.objects.get(id=obj.city.id).city
        else:
            return None

    def get_looking_for(self, obj):
        job_list = []

        for i in obj.looking_for.values():
            job_list.append(i['type'])
        return job_list

    def get_job_category(self, obj):

        category_list = []
        for i in obj.job_category.values():
            category_list.append(i['company_categories'])
        return category_list

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ['state']


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['city', 'state']


class JobCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyCategories
        fields = ['company_categories', 'categories_image']

class JoblistSerializer(serializers.ModelSerializer):
    state = serializers.SerializerMethodField()
    city = serializers.SerializerMethodField()
    employer = serializers.SerializerMethodField()

    class Meta:
        model = Job
        fields = ['id','job_title', 'job_catagories', 'job_type', 'employer',
                  'company_profile_image', 'job_end_date', 'created_date', 'state', 'city', 'description',
                  'Number_vacancy', 'salary_max', 'salary_min', 'about_company']

    def get_state(self, obj):
        if obj.state != None:
            return State.objects.get(id=obj.state.id).state
        else:
            return None

    def get_city(self, obj):
        if obj.city != None:
            return City.objects.get(id=obj.city.id).city
        else:
            return None

    def get_employer(self, obj):
        return Employer.objects.get(id=obj.employer.id).employer


class ApplyJobSerializer(serializers.ModelSerializer):
    job_catagories = serializers.SerializerMethodField()
    employer = serializers.SerializerMethodField()
    job_title = serializers.SerializerMethodField()

    class Meta:
        model = Applicant
        fields = ['job_Application_name', 'job_title', 'selection_status', 'job_catagories',
                  'employer', 'created_date', 'updated_date']

    def get_job_catagories(self, obj):
        return CompanyCategories.objects.get(id=obj.job_catagories.id).company_categories

    def get_employer(self, obj):
        return Employer.objects.get(id=obj.employer.id).employer

    def get_job_title(self, obj):
        return Job.objects.get(id=obj.job_Application_name.id).job_title


class FavouriteJobSerializers(serializers.ModelSerializer):

    class Meta:
        model = FavouriteJob
        fields = '__all__'


class FavouriteJobListSerializers(serializers.ModelSerializer):
    job = serializers.SerializerMethodField()
    job_id = serializers.SerializerMethodField()

    class Meta:
        model = FavouriteJob
        fields = ['id', 'job_id', 'job']

    def get_job_id(self, obj):
        return Job.objects.get(id=obj.job.id).id

    def get_job(self, obj):
        return Job.objects.get(id=obj.job.id).job_title


class JobSearchSerializer(serializers.ModelSerializer):

    job_catagories = serializers.SerializerMethodField()
    state = serializers.SerializerMethodField()
    city = serializers.SerializerMethodField()
    employer = serializers.SerializerMethodField()

    class Meta:
        model = Job
        fields = ['id', 'job_title', 'job_catagories', 'job_type', 'employer',
                  'company_profile_image', 'job_end_date', 'created_date', 'state', 'city', 'description',
                  'Number_vacancy', 'salary_max', 'salary_min', 'about_company', 'job_designation']

    def get_state(self, obj):
        if obj.state != None:
            return State.objects.get(id=obj.state.id).state
        else:
            return None

    def get_city(self, obj):
        if obj.city != None:
            return City.objects.get(id=obj.city.id).city
        else:
            return None

    def get_job_catagories(self, obj):
        if obj.job_catagories != None:
            return CompanyCategories.objects.get(id=obj.job_catagories.id).company_categories
        else:
            return None

    def get_employer(self, obj):
        if obj.employer != None:
            return Employer.objects.get(id=obj.employer.id).employer
        else:
            return None
