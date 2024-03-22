from django.urls import path
from . import views
from .views import submit_contact_form

urlpatterns = [
    
    path('',views.index,name='home'),
    path('about/',views.about,name='about'),
    path('booking/',views.booking,name='booking'),
    path('doctors/',views.doctors,name='doctors'),
    path('contact/',views.contact,name='contact'),
    path('department/',views.department,name='department'),
    path('contact/submit_contact_form/', submit_contact_form, name='submit_contact_form'),

]
