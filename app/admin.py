from django.contrib import admin
from .models import CustomerProfile, Service, Appointment, Payment, CleanerAssignment

admin.site.register(CustomerProfile)
admin.site.register(Service)
admin.site.register(Appointment)
admin.site.register(Payment)
admin.site.register(CleanerAssignment)
