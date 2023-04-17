from django.shortcuts import render,redirect
from listings.models import Listing
from . models import Contact
from django.contrib import messages
from django.core.mail import send_mail
# Create your views here.

def submit_request(request,id):
    if request.method=='POST':
        listing = Listing.objects.filter(id=id)[0]
        name    = request.POST["name"]
        email   = request.POST["email"]   
        message = request.POST["message"]
        user_id = request.POST["user_id"]
        listing_id = id
        realtor_email = request.POST["realtor_email"]

        #check user already made inquiry
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=id,user_id=user_id)
            if has_contacted:
                messages.error(request,"You have already made an inquiry for this listing")
                return redirect("/listings/"+str(id))
            
        contact = Contact(listing=listing,listing_id=listing_id,name=name,email=email,message=message,user_id=user_id)
        contact.save()

        #send mail tp realtor
        send_mail(
            "Property Listing Inquiry",
            f"There is has been inquiry for {listing}.",
            "Your email from which you need to send email",
            [realtor_email],
            fail_silently=False,
        )
        messages.success(request,"Your request has been submitted, a realtor will get back to you soon")
        return redirect("/listings/"+str(id))
    return render(request,'listings/single_listing.html')
