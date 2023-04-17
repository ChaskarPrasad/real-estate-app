from django.urls import path
from .views import listings,single_listing,search
urlpatterns = [
    path('',listings,name="listings"),
    path('<int:listing_id>',single_listing,name="listing"),
    path('search',search,name="search"),
]
