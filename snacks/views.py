from django.views.generic import TemplateView


class Snacklistview(TemplateView):
    template_name = 'snack_list.html'
