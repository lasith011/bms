from django.urls import path, include

urlpatterns = [
    path('team/', include('api.v1.team.urls')),
    path('player/', include('api.v1.player.urls')),
    path('user/', include('api.v1.user.urls')),
]
