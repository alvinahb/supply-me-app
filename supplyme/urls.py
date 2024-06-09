from django.urls import path

from supplyme import views

urlpatterns = [
    path("", views.index, name="index"),
]
