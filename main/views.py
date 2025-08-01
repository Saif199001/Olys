from django.shortcuts import render
from django.contrib import messages
from .models import Contact
from django.shortcuts import redirect


# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def menu(request):
    return render(request, 'menu.html')

def frenchisee(request):
    franchise_benefits = [
        "Premium Equipment",
        "Uniforms & Training",
        "POS Software & Billing",
        "Social Media & Marketing",
        "1 Month Starter Stock",
        "Franchise Licensing",
    ]
    locations = [
        "High streets",
        "Malls",
        "College hubs",
        "Railway stations",
        "Highways",
        "Small towns"
    ]
    return render(request, 'frenchisee.html', {
        'franchise_benefits': franchise_benefits,
        'locations': locations,
    })

def gallery(request):
    return render(request, 'gallery.html')

def save_contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        mobile_no = request.POST.get("mobile_no")
        message = request.POST.get("message")

        if not name or not email:
            messages.error(request, "Name and email are required.")
            return redirect('contact')

        try:
            contact = Contact(name=name, email=email, mobile_no=mobile_no, message=message)
            contact.save()
            messages.success(request, "Thank you! Your query has been sent successfully! We will contact you soon")
        except Exception as e:
            messages.error(request, "Something went wrong. Please try again later.")

        return redirect('contact')
