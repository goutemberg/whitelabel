from django.urls import path
from home.views import index
from . import views



urlpatterns = [
    path('', index, name='index'),
    path('send-email/', views.send_email_view, name='send_email_view'),
  
]