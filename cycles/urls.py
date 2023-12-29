from django.urls import path, include
from .views import (
    CycleApiView,
    CycleDetailApiView,
)

urlpatterns = [
    path('cycles', CycleApiView.as_view()),
    path('cycles/<int:cycle_id>', CycleDetailApiView.as_view()),
]