from django.urls import path, include
from ifheplapp import views
from ifheplapp.api import AttendanceView, EmployeeRegistrationView, UserLoginView, UserProfileView


urlpatterns = [
    path('', views.index, name="index"),
    path('membership', views.membership, name="membership"),
    path('qr_generator_fuc', views.qr_generator_fuc, name="qr_generator_fuc"),
    path('card_generator_fuc', views.card_generator_fuc, name="card_generator_fuc"),
    path('login', views.login, name="login"),
    path('attendance', views.attendance, name="attendance"),
    path('handleAttendance', views.handleAttendance, name="handleAttendance"),
    path('logout', views.handelLogout, name="logout"),
    path('handeLogin', views.handeLogin, name="handeLogin"),
    path('membership/Confirmation', views.membership_submit, name="membership_submit"),
    path('card/Kisan-Card', views.kisan_card, name="kisan_card"),
    path('card/Kisan-Card/apply', views.kisan_card_apply, name="kisan_card_apply"),
    path('card/Kisan-Card/Confirmation', views.kisan_submit, name="kisan_submit"), 
    path('card/Health-Card', views.health_card, name="health_card"),
    path('card/Health-Card/apply', views.health_card_apply, name="health_card_apply"),
    path('card/Health-Card/Confirmation', views.health_submit, name="health_submit"),
    path('privacy-policy', views.privacypolicy, name="privacypolicy"),
    path('reach-us', views.reachus, name="reachus"),
    path('reachus_submit', views.reachus_submit, name="reachus_submit"),
    path('terms-and-condition', views.termscondition, name="termscondition"),
    path('cookie-policy', views.cookiepolicy, name="cookiepolicy"),
    path('about-us', views.aboutus, name="aboutus"),
    path('gallery', views.gallery, name="gallery"),
    path('search_membership', views.searchMembership, name="search_membership"),
    path('search_membership/viewDetails',
         views.viewMembership, name="viewMembership"),
    path('comingsoon', views.comingsoon, name="comingsoon"),
    path('career', views.career, name="career"),
    path('career/<str:slug>/apply', views.careerApply, name="careerApply"),
    path('job_submit', views.job_submit, name="job_submit"),
    path('notice/rules_regulation', views.rules_regulation, name="rules_regulation"),
    path('notice/academic_notice', views.academic_notice, name="academic_notice"),
    path('notice/administrative_notice', views.administrative_notice,
         name="administrative_notice"),
    path('notice/requirement_notice', views.requirement_notice, name="requirement_notice"),
    path('offer_letter', views.offer_letter, name="offer_letter"),
    #API's
    path('api/EmployeeRegistration', EmployeeRegistrationView.as_view(), name="signup"),
    path('api/signin', UserLoginView.as_view(), name="signin"),
    path('api/profile', UserProfileView.as_view(), name="profile"),
    path('api/attendance', AttendanceView.as_view(), name="attendance"),
]
