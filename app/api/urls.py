from django.urls import path
from .views import HelloWorld
from .views import Students
from .views import ContactListView



urlpatterns = [
    path('hello/', HelloWorld.as_view(), name='hello_world'),
    path('Students/', Students.as_view(), name='list_student'),
    path('contact/', ContactListView.as_view(), name='contact_new'),



]
