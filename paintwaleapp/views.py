from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
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

def index(request):
    return HttpResponse("Hello, world. You're at the paintwale index.")

def home(request):
    return render(request, 'paintwaleapp/home.html', {'service_data': service_data})

def about(request):
    return render(request, 'paintwaleapp/about.html')
def service(request):

    return render(request, 'paintwaleapp/services.html', {'service_data': service_data})