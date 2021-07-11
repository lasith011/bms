from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.db.models import Avg, Sum, Count

from api.models import Team, Player, TeamStat
from . import serializer


class TeamAPI(ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = serializer.TeamSerializer
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class TeamRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = serializer.TeamSerializer

    def retrieve(self, request, *args, **kwargs):
        team_id = self.kwargs.get('pk', None)
        players = Player.objects.filter(team_id=team_id)
        return Response({
            'players': players,
            'average_score': TeamStat.objects.filter(team_id=team_id).aggregate(Avg('score')),
        })
