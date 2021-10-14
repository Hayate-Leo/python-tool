from django.urls import path
from .views import HomeTemplateView, ContactFormView, BlogListView

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('blog/', BlogListView.as_view(), name='blog'),
    path('contact/', ContactFormView.as_view(), name='contact'),
]