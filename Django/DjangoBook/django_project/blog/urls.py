from django.urls import path
from .views import HomeTemplateView, ContactFormView, BlogListView
from . import views

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('blog/', BlogListView.as_view(), name='blog'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('line-chart/', views.line_chart, name='line-chart'),
]