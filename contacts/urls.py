from django.urls import path
from . views import submit_request
urlpatterns = [
    path("submit-request/<int:id>",submit_request,name="submit-request")
]
