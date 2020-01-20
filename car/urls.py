# Create your views here.
from django.conf.urls import url
from . import views
from django.contrib.auth.views import LoginView

urlpatterns=[
    url(r'^$',views.carbooking, name='carbooking'),
    url(r'^login/$', LoginView.as_view(template_name="car/login.html"), name="login"),
    url(r'^logout/$', LoginView.as_view(template_name="car/logout.html"), name="logout"),
    url(r'^car_booking_submission/$',views.car_booking_submission,name='car_booking_submission'),
    ]
