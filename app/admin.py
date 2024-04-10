from django.contrib import admin
from .models import Doctor,Patient,Appointment,PatientDischargeDetails,contact
# Register your models here.
class conactadmin(admin.ModelAdmin):
    list_display=('name','surname','phone','email','msg')
admin.site.register(contact,conactadmin)


class DoctorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Doctor, DoctorAdmin)

class PatientAdmin(admin.ModelAdmin):
    pass
admin.site.register(Patient, PatientAdmin)

class AppointmentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Appointment, AppointmentAdmin)

class PatientDischargeDetailsAdmin(admin.ModelAdmin):
    pass
admin.site.register(PatientDischargeDetails, PatientDischargeDetailsAdmin)
