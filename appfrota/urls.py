from django.conf.urls import include
from django.urls import path
from .views import SignUpView, setTripView, saveTripView


urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("set_trip/", setTripView, name="set_trip"),
    path("save_trip/", saveTripView, name="save_trip"),
]