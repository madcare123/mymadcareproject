
from django.urls import path
from .import views
urlpatterns = [
    path('',views.index,name='index'),
    path('doctor_index/',views.doctor_index,name='doctor_index'),
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('about/',views.about,name='about'),
    path('services/',views.services,name='services'),
    path('contact/',views.contact,name='contact'),
    path('team/',views.team,name='team'),
    path('logout/',views.logout,name='logout'),
    path('forgot_password/',views.forgot_password,name='forgot_password'),
    path('verify_otp/',views.verify_otp,name='verify_otp'),
    path('update_password/',views.update_password,name='update_password'),
    path('change_password/',views.change_password,name='change_password'),
    path('doctor_profile/',views.doctor_profile,name='doctor_profile'),
    path('doctor_detail/<int:pk>/',views.doctor_detail,name='doctor_detail'),
    path('book_appointment/<int:pk>/',views.book_appointment,name='book_appointment'),
    path('view_appointment/',views.view_appointment,name='view_appointment'),
    path('complete_appointment/<int:pk>/',views.complete_appointment,name='complete_appointment'),
    path('pay/',views.initiate_payment, name='pay'),
    path('callback/',views.callback, name='callback'),
    path('my_appointments/',views.my_appointments,name='my_appointments'),
]
