from django.urls import path
from .views import *
urlpatterns = [
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("jobseeker/login/", JobSeekerLogin.as_view(), name="jobseeker"),
    path("jobseeker/login/verify",
         JobSeekerLoginVerify.as_view(), name="jobseeker_verify"),
    path("jobseeker/create", JobSeekerCreate.as_view(), name="jobseeker_create"),
    path("state/", StateList.as_view(), name="jobseeker_state"),
    path("city/<state>/", CityList.as_view(), name="jobseeker_city"),
    path("jobseeker/details", JobseekerProfile.as_view(), name="jobseeker_deatils"),
    path("jobseeker/update", JobSeekerUpdate.as_view(), name="jobseeker_update"),
    path("categories", JobCategorie.as_view(), name="job_catregories"),
    path("joblist", Joblist.as_view(), name="joblisting"),
    path("applyjob/<job_id>", ApplyJob.as_view(), name="applyjob"),
    path("applyjob/", AppliyedJob.as_view(), name="AppliedJob"),
    path("favourite", FavouriteJobListView.as_view(), name="favourites"),
    path("favourite/create/<job_id>", FavouriteJobCreateView.as_view(), name="favouritesCreate"),
    path("favourite/delete/<job_id>", FavouriteJobDestroyView.as_view(), name="favouritesDestroy"),
    path('job', JobSearchAPI.as_view(), name="search"),

]
