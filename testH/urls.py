from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
     path("index", views.normal, name="homepage"),
    path("", views.contact_view, name="mailsend"),
    

]
