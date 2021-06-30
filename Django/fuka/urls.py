from django.urls import path
from .views import FukaListView, FukaDetailView
from . import views

urlpatterns = [
    path('', FukaListView.as_view(), name='fuka-home'),
    path('<int:pk>/', FukaDetailView.as_view(), name='fuka-detail'),
    path('api/chart/<int:pk>', views.chart_data, name='api-chart'),
]