from django.db.models import Avg
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from api.models import Player, PlayerStat
from . import serializer


class PlayerAPI(ListCreateAPIView):
    queryset = Player.objects.all()
    serializer_class = serializer.PlayerSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class PlayerRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = serializer.PlayerSerializer

    def retrieve(self, request, *args, **kwargs):
        player_id = self.kwargs.get('pk', None)
        player = Player.objects.filter(id=player_id).first()
        # stat = PlayerStat.objects.filter(player_id=player_id)
        return Response({
            # 'player': player,
            'id': player.id,
            'team': player.team.name,
            # 'games': len(stat),
            'average_score': PlayerStat.objects.filter(player_id=player_id).aggregate(Avg('score'))
        })
