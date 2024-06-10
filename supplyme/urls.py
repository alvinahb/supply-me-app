from django.urls import path

from supplyme import views

urlpatterns = [
    path("", views.index, name="index"),
    path("connexion", views.user_login, name="login"),
    path("deconnexion", views.user_logout, name="logout"),
]
