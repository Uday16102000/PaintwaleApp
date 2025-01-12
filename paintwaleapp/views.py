from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
# Create your views here.
from django.http import HttpResponse, JsonResponse
from .constants import BRAND_NAME

from paintwaleapp.models import Service, ServiceImage
def getAllServiceType():
    service_type =Service.objects.values_list('service_name',flat=True)
    return service_type


def index(request):
    return HttpResponse("Hello, world. You're at the paintwale index.")

def home(request):

    services = Service.objects.all()
    service_type = getAllServiceType()
    context ={
        'brand_name': BRAND_NAME,
        'service_data': services,
        'service_type':service_type,
        'exclude_footer': True

    }

    return render(request, 'paintwaleapp/home.html', context)

def about(request):
    context ={
        'brand_name': BRAND_NAME,
        'exclude_footer': False

    }
    return render(request, 'paintwaleapp/about.html',context)
def service(request):
    services = Service.objects.all()


    return render(request, 'paintwaleapp/services.html', {'service_data': services})

def contact(request):
    service_title = request.GET.get('service', '') 
    service_type = getAllServiceType()
    context ={
        'brand_name': BRAND_NAME,
        'service_title': service_title,
        'service_type':service_type

    }

    return render(request, 'paintwaleapp/contact.html', context)
def sendMessage(request):

    name = request.POST.get('name', '') 
    email = request.POST.get('email', '')
    telephone = request.POST.get('telephone', '')
    subject = request.POST.get('subject', '')
    message = request.POST.get('message', '')

    print("Email sent successfully!", name)

    if not name or not email or not telephone or not message:
        return JsonResponse({'error': 'All fields except subject are required.'})
    
    email_subject_to_team = f"Message from {name} - {subject}"
    email_body_to_team = f"""
    <html>
        <body>
            <!-- Header with brand logo on the left -->
            <div style="padding: 20px; background-color: #f0f0f0; border-bottom: 1px solid #ccc;">
             <img src="https://images.app.goo.gl/GXNdHYpNUeL1cQ1e7" alt="Brand Logo" style="float: left; height: 50px;">                <h3 style="text-align: center; color: #333;">Contact Form Submission</h3>
            </div>
            
            <!-- Main message content -->
            <div style="padding: 20px;">
                <p><strong>Name:</strong> {name}</p>
                <p><strong>Email:</strong> {email}</p>
                <p><strong>Telephone:</strong> {telephone}</p>
                <p><strong>Message:</strong><br>{message}</p>
                <p><strong>Subject:</strong><br>{subject}</p>
            </div>

            <!-- Footer with text aligned to the right -->
            <div style="padding: 20px; background-color: #f0f0f0; border-top: 1px solid #ccc; text-align: right;">
                <p style="font-size: 12px; color: #777;">Powered by Your {BRAND_NAME}</p>
            </div>
        </body>
    </html>
    """

    email_subject_to_user = "We have received your request"
    email_body_to_user = f"""
    <html>
        <body>
            <div style="padding: 20px; background-color: #f0f0f0; border-bottom: 1px solid #ccc;">
                <img src="https://images.app.goo.gl/GXNdHYpNUeL1cQ1e7" alt="Brand Logo" style="float: left; height: 50px;">
                <h3 style="text-align: center; color: #333;">Thank you for contacting us</h3>
            </div>
            
            <div style="padding: 20px;">
                <p>Dear {name},</p>
                <p>Thank you for reaching out to us. We have received your message and our team will get back to you soon.</p>
                <p>Below are the details of your request:</p>
                <p><strong>Subject:</strong> {subject}</p>
                <p><strong>Message:</strong><br>{message}</p>
                <p>We appreciate your interest, and one of our team members will reach out shortly.</p>
                <p>Best regards,<br>Your {BRAND_NAME} Team</p>
            </div>

            <div style="padding: 20px; background-color: #f0f0f0; border-top: 1px solid #ccc; text-align: right;">
                <p style="font-size: 12px; color: #777;">Powered by Your {BRAND_NAME}</p>
            </div>
        </body>
    </html>
    """

    try:
        send_mail(
            email_subject_to_team,
            '', 
            email, 
            [settings.EMAIL_HOST_USER], 
            fail_silently=False,
            html_message=email_body_to_team,  
        )

        send_mail(
            email_subject_to_user,
            '', 
            settings.EMAIL_HOST_USER,  
            [email], 
            fail_silently=False,
            html_message=email_body_to_user,  
        )

        services = Service.objects.all()
        service_type = getAllServiceType()
        context ={
        'brand_name': BRAND_NAME,
        'service_data': services,
        'service_type':service_type,
        'exclude_footer': True

                  }

        return render(request, 'paintwaleapp/home.html', context)
    except Exception as e:
        print(f"Error sending email: {e}")
        return JsonResponse({'error': f'Failed to send message. Error: {str(e)}'})
    

from django.shortcuts import render, get_object_or_404
from .models import Service, ServiceImage

def serviceDetails(request):
    service_title = request.GET.get('service', '') 
    
    service_id = request.GET.get('serviceId', '')  
    
    error_message = None

    if not service_id or not service_id.isdigit():
        error_message = "Invalid or missing service ID."
        service_images = []
    else:
        try:
            service = get_object_or_404(Service, id=service_id)
            service_images = ServiceImage.objects.filter(service=service)
        except Service.DoesNotExist:
            error_message = "Service not found."
            service_images = []
    context ={
        'brand_name': BRAND_NAME,
        'service_detail': service_title,
        'service_images': service_images,
        'error_message': error_message 
    }

    return render(request, "paintwaleapp/service_details.html",context)
