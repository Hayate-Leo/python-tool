from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView
from .forms import ContactForm
from django.urls import reverse_lazy
from .models import Contact, Blog
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.http import JsonResponse

class HomeTemplateView(TemplateView):
    template_name = 'blog/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blogs'] = Blog.objects.all()
        return context


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

        return queryset.order_by('-created_at')\

def line_chart(request):
    data = [1415, 1307, 1496, 1394, 1984]
    return JsonResponse(data={
        'data': data,
    })