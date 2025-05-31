from django.urls import path
from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact_view, name='contact'),  # updated here
    path('services/', views.services, name='services'),
      path('thank-you/', views.thank_you_view, name='thank_you'),
       path('testimonials/', views.testimonial_view, name='testimonials'),
        path('blog/', include('blog.urls')),
]
