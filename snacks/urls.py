from django.urls import path
from snacks.api.viewsets import (
    SnackListView,
    SnackDetailView,
)

urlpatterns = [
    path('snacks-list', SnackListView.as_view(), name='snack_list'),
    path('snack-detail/<int:pk>', SnackDetailView.as_view(), name='snack_detail'),
]