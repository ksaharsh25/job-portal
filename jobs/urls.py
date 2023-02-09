from django.contrib import admin  
from django.urls import path
from jobs import views
from django.conf.urls import url
 
urlpatterns = [  
    # path('admin/', admin.site.urls),  
    # path('signup', views.signup, name='signup'),
    # path('activate/<uidb64>/<token>', views.activate, name='activate'),
    # path('signin', views.signin, name='signin'),
    path('logout', views.logout, name='logout'),
    path('login', views.login, name="login"),
    path('otp', views.otp , name="otp"),
]
