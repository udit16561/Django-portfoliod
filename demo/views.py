
from django.shortcuts import render
from django.http import HttpResponse
from contact.models import contact
from resume.models import resume
from client.models import contactEnquiry

def homepage(request):
    if request.method=="Post":
        name=request.Post.get('name')
        Email=request.Post.get('email')
        message=request.Post.get('message')
        en=contactEnquiry(name=name,Email=Email,message=message)
        en.save()

    contactsData=contact.objects.all()
    resumeData=resume.objects.all()
    data={
        'contactsData':contactsData,
        'resumeData':resumeData,
    }
    return render(request,'index.html',data)

