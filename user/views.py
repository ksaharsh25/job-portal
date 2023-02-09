from urllib import request, response
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from user.permissions import AppOnlyUser
from user.serializer import *
from django.contrib.auth import authenticate
from user.renderers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime
import base64
from jobs.models import JobSeeker
# from . models import phoneModel
import pyotp

from django.conf import settings
from django.contrib.auth import authenticate, login
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

# from .models import PhoneToken
# from .serializer import (PhoneTokenCreateSerializer, PhoneTokenValidateSerializer )
# from .utils import user_detail

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

# Generate Token Manually
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return{
        'refresh': str(refresh),
        'access': str(refresh.access_token),
        'RefreshTokenExpTime': (int(refresh.payload['exp'])*1000),
        'AccessTokenExpTime': (int(refresh.access_token.payload['exp'])*1000)
    }


class UserRegistrationView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, format=None):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            token = get_tokens_for_user(user)
            return Response({'token': token, 'msg': 'Registration Successful'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                token = get_tokens_for_user(user)
                return Response({'token': token, 'msg': 'Login Success'}, status=status.HTTP_200_OK)
            else:
                return Response({'errors': {'non_field_errors': ['Email or Password is not Valid']}}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserProfileView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserChangePasswordView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = UserChangePasswordSerializer(
            data=request.data, context={'user': request.user})
        if serializer.is_valid(raise_exception=True):
            return Response({'msg': 'Password Changed Successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SendPasswordResetEmailView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, format=None):
        serializer = SendPasswordResetEmailSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response({'msg': 'Password Reset link send. Please check your Email'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserPasswordResetView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, uid, token, format=None):
        serializer = UserPasswordResetSerializer(
            data=request.data, context={'uid': uid, 'token': token})
        if serializer.is_valid(raise_exception=True):
            return Response({'msg': 'Password Reset Successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLogoutView(APIView):
    renderer_classes = [UserRenderer]

    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response('User Logged out successfully')


from datetime import datetime
import base64

def get_key(phone):
    mystr = "aaeb8363976c04d3d757468feadef95c" + phone
    return base64.b32encode(mystr.encode())

EXPIRY_TIME = 60  # seconds


class getPhoneNumberRegistered_TimeBased(APIView):
    # Get to Create a call for OTP
    @staticmethod
    def get(request, phone):
        OTP_SECRET_KEY = get_key(phone)
        try:
            # if Mobile already exists the take this else create New One
            Mobile = JobSeeker.objects.get(mobile_number=phone)
        except ObjectDoesNotExist:
            JobSeeker.objects.create(
                mobile_number=phone,
            )
            Mobile = JobSeeker.objects.get(
                mobile_number=phone)  # user Newly created Model
        Mobile.save()  # Save the data
        OTP = pyotp.TOTP(OTP_SECRET_KEY,
                         5, interval=EXPIRY_TIME, name=Mobile)
        # Using Multi-Threading send the OTP Using Messaging Services like Twilio or Fast2sms
        # Just for demonstration
        return Response({"OTP": OTP.now()}, status=200)

    # This Method verifies the OTP
    @staticmethod
    def post(request, phone):
        OTP_SECRET_KEY = get_key(phone)
        try:
            Mobile = JobSeeker.objects.get(mobile_number=phone)
        except ObjectDoesNotExist:
            return Response("User does not exist", status=404)  # False Call

        OTP = pyotp.TOTP(OTP_SECRET_KEY,
                         5, interval=EXPIRY_TIME, name=Mobile)  # TOTP Model
        tokens = get_tokens_for_user(Mobile)
        
        if OTP.verify(request.data["OTP"]):  # Verifying the OTP
            Mobile.is_phone_verified = True
            Mobile.save()
            return Response({'tokens': tokens}, status=200)
        return Response("OTP is wrong/expired", status=400)
    



