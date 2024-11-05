from django.urls import path
from . import views

urlpatterns = [
    path("", views.chat, name="chat"),  # This will route to the new index.html
]
