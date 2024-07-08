
# from .models import Character, Move
# from rest_framework import viewsets
# from rest_framework import permissions
# from rest_framework.decorators import action
# from rest_framework.response import Response
# from .serializers import CharacterSerializer, MoveSerializer


# class CharacterViewSet(viewsets.ModelViewSet):
#     ## The Main Query for the index route
#     queryset = Character.objects.all()
#     # The serializer class for serializing output
#     serializer_class = CharacterSerializer
#     # optional permission class set permission level
#     permission_classes = [permissions.AllowAny] #Coule be [permissions.IsAuthenticated]

# class MoveViewSet(viewsets.ModelViewSet):
#     ## The Main Query for the index route
#     queryset = Move.objects.all()
#     # The serializer class for serializing output
#     serializer_class = MoveSerializer
#     # optional permission class set permission level
#     permission_classes = [permissions.AllowAny] #Coule be [permissions.IsAuthenticated]

# # URL: http://localhost:8000/moves/character/<characterid>/
# @action(detail=False, methods=['get'], url_path='character/(?P<character_name>[^/.]+)')
# def character_moves(self, request, character_name=None):
#         try:
#             character = Character.objects.get(name=character_name)
#             moves = self.queryset.filter(character=character)
#             serializer = self.get_serializer(moves, many=True)
#             return Response(serializer.data)
#         except Character.DoesNotExist:
#             return Response({"message": f"Character '{character_name}' does not exist."}, status=404)
from .models import Character, Move
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import CharacterSerializer, MoveSerializer


class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    permission_classes = [permissions.AllowAny]


class MoveViewSet(viewsets.ModelViewSet):
    queryset = Move.objects.all()
    serializer_class = MoveSerializer
    permission_classes = [permissions.AllowAny]

    @action(detail=False, methods=['get'], url_path='character/(?P<character_name>[^/.]+)')
    def character_moves(self, request, character_name=None):
        try:
            character = Character.objects.get(name=character_name)
            moves = self.queryset.filter(character=character)
            serializer = self.get_serializer(moves, many=True)
            return Response(serializer.data)
        except Character.DoesNotExist:
            return Response({"message": f"Character '{character_name}' does not exist."}, status=404)
