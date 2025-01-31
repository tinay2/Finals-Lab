from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class CustomerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    address = models.TextField()
    contact_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.user.username}'s Profile"


class Service(models.Model):
    SERVICE_TYPES = [
        ('STANDARD', 'Standard Cleaning'),
        ('DEEP', 'Deep Cleaning'),
        ('MOVE_IN_OUT', 'Move-in/Move-out Cleaning'),
        ('ADD_ON', 'Add-on Service'),]
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    service_type = models.CharField(max_length=20, choices=SERVICE_TYPES)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    customer = models.ForeignKey(CustomerProfile, on_delete=models.CASCADE, related_name="appointments")
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="appointments")
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=20,default="Scheduled")
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Appointment for {self.customer.user.username} on {self.date} at {self.time}"
    
        
    def get_absolute_url(self):
        return reverse('appointment_detail', args=[str(self.id)])


class Payment(models.Model):
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE, related_name="payment")
    payment_method = models.CharField(max_length=50)  # e.g., Credit Card, PayPal
    payment_status = models.CharField(max_length=20, default="Pending")
    payment_date = models.DateTimeField(auto_now_add=True)
    amount_paid =models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Payment for Appointment {self.appointment.id} - Status: {self.payment_status}"


class CleanerAssignment(models.Model):
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE, related_name="cleaner_assignment")
    cleaner_name = models.CharField(max_length=100)
    cleaner_contact = models.CharField(max_length=15)
    assigned_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cleaner {self.cleaner_name} assigned to Appointment {self.appointment.id}"
