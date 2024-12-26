from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
# Create your views here.
from django.http import HttpResponse, JsonResponse
service_data = [
        {
            "imagePath": "paintwaleapp/images/servicecard1.jpg",
            "cardTitle": "Decorative Paints",
            "description": "Enhance your home with our wide range of decorative paints designed for every style. Choose the perfect shade for your walls and give your home a new look."
        },
        {
            "imagePath": "paintwaleapp/images/servicecard2.jpg",
            "cardTitle": "Enamels",
            "description": "Our premium enamels offer long-lasting protection and a glossy finish for various surfaces. Ideal for metal, wood, and other materials."
        },
        {
            "imagePath": "paintwaleapp/images/servicecard3.jpg",
            "cardTitle": "Wall Putty",
            "description": "Smooth out rough surfaces with our wall putty. Ideal for repairing and filling cracks, ensuring a flawless finish for your walls."
        },
        {
            "imagePath": "paintwaleapp/images/servicecard4.jpg",
            "cardTitle": "Polyurethane Polish",
            "description": "Give your wooden furniture a premium finish with our polyurethane polish. It enhances the natural grain while providing protection against wear."
        },
        {
            "imagePath": "paintwaleapp/images/servicecard5.jpg",
            "cardTitle": "Waterproofing Chemicals",
            "description": "Protect your walls and surfaces from water damage with our waterproofing chemicals. Ideal for both residential and commercial use."
        },
        {
            "imagePath": "paintwaleapp/images/servicecard6.jpg",
            "cardTitle": "Doorstep Shade Selection",
            "description": "Select the perfect shade for your doorsteps with our expert guidance and high-quality paint options, ensuring durability and aesthetic appeal."
        }
    ]
service_type=[
    "Decorative Paints", 
    "Enamels", 
    "Wall Putty", 
    "Polyurethane Polish", 
    "Waterproofing Chemicals", 
    "Doorstep Shade Selection"
]

def index(request):
    return HttpResponse("Hello, world. You're at the paintwale index.")

def home(request):
    return render(request, 'paintwaleapp/home.html', {'service_data': service_data,'service_type':service_type})

def about(request):
    return render(request, 'paintwaleapp/about.html')
def service(request):

    return render(request, 'paintwaleapp/services.html', {'service_data': service_data})

def contact(request):
    service_title = request.GET.get('service', '') 
    return render(request, 'paintwaleapp/contact.html', {'service_title': service_title,'service_type':service_type})
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
                <p style="font-size: 12px; color: #777;">Powered by Your PaintWale</p>
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
                <p>Best regards,<br>Your PaintWale Team</p>
            </div>

            <div style="padding: 20px; background-color: #f0f0f0; border-top: 1px solid #ccc; text-align: right;">
                <p style="font-size: 12px; color: #777;">Powered by Your PaintWale</p>
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

        return JsonResponse({'success': 'Message sent successfully!'})

    except Exception as e:
        print(f"Error sending email: {e}")
        return JsonResponse({'error': f'Failed to send message. Error: {str(e)}'})