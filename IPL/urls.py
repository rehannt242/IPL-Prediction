"""IPL URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from IPLApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.CommonHome,name='CommonHome'),
    path('SignIn/',views.SignIn,name='Sign In'),
    path('ClubSignUp/',views.ClubRegistration,name='ClubRegistration'),
    path('SignUp/',views.CustomerRegistration,name='Sign Up'),
    
    
    
    path('AdminHome/',views.AdminHome,name='Admin Home'),
    path('ClubHome/',views.ClubHome,name='Club Home'),
    path('CustomerHome/',views.CustomerHome,name='Customer Home'),
    
    
    
    path('AdminAddFixtures/',views.AdminAddFixtures,name='AdminAddFixtures'),
    path('AdminViewCustomers/',views.AdminViewCustomers,name='Admin View Customers'),
    path('AdminViewClub/',views.AdminViewClub,name='Admin View Club'),
    
    
    
    path('ClubAddPlayer/',views.ClubAddPlayer,name='ClubAddPlayer'),
    path('ClubAddNewsUpdates/',views.ClubAddNewsUpdates,name='ClubAddNewsUpdates'),
    path('ClubViewFixtures/',views.ClubViewFixtures,name='ClubViewFixtures'),
    path('ClubViewFeedback/',views.ClubViewFeedback,name='ClubViewFeedback'),
    path('ClubViewcomplaints/',views.ClubViewcomplaints,name='ClubViewcomplaints'),    
    
    
    
    path('CustomerViewFixtures/',views.CustomerViewFixtures,name='CustomerViewFixtures'),
    path('CustomerViewClubDetails/',views.CustomerViewClubDetails,name='CustomerViewClubDetails'),
    path('CustomerAddFeedback/',views.CustomerAddFeedback,name='CustomerAddFeedback'),
    path('CustomerAddComplaints/',views.CustomerAddComplaints,name='CustomerAddComplaints'),
    path('CustomerViewNewsUpdates/',views.CustomerViewNewsUpdates,name='CustomerViewNewsUpdates'),
    path('CustomerViewMoreNewsUpdates/',views.CustomerViewMoreNewsUpdates,name='CustomerViewMoreNewsUpdates'),
    path('CustomerViewTeamSquad/',views.CustomerViewTeamSquad,name='CustomerViewTeamSquad'),
    path('CustomerViewPlayers/',views.CustomerViewPlayers,name='CustomerViewPlayers'),
    path('CustomerViewPlayerDetails/',views.CustomerViewPlayerDetails,name='CustomerViewPlayerDetails'),

    path('predict_result/',views.predict_result,name='predict_result'),
    path('score/',views.score,name='score prediction'),
]
