<<<<<<< HEAD
from rest_framework import serializers, validators
from django.utils.translation import gettext_lazy as _
=======
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers, validators
>>>>>>> main

from ..models import Event, Participant
from .tag import TagSerializer


class EventSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    taken_seats = serializers.IntegerField(read_only=True)
    booked = serializers.BooleanField(default=False, read_only=True)

    class Meta:
        model = Event
        exclude = ['participants']


class ParticipantSerializer(serializers.ModelSerializer):
    participant = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Participant
        fields = '__all__'
        validators = [
            validators.UniqueTogetherValidator(
                queryset=Participant.objects.all(),
                fields=['event', 'participant'],
                message=_('Вы уже зарегестрированы на это событие')
            )
        ]
