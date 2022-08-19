from django.urls import path
from .views import HomePageView, SnackDetail, SnackList

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('snack_list/', SnackList.as_view(), name='list_snacks'),
    path('<int:pk>/', SnackDetail.as_view(), name='detail_snack'),
]