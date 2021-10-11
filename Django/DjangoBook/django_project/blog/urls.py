from django.urls import path
from .views import HomeTemplateView, ContactFormView

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('contact/', ContactFormView.as_view(), name='contact'),
]