from django.urls import path
from . import views

urlpatterns = [
    path("", views.describe_index, name="describe_index"),
    path("<int:pk>/", views.describe_detail, name="describe_detail"),
]
