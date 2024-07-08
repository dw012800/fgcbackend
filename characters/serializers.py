# from .models import Character
# from .models import Move
# from django.contrib.auth.models import User, Group
# from rest_framework import serializers

# # Our TodoSerializer
# class CharacterSerializer(serializers.HyperlinkedModelSerializer):
#         moves = MoveSerializer(many=True, read_only=True)
#     class Meta:
#         # The model it will serialize
#         model = Character
#         # the fields that should be included in the serialized output
#         fields = ['id', 'name', 'details']

# class MoveSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Move
#         fields = ['character', 'id', 'command', 'hitlevel', 'damage', 'startup', 'hit', 'counterhit']

from rest_framework import serializers
from .models import Character, Move

class MoveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Move
        fields = '__all__'

class CharacterSerializer(serializers.ModelSerializer):
    moves = MoveSerializer(many=True, read_only=True)

    class Meta:
        model = Character
        fields = '__all__'
