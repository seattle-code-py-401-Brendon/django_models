from django.views.generic import TemplateView, ListView, DetailView
from snacks.models import Snack

class HomePageView(TemplateView):
    template_name = "home.html"
    
class SnackList(ListView):
    template_name = "snack-list.html"
    model = Snack
    context_object_name = 'snacks'

class SnackDetail(DetailView):
    template_name = 'snack-detail.html'
    model = Snack