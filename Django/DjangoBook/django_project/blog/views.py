from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from .forms import ContactForm
from django.urls import reverse_lazy
from .models import Contact


class HomeTemplateView(TemplateView):
    template_name = 'blog/home.html'


class ContactFormView(CreateView):
    template_name = 'blog/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('home')
    model = Contact