from django.urls import path, include
from ifheplapp import views, cards
from ifheplapp.api import AttendanceView, EmployeeRegistrationView, SliderList, UserLoginView, UserProfileView


urlpatterns = [
    path('', views.maintainance, name="maintainance"),
    path('ads.txt', views.ads, name="ads.txt"),
]
