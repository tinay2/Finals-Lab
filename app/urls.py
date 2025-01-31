from django.urls import path
from django.shortcuts import redirect
from django.contrib.auth.views import LogoutView
from .views import (
    HomePageView,
    AboutPageView, ContactPageView, ServicesPageView,
    AppointmentListView, 
    AppointmentDetailView, 
    AppointmentCreateView,
    AppointmentUpdateView,
    AppointmentDeleteView,
    CustomerProfileListView,
    CustomerProfileDetailView,
    CustomerProfileCreateView,
    CustomerProfileUpdateView,
    CustomerProfileDeleteView,
    ServiceListView,
    ServiceDetailView,
    ServiceCreateView,
    ServiceUpdateView,
    ServiceDeleteView,
    PaymentListView,
    PaymentDetailView,
    PaymentCreateView,
    PaymentUpdateView,
    PaymentDeleteView,
    CleanerAssignmentListView, 
    CleanerAssignmentDetailView, 
    CleanerAssignmentCreateView, 
    CleanerAssignmentUpdateView, 
    CleanerAssignmentDeleteView,
    SignupView,
    LoginPageView
)

urlpatterns = [
    # Redirect user to login page if not authenticated
    path('', lambda request: redirect('login') if not request.user.is_authenticated else redirect('home')),  # Only redirect to login if user is not logged in
    
    path('home/', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('services/info/', ServicesPageView.as_view(), name='services'),

    path('appointment/', AppointmentListView.as_view(), name='appointment'),
    path('appointment/<int:pk>/', AppointmentDetailView.as_view(), name='appointment_detail'),
    path('appointment/create/', AppointmentCreateView.as_view(), name='appointment_create'),
    path('appointment/update/<int:pk>/', AppointmentUpdateView.as_view(), name='appointment_update'),
    path('appointment/delete/<int:pk>/', AppointmentDeleteView.as_view(), name='appointment_delete'),

    path('customerprofile/', CustomerProfileListView.as_view(), name='customerprofile_list'),
    path('customerprofile/<int:pk>/', CustomerProfileDetailView.as_view(), name='customerprofile_detail'),
    path('customerprofile/create/', CustomerProfileCreateView.as_view(), name='customerprofile_create'),
    path('customerprofile/update/<int:pk>/', CustomerProfileUpdateView.as_view(), name='customerprofile_update'),
    path('customerprofile/delete/<int:pk>/', CustomerProfileDeleteView.as_view(), name='customerprofile_delete'),

    path('services/', ServiceListView.as_view(), name='service_list'),
    path('services/<int:pk>/', ServiceDetailView.as_view(), name='service_detail'),
    path('services/create/', ServiceCreateView.as_view(), name='service_create'),
    path('services/update/<int:pk>/', ServiceUpdateView.as_view(), name='service_update'),
    path('services/delete/<int:pk>/', ServiceDeleteView.as_view(), name='service_delete'),

    path('payments/', PaymentListView.as_view(), name='payment_list'),
    path('payments/<int:pk>/', PaymentDetailView.as_view(), name='payment_detail'),
    path('payments/create/', PaymentCreateView.as_view(), name='payment_create'),
    path('payments/update/<int:pk>/', PaymentUpdateView.as_view(), name='payment_update'),
    path('payments/delete/<int:pk>/', PaymentDeleteView.as_view(), name='payment_delete'),

    path('cleaner_assignments/', CleanerAssignmentListView.as_view(), name='cleaner_assignment_list'),
    path('cleaner_assignments/<int:pk>/', CleanerAssignmentDetailView.as_view(), name='cleaner_assignment_detail'),
    path('cleaner_assignments/create/', CleanerAssignmentCreateView.as_view(), name='cleaner_assignment_create'),
    path('cleaner_assignments/update/<int:pk>/', CleanerAssignmentUpdateView.as_view(), name='cleaner_assignment_update'),
    path('cleaner_assignments/delete/<int:pk>/', CleanerAssignmentDeleteView.as_view(), name='cleaner_assignment_delete'),

    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginPageView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
