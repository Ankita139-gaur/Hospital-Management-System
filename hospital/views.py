from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def dashboard(request):

    doctor_count = Doctor.objects.count()

    patient_count = Patient.objects.count()

    appointment_count = Appointment.objects.count()

    context = {

        'doctor_count':doctor_count,

        'patient_count':patient_count,

        'appointment_count':appointment_count

    }

    return render(
        request,
        'dashboard.html',
        context
    )

def book_appointment(request):

    doctors = Doctor.objects.all()
    patients = Patient.objects.all()

    if request.method == "POST":

        Appointment.objects.create(
            patient_id=request.POST['patient'],
            doctor_id=request.POST['doctor'],
            date=request.POST['date'],
            time=request.POST['time']
        )
        return redirect('dashboard')

    return render(
        request,
        'appointment.html',
        {
            'doctors': doctors,
            'patients': patients
        }
    )
def add_doctor(request):

    if request.method == "POST":

        name = request.POST['name']
        specialization = request.POST['specialization']
        phone = request.POST['phone']
        if not name or not specialization or not phone:
            return render(request,'add_doctor.html',{'error':'All fields are required'})
        Doctor.objects.create(
            name=name,
            specialization=specialization,
            phone=phone
        )

        return redirect('doctor_list')

    return render(request,'add_doctor.html')
def doctor_list(request):

    doctors = Doctor.objects.all()

    return render(
        request,
        'doctor_list.html',
        {'doctors':doctors}
    )
def add_patient(request):

    if request.method == "POST":

        name = request.POST['name']
        age = request.POST['age']
        phone = request.POST['phone']
        if not name or not age or not phone:
            return render(request,'add_patient.html',{'error':'All fields are required'})

        Patient.objects.create(
            name=name,
            age=age,
            phone=phone
        )

        return redirect('patient_list')

    return render(request,'add_patient.html')
def patient_list(request):

    patients = Patient.objects.all()

    return render(
        request,
        'patient_list.html',
        {'patients':patients}
    )
def delete_patient(request,id):

    patient=Patient.objects.get(id=id)

    patient.delete()

    return redirect('patient_list')
