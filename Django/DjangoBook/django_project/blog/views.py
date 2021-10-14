from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView
from .forms import ContactForm
from django.urls import reverse_lazy
from .models import Contact, Blog
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q


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

    def get_queryset(self, **kwargs):
        queryset = super().get_queryset(**kwargs)
        query = self.request.GET

        if q := query.get('q'):
            queryset = queryset.filter(Q(content__icontains=q)|Q(title__icontains=q))

        return queryset.order_by('-created_at')