from django.urls import path, include
from ifheplapp import views, cards
import jobApplications.views as jobApplication
import vendorApplication.views as vendor
from ifheplapp.api import AttendanceView, EmployeeRegistrationView, SliderList, UserLoginView, UserProfileView


urlpatterns = [
    path('', views.index, name="index"),
    path('ads.txt', views.ads, name="ads.txt"),
    
    ##Card Generate Function
    path('membership_card_generate', cards.membership_card_generate, name="membership_card_generate"),
    path('health_card_generate', cards.health_card_generate, name="health_card_generate"),
    path('kisan_card_generate', cards.kisan_card_generate, name="kisan_card_generate"),
    # headers and footer
    path('associate-partner', views.associate, name="associate_partner"),
    path('comingsoon', views.comingsoon, name="comingsoon"),
    path('privacy-policy', views.privacypolicy, name="privacypolicy"),
    path('reach-us', views.reachus, name="reachus"),
    path('reachus_submit', views.reachus_submit, name="reachus_submit"),
    path('terms-and-condition', views.termscondition, name="termscondition"),
    path('cookie-policy', views.cookiepolicy, name="cookiepolicy"),
    path('refund-cancellation-policy', views.returnpolicy, name="returnpolicy"),
    path('about-us', views.aboutus, name="aboutus"),
    path('gallery', views.gallery, name="gallery"),
    path('pricing', views.pricing, name="pricing"),
    # health
    path('card/Health-Card', views.health_card, name="health_card"),
    path('card/Health-Card/apply', views.health_card_apply, name="health_card_apply"),
    path('card/Health-Card/Confirmation', views.health_submit, name="health_submit"),
    path('verify-health', views.searchHealth, name="verify_health"),
    path('verify-health/viewDetails', views.viewHealthCard, name="viewHealthCard"),
    # membership
    path('membership', views.membership, name="membership"),
    path('membership/Confirmation', views.membership_submit, name="membership_submit"),
    path('verify-membership', views.searchMembership, name="verify_membership"),
    path('verify-membership/viewDetails', views.viewMembership, name="viewMembership"),
    # kisan
    path('card/Kisan-Card/Confirmation', views.kisan_submit, name="kisan_submit"), 
    path('card/Kisan-Card', views.kisan_card, name="kisan_card"),
    path('card/Kisan-Card/apply', views.kisan_card_apply, name="kisan_card_apply"),
    path('verify-kisan', views.searchKisan, name="verify_kisan"),
    path('verify-kisan/viewDetails', views.viewKisanCard, name="viewKisanCard"),
    # vendor
    path('vendor-registration', views.vendor, name="vendor_registration"),
    path('vendor-registration/Confirmation', vendor.vendor_submit, name="vendor_submit"),
    path('verify-vendor', views.searchVendor, name="verify_vendor"),
    path('verify-vendor/viewDetails', views.viewVendor, name="viewVendor"),
    # career and employee
    path('career', views.career, name="career"),
    path('career/<str:slug>/apply', views.careerApply, name="careerApply"),
    path('job_submit', jobApplication.job_submit, name="job_submit"),
    path('print/<str:order_id>', views.print, name="print"),
    path('profile', views.profile, name="profile"),
    path('complete_profile', jobApplication.complete_profile, name="complete_profile"),
    path('login', views.login, name="login"),
    path('attendance', views.attendance, name="attendance"),
    path('handleAttendance', views.handleAttendance, name="handleAttendance"),
    path('logout', views.handelLogout, name="logout"),
    path('handeLogin', views.handeLogin, name="handeLogin"),
    path('offer_letter', views.offer_letter, name="offer_letter"),

    # notice
    path('notice/rules_regulation', views.rules_regulation, name="rules_regulation"),
    path('notice/academic_notice', views.academic_notice, name="academic_notice"),
    path('notice/administrative_notice', views.administrative_notice,
         name="administrative_notice"),
    path('notice/requirement_notice', views.requirement_notice, name="requirement_notice"),
    #API's
    path('api/EmployeeRegistration', EmployeeRegistrationView.as_view(), name="signup"),
    path('api/signin', UserLoginView.as_view(), name="signin"),
    path('api/profile', UserProfileView.as_view(), name="profile"),
    path('api/attendance', AttendanceView.as_view(), name="attendance"),
    path('api/slider', SliderList.as_view(), name="slider"),
    # payment
    path('pay/<str:order_id>', views.initiate_payment, name='pay'),
    path('success/', views.callback, name='callback'),
]
