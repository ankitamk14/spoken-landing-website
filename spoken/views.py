from django.shortcuts import render, redirect
from django.conf import settings
# Create your views here.
from django.http import HttpResponse
from .models import Products, Nav, Blended_workshops, Jobfair, Internship, Testimonials, MediaTestimonials
from datetime import datetime
from django.utils import timezone
from .forms import ContactForm
from rest_framework.views import APIView
from .serializers import JobFairSerializer
from rest_framework.response import Response

today = datetime.today().strftime('%Y-%m-%d')

def home(request):
    if request.method == 'POST':
        c = ContactForm(request.POST)
        if c.is_valid():
            c.save()
            messages.add_message(request,messages.INFO,'Message submitted!')
            return redirect('/spoken#contact')
            #c = ContactForm()
    else:
        c = ContactForm()

    # return HttpResponse("Hello, world. You're at the spoken landing page.")
    navs = Nav.objects.filter(status=1)
    products = Products.objects.all()
    now = timezone.now()
    jobfairs = Jobfair.objects.filter(jobfair_date__gte=now).order_by('jobfair_date')[:3]
    internships = Internship.objects.filter(internship_date__gte=now).order_by('internship_date')[:2]
    workshops = Blended_workshops.objects.filter(workshop_date__gte=now).order_by('workshop_date')[:3]
    testimonials = Testimonials.objects.all()[:9]
    media_testimonials = MediaTestimonials.objects.all()[:3]
    context = {'jobfairs':jobfairs,'internships':internships,'workshops':workshops,'products':products, 
    'nav_list':navs, 'form':c, 'testimonials':testimonials,'media_testimonials':media_testimonials,'media_url' : settings.MEDIA_URL,}

    return render(request,'spoken/home.html',context)

def jobfairs(request):
    
    context = {}
    return render(request,'spoken/jobfairs.html',context)

#job_fairs/
class JobFairList(APIView):
    def get(self,request):
        jobfairs = Jobfair.objects.all()

        serializer = JobFairSerializer(jobfairs,many=True)
        return Response(serializer.data)


    def post(self):
        pass