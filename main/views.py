from django.shortcuts import render, redirect
from .models import Service, Testimonial
from .forms import ContactForm, TestimonialForm
from blog.models import BlogPost



def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def services(request):
    services = Service.objects.all()
    return render(request, 'main/services.html', {'services': services})

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')  # Ensure this matches your urls.py name
    else:
        form = ContactForm()
    return render(request, 'main/contact.html', {'form': form})

def thank_you_view(request):
    return render(request, 'main/thank_you.html')

def testimonial_view(request):
    if request.method == 'POST':
        form = TestimonialForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'main/testimonial_thanks.html')  # Create this template
    else:
        form = TestimonialForm()

    testimonials = Testimonial.objects.filter(is_approved=True).order_by('-created_at')
    return render(request, 'main/testimonials.html', {'form': form, 'testimonials': testimonials})

def home(request):
    posts = BlogPost.objects.order_by('-created_at')[:3]  
    return render(request, 'main/home.html', {'posts': posts})

