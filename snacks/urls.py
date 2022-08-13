from django.urls import path
from .views import Snacklistview

urlpatterns = [
    path('', Snacklistview.as_view(), name='snack_list'),
]