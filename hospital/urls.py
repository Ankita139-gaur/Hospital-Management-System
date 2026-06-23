from django.urls import path
from . import views

urlpatterns = [

    path('dashboard/',
         views.dashboard,
         name='dashboard'),

    path('add-doctor/',
         views.add_doctor,
         name='add_doctor'),

    path('doctors/',
         views.doctor_list,
         name='doctor_list'),

    path('add-patient/',
         views.add_patient,
         name='add_patient'),

    path('patients/',
         views.patient_list,
         name='patient_list'),

    path('book-appointment/',
         views.book_appointment,
         name='book_appointment'),

     path('delete-patient/',
         views.delete_patient,
         name='delete_patient'),
]