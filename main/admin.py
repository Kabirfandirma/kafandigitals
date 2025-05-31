from django.contrib import admin
from .models import ContactMessage, Service

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject',)
    search_fields = ('name', 'email', 'subject')

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title', 'description')

admin.site.register(ContactMessage, ContactMessageAdmin)
admin.site.register(Service, ServiceAdmin)

from django.contrib import admin
from .models import Testimonial

class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'is_approved')
    list_filter = ('is_approved',)
    search_fields = ('name', 'message')

admin.site.register(Testimonial, TestimonialAdmin)
