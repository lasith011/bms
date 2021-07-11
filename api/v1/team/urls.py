from django.urls import path
from . import views

urlpatterns = [
    path('', views.TeamAPI.as_view()),
    path('<int:pk>', views.TeamRetrieveUpdateDestroyAPIView.as_view()),
]
