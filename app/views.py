from django.shortcuts import render,redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Appointment
from .models import CustomerProfile, Service, Payment, CleanerAssignment
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import FormView
from django.shortcuts import render, redirect
from django.contrib.auth import login

    
    

class HomePageView(TemplateView):
    template_name = 'app/home.html'

class AboutPageView(TemplateView):
    template_name = 'app/about.html'

class ServicesPageView(TemplateView):
    template_name = 'app/services.html'


class ContactPageView(TemplateView):
    template_name = 'app/contact.html'


class AppointmentListView(ListView):
    model = Appointment
    context_object_name = 'appointment'
    template_name = 'app/appointment_list.html'

class AppointmentDetailView(DetailView):
    model = Appointment
    context_object_name = 'appointment'
    template_name = 'app/appointment_detail.html'

class AppointmentCreateView(CreateView):
    model = Appointment
    fields = ['customer','service', 'date', 'time', 'status', 'total_price']
    template_name = 'app/appointment_create.html'

class AppointmentUpdateView(UpdateView):
    model = Appointment
    fields = ['customer','service', 'date', 'time', 'status', 'total_price']
    template_name = 'app/appointment_update.html'
    success_url = reverse_lazy('appointment_list')

class AppointmentDeleteView(DeleteView):
    model = Appointment
    template_name = 'app/appointment_delete.html'
    success_url = reverse_lazy('appointment_list')

class CustomerProfileListView(ListView):
    model = CustomerProfile
    context_object_name = 'customerprofile'
    template_name = 'app/customerprofile_list.html'

class CustomerProfileDetailView(DetailView):
    model = CustomerProfile
    context_object_name = 'customerprofile'
    template_name = 'app/customerprofile_detail.html'


class CustomerProfileCreateView(CreateView):
    model = CustomerProfile
    fields = ['user', 'address', 'contact_number']
    template_name = 'app/customerprofile_create.html'
    success_url = reverse_lazy('customerprofile_list')


class CustomerProfileUpdateView(UpdateView):
    model = CustomerProfile
    fields = ['address', 'contact_number']
    template_name = 'app/customerprofile_update.html'
    success_url = reverse_lazy('customerprofile_list')


class CustomerProfileDeleteView(DeleteView):
    model = CustomerProfile
    template_name = 'app/customerprofile_delete.html'
    success_url = reverse_lazy('customerprofile_list') 

class ServiceListView(ListView):
    model = Service
    context_object_name = 'services'
    template_name = 'app/service_list.html'

class ServiceDetailView(DetailView):
    model = Service
    context_object_name = 'service'
    template_name = 'app/service_detail.html'

class ServiceCreateView(CreateView):
    model = Service
    fields = ['name', 'description', 'price', 'service_type']
    template_name = 'app/service_create.html'
    success_url = reverse_lazy('service_list')

class ServiceUpdateView(UpdateView):
    model = Service
    fields = ['name', 'description', 'price', 'service_type']
    template_name = 'app/service_update.html'
    success_url = reverse_lazy('service_list')

class ServiceDeleteView(DeleteView):
    model = Service
    template_name = 'app/service_delete.html'
    success_url = reverse_lazy('service_list')

class PaymentListView(ListView):
    model = Payment
    context_object_name = 'payments'
    template_name = 'app/payment_list.html'

class PaymentDetailView(DetailView):
    model = Payment
    context_object_name = 'payment'
    template_name = 'app/payment_detail.html'


def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    payment = self.get_object()
    context['service'] = payment.service  # Ensure the related service is added to context
    return context

class PaymentCreateView(CreateView):
    model = Payment
    fields = ['appointment', 'payment_method', 'payment_status', 'amount_paid']
    template_name = 'app/payment_create.html'
    success_url = reverse_lazy('payment_list')

class PaymentUpdateView(UpdateView):
    model = Payment
    fields = ['payment_method', 'payment_status', 'amount_paid']
    template_name = 'app/payment_update.html'
    success_url = reverse_lazy('payment_list')

class PaymentDeleteView(DeleteView):
    model = Payment
    template_name = 'app/payment_delete.html'
    success_url = reverse_lazy('payment_list')

class CleanerAssignmentListView(ListView):
    model = CleanerAssignment
    context_object_name = 'cleaner_assignments'
    template_name = 'app/cleaner_assignment_list.html'

class CleanerAssignmentDetailView(DetailView):
    model = CleanerAssignment
    context_object_name = 'cleaner_assignment'
    template_name = 'app/cleaner_assignment_detail.html'

class CleanerAssignmentCreateView(CreateView):
    model = CleanerAssignment
    fields = ['appointment', 'cleaner_name', 'cleaner_contact']
    template_name = 'app/cleaner_assignment_create.html'
    success_url = reverse_lazy('cleaner_assignment_list')

class CleanerAssignmentUpdateView(UpdateView):
    model = CleanerAssignment
    fields = ['appointment', 'cleaner_name', 'cleaner_contact']
    template_name = 'app/cleaner_assignment_update.html'
    success_url = reverse_lazy('cleaner_assignment_list')

class CleanerAssignmentDeleteView(DeleteView):
    model = CleanerAssignment
    template_name = 'app/cleaner_assignment_delete.html'
    success_url = reverse_lazy('cleaner_assignment_list')

class SignupView(FormView):
    template_name = 'register/signup.html'
    form_class = UserCreationForm

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)  # Log the user in after signup
        return redirect('login') 

class LoginPageView(FormView):
    template_name = 'register/login.html'
    form_class = AuthenticationForm  # Use AuthenticationForm for login

    def form_valid(self, form):
        # Handle form submission: authenticate the user and log them in
        user = form.get_user()  # Get the authenticated user
        login(self.request, user)  # Log the user in
        return redirect('home')  # Redirect to home or desired page after successful login

