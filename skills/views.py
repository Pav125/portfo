from django.shortcuts import render, redirect
from .models import Profile, Project, Skill
from .forms import ContactForm
from django.core.mail import send_mail
from django.contrib import messages
from django.core.mail import BadHeaderError
# Create your views here.

def profile_view(request):
    latest_profile = Profile.objects.latest('id')

    latest_projects = Project.objects.all()

    latest_skills = Skill.objects.all()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            em = 'from.portfolio@example.com'
            try:
                send_mail(
                    subject,
                    f"Name : {name}\nEmail : {email}\n\nMessage : {message}",
                    em, # sender
                    ['devipavan824@gmail.com', 'devipavan825@gmail.com'], # receiver
                    fail_silently=False,
                )
                messages.success(request, 'Your message was sent successfully.')
                return redirect('/')
            except BadHeaderError:
                messages.error(request, 'Invalid header found in email. Please try again.')
        else:
            messages.error(request, 'Form submission is invalid. Please correct the errors.')
    else:
        form = ContactForm()

    context = {
        'latest_profile' : latest_profile,
        'latest_projects' : latest_projects,
        'latest_skills' : latest_skills,
        'form' : form,
    }
    return render(request, 'skills/home.html', context)
