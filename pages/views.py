from django.shortcuts import render
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import state_choices,price_choices,bedroom_choices
# Create your views here.

def home(request):
    listings = Listing.objects.order_by("-list_date")[:3]
    contex = {
        "listings":listings,
        "state_choices":state_choices,
        "price_choices":price_choices,
        "bedroom_choices":bedroom_choices
    }
    return render(request,'pages/index.html',contex)

def about(request):
    realtors = Realtor.objects.all()

    #get mvp realtors
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)
    context = {
        "realtors":realtors,
        "mvp_realtors":mvp_realtors
    }

    return render(request,'pages/about.html',context)