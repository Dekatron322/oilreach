from django.urls import path
from . import views

app_name = "main"

urlpatterns = [

	path("", views.IndexView, name="index"),
	path("about/", views.AboutView, name="about"),
	path("projects/", views.ProjectsView, name="projects"),
	path("contact/", views.ContactView, name="contact"),
	path("contact/", views.ContactView, name="contact"),
	path("services/", views.ServiceView, name="services"),

]