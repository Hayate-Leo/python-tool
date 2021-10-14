from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView
from .forms import ContactForm
from django.urls import reverse_lazy
from .models import Contact, Blog
from django.contrib.messages.views import SuccessMessageMixin


class HomeTemplateView(TemplateView):
    template_name = 'blog/home.html'


class ContactFormView(SuccessMessageMixin, CreateView):
    template_name = 'blog/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('home')
    model = Contact
    success_message = 'お問い合わせありがとうございました。'

class BlogListView(ListView):
    model = Blog
    template_name = 'blog/blog.html'
    context_object_name = 'results'
    paginate_by = 3