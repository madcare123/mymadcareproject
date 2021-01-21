from django.contrib import admin
from .models import Patient,Contact,Doctor,Appointment,Transaction

# Register your models here.
admin.site.register(Patient)
admin.site.register(Contact)
admin.site.register(Doctor)
admin.site.register(Appointment)
admin.site.register(Transaction)