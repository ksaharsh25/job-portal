from unicodedata import name
from django.urls import path, include
from user.views import *
from . import views
from django.conf.urls import url

# from .views import GenerateOTP, ValidateOTP

urlpatterns = [
    path('', views.index, name='home'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('changepassword/', UserChangePasswordView.as_view(), name='changepassword'),
    path('send-reset-password-email/', SendPasswordResetEmailView.as_view(),
         name='send-reset-password-email'),
    path('reset-password/<uid>/<token>/',
         UserPasswordResetView.as_view(), name='reset-password'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('verify/<phone>/', getPhoneNumberRegistered_TimeBased.as_view(), name='phoneOtp')
    
#     url(r'^generate/$', GenerateOTP.as_view(), name="generate"),
#     url(r'^validate/$', ValidateOTP.as_view(), name="validate"),

]