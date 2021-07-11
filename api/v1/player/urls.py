from django.urls import path
from . import views

urlpatterns = [
    path('', views.PlayerAPI.as_view()),
    path('<int:pk>', views.PlayerRetrieveUpdateDestroyAPIView.as_view()),
]
