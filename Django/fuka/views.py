from django.db.models import query
from django.views.generic import ListView, DetailView
from .models import Search
from django.http import JsonResponse

class FukaListView(ListView):
    model = Search
    template_name = 'fuka/home.html'
    context_object_name = 'searchs'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        data = [12, 19, 30, 50, 20, 30, 24]
        context['data_list'] = data
        return context 

class FukaDetailView(DetailView):
    model = Search
    template_name = 'fuka/detail.html'

def chart_data(request, pk=1):

    queryset = Search.objects.all()
    id = pk - 1
    label = queryset[id].re_area.split(',')
    rate = queryset[id].re_rate.split(',')

    data={
        'labels': label,
        'data': rate,
    }

    return JsonResponse(data)