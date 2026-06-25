

from django.shortcuts import render, redirect
from .models import Complaint


def home(request):
    total = Complaint.objects.count()
    submitted = Complaint.objects.filter(status="Submitted").count()
    resolved = Complaint.objects.filter(status__iexact="resolved").count()
    

    return render(request, 'home.html', {
        'total': total,
        'submitted': submitted,
        'resolved': resolved
    })

def register(request):
    
    

    if request.method == "POST":
        complaint = Complaint.objects.create(
    name=request.POST['name'],
    mobile=request.POST['mobile'],
    address=request.POST['address'],
    complaint_type=request.POST['complaint_type'],
    description=request.POST['description'],
    image=request.FILES.get('image'),

    latitude=request.POST.get('latitude'),
    longitude=request.POST.get('longitude')
)
        
        
        
       
        return render(
            request,
            'success.html',
            {'complaint': complaint}
        )

    return render(request, 'register.html')

def track(request):
    complaint = None

    if request.method == "POST":
        cid = request.POST['complaint_id']

        try:
            complaint = Complaint.objects.get(id=cid)
        except:
            complaint = None

    return render(request, 'track.html', {'complaint': complaint})

def emergency(request):
    return render(request, 'emergency.html')



def complaints_list(request):
    complaints = Complaint.objects.all().order_by('-id')

    return render(
        request,
        'complaints_list.html',
        {'complaints': complaints}
    )